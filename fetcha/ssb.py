import logging
import requests
import json

import numpy as np
import pandas as pd
from pyjstat import pyjstat

logger = logging.getLogger(__name__)


class SSB:
    """Communcation with SSB.

    Terminology
    -----------
    name : ContentsCode
    label : 'Pengemengden M3. Beholdninger, sesongjustert (mill. kr)'
    code : 'M3SesJust'
    """

    def __init__(self, table_id, language="no"):
        """
        Parameters
        ----------
        table_id : str
        language : str
            no or en
        """
        assert language in ("no", "en"), "language can only be 'no' or 'en'."

        self.table_id = table_id
        self.language = language
        self.url = "https://data.ssb.no/api/v0/{}/table/{}".format(
            self.language, self.table_id
        )
        self.levels = pd.read_json(self.url, orient="columns")["variables"]

    def __repr__(self):
        return "SSB(table_id=%r, language=%r)" % (self.table_id, self.language)

    def periods(self):
        """All available periods.

        Returns
        -------
        list of str representing periods.
        """
        return self._labels()["Tid"]

    def max_period(self):
        """Latest period available.

        Returns
        -------
        max_p : str
        """
        max_p = max(self.periods())
        return max_p

    def min_period(self):
        """Earlies period available.

        Returns
        -------
        min_p : str
        """
        min_p = min(self.periods())
        return min_p

    def _codes(self):
        """Map between names and codes.
        Uses mapping from last period and assumes it to be constant through out all time.
            
        Returns
        -------
        lvl_codes : dict
        """
        period = self.max_period()

        lvl_codes = {}
        for lvl in self.levels:
            if lvl["code"] == "Tid":
                lvl_codes[lvl["code"]] = [period]
            else:
                lvl_codes[lvl["code"]] = lvl["values"]
        return lvl_codes

    def _labels(self):
        """Map between names and labels.
        
        Returns
        -------
        lvl_codes : dict
            Mapping level names to labels.
        """
        lvl_codes = {}
        for lvl in self.levels:
            lvl_codes[lvl["code"]] = lvl["valueTexts"]
        return lvl_codes

    def _codes_and_labels(self):
        """Mapping between codes and labels.

        Returns
        -------
        codes_and_labels : dict
        """
        codes_and_labels = {}
        for lvl in self.levels:
            d_mapping = {}
            for code, label in zip(lvl.get("values"), lvl.get("valueTexts")):
                d_mapping[label] = code
            codes_and_labels[lvl.get("text")] = d_mapping
        return codes_and_labels

    def _add_id_cols(self, df):
        """Add columns containing codes used to make request to api.
        Useful if you for example want to make same request again to verify results.

        Returns
        -------
        df : pandas dataframe
        """
        for col in df:
            if col != "value":
                df[col + "_id"] = df[col].replace(self._codes_and_labels().get(col))
        return df

    def _nrows(self, mapping):
        """Number of rows in table.
        
        Parameters
        ----------
        mapping : dict
            Mapping between names and codes, or names and labels.
            If between names and codes we get the number of rows to fetch next.
            If between names and labels, we get total number of rows in a table.
        Returns
        -------
        prod : int
        """
        prod = np.prod([len(val) for val in mapping.values()])
        return prod

    def nrows_tot(self):
        """Total number of rows that can be fetched.

        Returns
        -------
        int
        """
        return self._nrows(self._labels())

    def nrows_period(self):
        """Number of rows per period.

        Returns
        -------
        int
        """
        return int(self.nrows_tot() / len(self.periods()))

    def nrows_query(self, query):
        return self._nrows(query)

    def _index_cols(self):
        """Columns comprising index.

        Returns
        -------
        index_cols : list of str
        """
        index_cols = [lvl.get("text") for lvl in self.levels]
        return index_cols

    def _req2data(self, req):
        """Convert requests object to pandas dataframe using third-party package.

        Parameters
        ----------
        req : request object

        Returns
        -------
        df : pandas dataframe
        """
        dataset = pyjstat.Dataset.read(req.text)
        df = dataset.write("dataframe")
        # OK to drop duplicates taking into account all columns,
        # and not only columns comprising the index.
        # See for example https://www.ssb.no/statbank/table/09560/,
        # Here `Låntakersektor` can be either `Hovedsektor` or `Detaljer Sektor`,
        # which might give duplicates.
        df = df.drop_duplicates()

        return df

    def fetch(self, period=None, id_cols=False, fltr=None):
        """Get data for a set of periods, a single period or latest period.

        Parameters
        ----------
        period : str or list of str
            Period(s) with format suitable for table.
            If None, get latest.
        id_cols : bool
            If True appends columns containing codes used to call api.
        fltr : list of dicts

        Returns
        -------
        df : pandas dataframe
        """
        # TODO: Think of a better variable names. Too many similar "period" names.
        if period is None:
            _period = [max(self._labels()["Tid"])]
        elif not isinstance(period, list):
            _period = [period]
        else:
            _period = period

        # Reason for looping over self.periods() is so the function works
        # when period is f.ex 2020M01, 2020K01 or the whole year 2020.
        # It will work when period is 20, or anything else that can be found in self.periods().
        periods = []
        for p in _period:
            for per in self.periods():
                if p in per:
                    periods.append(per)

        codes = self._codes()
        labels = self._labels()

        codes["Tid"] = periods

        query = []
        for key, val in codes.items():
            values = None
            if fltr is not None:
                for q in fltr:
                    if key in q.get("code"):
                        values = q.get("values")
            if values is not None:
                val = values
            selection = {"filter": "item", "values": val}
            query.append({"code": key, "selection": selection})

        body = {}
        body["query"] = query
        body["response"] = {"format": "json-stat2"}

        nrows_query = 1
        for q in query:
            nrows_query = nrows_query * len(q.get("selection").get("values"))

        if nrows_query >= 300000:
            logger.warning(
                "Query exceeds SSB limit of 300k rows per transaction. Current query tries to fetch {} rows. User a filter".format(
                    nrows_query
                )
            )
            return None

        req = requests.post(url=self.url, verify=True, json=body)

        df = self._req2data(req)

        if id_cols:
            df = self._add_id_cols(df)

        try:
            df = df.set_index(self._index_cols(), verify_integrity=True)
        except:
            logger.warning("Duplicates found in index columns. Will not set index.")

        return df
