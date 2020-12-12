# fetcha

Talk to SSB using Python.


```python
import fetcha as fetcha
```


```python
# Instantiate object with specific table_id that refers to a SSB-table.
# 10945 refers to Monetary aggregates M1, M2 and M3:
# https://www.ssb.no/en/statbank/table/10945
ssb_10945 = fetcha.SSB("10945", language="en")
```


```python
# Number of rows in table.
ssb_10945.nrows_tot()
```




    1386




```python
# Number of rows per period.
ssb_10945.nrows_period()
```




    9




```python
# Get all available periods
periods = ssb_10945.periods()
periods[-7:]
```




    ['2020M04', '2020M05', '2020M06', '2020M07', '2020M08', '2020M09', '2020M10']




```python
# Fetch latest period.
# Returns a pandas dataframe with its index set with verify_integrity set to True.
# If the dataframe is lacking an index, it means that the index columns do not make up a unique combination.
df_latest = ssb_10945.fetch()
df_latest.head()
```




<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>value</th>
    </tr>
    <tr>
      <th>contents</th>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Monetary aggregate M1. Stocks (NOK million)</th>
      <th>2020M10</th>
      <td>2465888.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M2. Stocks (NOK million)</th>
      <th>2020M10</th>
      <td>2638785.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M3. Stocks (NOK million)</th>
      <th>2020M10</th>
      <td>2639552.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M1. Transactions last 12 months (NOK million)</th>
      <th>2020M10</th>
      <td>284198.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M2. Transactions last 12 months (NOK million)</th>
      <th>2020M10</th>
      <td>274456.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Fetch list of periods
df_periods = ssb_10945.fetch(["2019M12", "2020M01", "2020M02"])
df_periods.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>value</th>
    </tr>
    <tr>
      <th>contents</th>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">Monetary aggregate M1. Stocks (NOK million)</th>
      <th>2019M12</th>
      <td>2159770.0</td>
    </tr>
    <tr>
      <th>2020M01</th>
      <td>2183983.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>2177656.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Monetary aggregate M2. Stocks (NOK million)</th>
      <th>2019M12</th>
      <td>2345545.0</td>
    </tr>
    <tr>
      <th>2020M01</th>
      <td>2366374.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Fetch whole year of data
df_year = ssb_10945.fetch("2020")
df_year.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>value</th>
    </tr>
    <tr>
      <th>contents</th>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Monetary aggregate M1. Stocks (NOK million)</th>
      <th>2020M01</th>
      <td>2183983.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>2177656.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>2302575.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>2342854.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>2377047.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Fetch multiple years
df_years = ssb_10945.fetch(["2019", "2020"])
df_year.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>value</th>
    </tr>
    <tr>
      <th>contents</th>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Monetary aggregate M1. Stocks (NOK million)</th>
      <th>2020M01</th>
      <td>2183983.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>2177656.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>2302575.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>2342854.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>2377047.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Pivot helper function - a thin wrapper over pandas' pivot_table.
ssb_10945.pivot(df_year)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>contents</th>
      <th>Monetary aggregate M1. 12-month growth (per cent</th>
      <th>Monetary aggregate M1. Stocks (NOK million)</th>
      <th>Monetary aggregate M1. Transactions last 12 months (NOK million)</th>
      <th>Monetary aggregate M2. 12-month growth (per cent)</th>
      <th>Monetary aggregate M2. Stocks (NOK million)</th>
      <th>Monetary aggregate M2. Transactions last 12 months (NOK million)</th>
      <th>Monetary aggregate M3. 12-month growth (per cent)</th>
      <th>Monetary aggregate M3. Stocks (NOK million)</th>
      <th>Monetary aggregate M3. Transactions last 12 months (NOK million)</th>
    </tr>
    <tr>
      <th>contents</th>
      <th>month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Monetary aggregate M1. 12-month growth (per cent</th>
      <th>2020M01</th>
      <td>3.2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>3.3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>7.1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>9.9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>11.1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Monetary aggregate M3. Transactions last 12 months (NOK million)</th>
      <th>2020M06</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>191747.0</td>
    </tr>
    <tr>
      <th>2020M07</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>236189.0</td>
    </tr>
    <tr>
      <th>2020M08</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>214480.0</td>
    </tr>
    <tr>
      <th>2020M09</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>253167.0</td>
    </tr>
    <tr>
      <th>2020M10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>270959.0</td>
    </tr>
  </tbody>
</table>
<p>90 rows × 9 columns</p>
</div>




```python
# Fetch and join
# Get another table so we have something to join with.
ssb_10948 = fetcha.SSB("10948", language="en")
df_10948 = ssb_10948.pivot(ssb_10948.fetch("2020"))

df_10948.join(df_year)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>1-month growth, seasonally adjusted (per cent)</th>
      <th>Monetary aggregate M3. Stocks, seasonally adjusted (NOK million)</th>
      <th>Transactions last month, seasonally adjusted (NOK million)</th>
      <th>value</th>
    </tr>
    <tr>
      <th>contents</th>
      <th>month</th>
      <th>holding sector</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">1-month growth, seasonally adjusted (per cent)</th>
      <th rowspan="5" valign="top">2020M01</th>
      <th>Households etc.</th>
      <td>5.5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Money holding sector</th>
      <td>-1.8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Municipal government</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Non-financial corporations</th>
      <td>0.9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Other financial corporations</th>
      <td>-60.4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Transactions last month, seasonally adjusted (NOK million)</th>
      <th rowspan="5" valign="top">2020M10</th>
      <th>Households etc.</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>18913.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Money holding sector</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>20794.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Municipal government</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>4598.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Non-financial corporations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>9139.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Other financial corporations</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-11856.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 4 columns</p>
</div>




```python
# Use id when pivoting for prettier column names.
df_10945_id = ssb_10945.pivot(ssb_10945.fetch(id_cols=True), "contents_id")
```


```python
df_10945_id.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>contents_id</th>
      <th>M1TolvMndVekst</th>
      <th>M2TolvMndVekst</th>
      <th>M3TolvMndVekst</th>
      <th>PengMengdtransM1</th>
      <th>PengmengdBehM1</th>
      <th>PengmengdBehM2</th>
      <th>PengmengdBehM3</th>
      <th>PengmengdTransM2</th>
      <th>PengmengdTransM3</th>
    </tr>
    <tr>
      <th>contents</th>
      <th>month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Monetary aggregate M1. 12-month growth (per cent</th>
      <th>2020M10</th>
      <td>13.1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Monetary aggregate M1. Stocks (NOK million)</th>
      <th>2020M10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2465888.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Monetary aggregate M1. Transactions last 12 months (NOK million)</th>
      <th>2020M10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>284198.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Monetary aggregate M2. 12-month growth (per cent)</th>
      <th>2020M10</th>
      <td>NaN</td>
      <td>11.6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Monetary aggregate M2. Stocks (NOK million)</th>
      <th>2020M10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2638785.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# SSB has a limit of 300k rows per transaction.
# Some tables have more than that in one period.
ssb_10261 = fetcha.SSB("10261", language="en")
```


```python
# Gives warning and returns None.
df_10261 = ssb_10261.fetch()
```

    WARNING:fetcha.ssb:Query exceeds SSB limit of 300k rows per transaction. Current query tries to fetch 499968 rows. User a filter



```python
# Can pass filter to fetch(), but first we need to choose what we want.
# Use variable levels to see which options you have.
ssb_10261.levels
```




    0    {'code': 'Region', 'text': 'region', 'values':...
    1    {'code': 'Kjonn', 'text': 'sex', 'values': ['0...
    2    {'code': 'Alder', 'text': 'age', 'values': ['9...
    3    {'code': 'Diagnose3', 'text': 'diagnosis: Chap...
    4    {'code': 'ContentsCode', 'text': 'contents', '...
    5    {'code': 'Tid', 'text': 'year', 'values': ['20...
    Name: variables, dtype: object




```python
# We limit the region to "The whole country".
ssb_10261.levels.iloc[0]
```




    {'code': 'Region',
     'text': 'region',
     'values': ['0',
      '01',
      '02',
      '03',
      '04',
      '05',
      '06',
      '07',
      '08',
      '09',
      '10',
      '11',
      '12',
      '14',
      '15',
      '50',
      '16',
      '17',
      '18',
      '19',
      '20',
      'F00',
      '9',
      'H03',
      'H04',
      'H05',
      'H12',
      'Uoppgitt'],
     'valueTexts': ['The whole country',
      'Østfold (-2019)',
      'Akershus (-2019)',
      'Oslo',
      'Hedmark (-2019)',
      'Oppland (-2019)',
      'Buskerud (-2019)',
      'Vestfold (-2019)',
      'Telemark (-2019)',
      'Aust-Agder (-2019)',
      'Vest-Agder (-2019)',
      'Rogaland',
      'Hordaland (-2019)',
      'Sogn og Fjordane (-2019)',
      'Møre og Romsdal',
      'Trøndelag - Trööndelage',
      'Sør-Trøndelag (-2017)',
      'Nord-Trøndelag (-2017)',
      'Nordland',
      'Troms - Romsa (-2019)',
      'Finnmark - Finnmárku (-2019)',
      'Total',
      'Uoppgitt',
      'Helseregion Vest',
      'Helseregion Midt-Norge',
      'Helseregion Nord',
      'Helseregion Sør-Øst',
      'Unknown'],
     'elimination': True}




```python
fltr = [{"code": "Region", "values": ["0"]}]
```


```python
df_10261 = ssb_10261.fetch(fltr=fltr)
```


```python
df_10261.shape
```




    (17856, 1)
