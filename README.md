# fetcha

Talk to SSB using Python.


```python
import fetcha as fetcha
import logging
# Turn off INFO-warnings
logging.getLogger().setLevel(logging.CRITICAL)
```

## Installation


```python
pip install git+https://github.com/dafeda/fetcha.git --upgrade
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




    1395




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




    ['2020M05', '2020M06', '2020M07', '2020M08', '2020M09', '2020M10', '2020M11']




```python
# Fetch latest period.
# Returns a pandas dataframe with its index set with verify_integrity set to True.
# If the dataframe is lacking an index, it means that the index columns do not make up a unique combination.
df_latest = ssb_10945.fetch()
df_latest.head()
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
      <th>Monetary aggregate M1. Stocks (NOK million)</th>
      <th>2020M11</th>
      <td>2485877.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M2. Stocks (NOK million)</th>
      <th>2020M11</th>
      <td>2656368.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M3. Stocks (NOK million)</th>
      <th>2020M11</th>
      <td>2658168.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M1. Transactions last 12 months (NOK million)</th>
      <th>2020M11</th>
      <td>300287.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M2. Transactions last 12 months (NOK million)</th>
      <th>2020M11</th>
      <td>286364.0</td>
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
# Reset index before pivoting
df_year = df_year.reset_index().pivot(index="month", columns="contents")
df_year.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="9" halign="left">value</th>
    </tr>
    <tr>
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
      <th>2020M01</th>
      <td>3.2</td>
      <td>2183983.0</td>
      <td>67827.0</td>
      <td>3.9</td>
      <td>2366374.0</td>
      <td>89213.0</td>
      <td>3.8</td>
      <td>2369935.0</td>
      <td>86503.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>3.3</td>
      <td>2177656.0</td>
      <td>67999.0</td>
      <td>3.9</td>
      <td>2362458.0</td>
      <td>88323.0</td>
      <td>3.8</td>
      <td>2366007.0</td>
      <td>85100.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>7.1</td>
      <td>2302575.0</td>
      <td>150339.0</td>
      <td>7.5</td>
      <td>2491535.0</td>
      <td>172563.0</td>
      <td>7.4</td>
      <td>2494933.0</td>
      <td>169831.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>9.9</td>
      <td>2342854.0</td>
      <td>207753.0</td>
      <td>9.6</td>
      <td>2524788.0</td>
      <td>218422.0</td>
      <td>9.5</td>
      <td>2528204.0</td>
      <td>216825.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>11.1</td>
      <td>2377047.0</td>
      <td>234673.0</td>
      <td>10.3</td>
      <td>2554949.0</td>
      <td>236943.0</td>
      <td>10.2</td>
      <td>2558258.0</td>
      <td>234366.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
ssb_10948 = fetcha.SSB("10948", language="en")
df_10948 = ssb_10948.fetch("2020")
```


```python
df_10948.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>value</th>
    </tr>
    <tr>
      <th>holding sector</th>
      <th>contents</th>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Money holding sector</th>
      <th rowspan="5" valign="top">Monetary aggregate M3. Stocks, seasonally adjusted (NOK million)</th>
      <th>2020M01</th>
      <td>2375314.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>2390118.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>2501374.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>2546104.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>2582335.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Fetch and join
# Get another table so we have something to join with.
ssb_10948 = fetcha.SSB("10948", language="en")
df_10948 = ssb_10948.fetch("2020")
df_10948 = df_10948.reset_index().pivot_table(
    index="month", columns="contents", aggfunc="mean"
)

df_10948.join(df_year).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="12" halign="left">value</th>
    </tr>
    <tr>
      <th>contents</th>
      <th>1-month growth, seasonally adjusted (per cent)</th>
      <th>Monetary aggregate M3. Stocks, seasonally adjusted (NOK million)</th>
      <th>Transactions last month, seasonally adjusted (NOK million)</th>
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
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020M01</th>
      <td>-10.54</td>
      <td>950125.6</td>
      <td>-1419.8</td>
      <td>3.2</td>
      <td>2183983.0</td>
      <td>67827.0</td>
      <td>3.9</td>
      <td>2366374.0</td>
      <td>89213.0</td>
      <td>3.8</td>
      <td>2369935.0</td>
      <td>86503.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>4.64</td>
      <td>956047.2</td>
      <td>3677.4</td>
      <td>3.3</td>
      <td>2177656.0</td>
      <td>67999.0</td>
      <td>3.9</td>
      <td>2362458.0</td>
      <td>88323.0</td>
      <td>3.8</td>
      <td>2366007.0</td>
      <td>85100.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>521.06</td>
      <td>1000549.6</td>
      <td>38143.8</td>
      <td>7.1</td>
      <td>2302575.0</td>
      <td>150339.0</td>
      <td>7.5</td>
      <td>2491535.0</td>
      <td>172563.0</td>
      <td>7.4</td>
      <td>2494933.0</td>
      <td>169831.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>22.56</td>
      <td>1018441.6</td>
      <td>19292.4</td>
      <td>9.9</td>
      <td>2342854.0</td>
      <td>207753.0</td>
      <td>9.6</td>
      <td>2524788.0</td>
      <td>218422.0</td>
      <td>9.5</td>
      <td>2528204.0</td>
      <td>216825.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>14.30</td>
      <td>1032934.0</td>
      <td>17314.6</td>
      <td>11.1</td>
      <td>2377047.0</td>
      <td>234673.0</td>
      <td>10.3</td>
      <td>2554949.0</td>
      <td>236943.0</td>
      <td>10.2</td>
      <td>2558258.0</td>
      <td>234366.0</td>
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




```python
df_10261.sample(10)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>value</th>
    </tr>
    <tr>
      <th>region</th>
      <th>sex</th>
      <th>age</th>
      <th>diagnosis: Chapter in ICD-10</th>
      <th>contents</th>
      <th>year</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="10" valign="top">The whole country</th>
      <th rowspan="4" valign="top">Females</th>
      <th>40-59 years</th>
      <th>Parkinson's disease</th>
      <th>Patients with day cases</th>
      <th>2019</th>
      <td>11.0</td>
    </tr>
    <tr>
      <th>Years, total</th>
      <th>Diseases of appendix</th>
      <th>Number of in-patient stays (discharges)</th>
      <th>2019</th>
      <td>3173.0</td>
    </tr>
    <tr>
      <th>60-69 years</th>
      <th>Dorsopathies</th>
      <th>Number of out-patient consultations</th>
      <th>2019</th>
      <td>9237.0</td>
    </tr>
    <tr>
      <th>0-9 years</th>
      <th>Delivery</th>
      <th>Number of out-patient consultations</th>
      <th>2019</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Both sexes</th>
      <th rowspan="2" valign="top">40-59 years</th>
      <th>Arthrosis</th>
      <th>Number of day cases</th>
      <th>2019</th>
      <td>1859.0</td>
    </tr>
    <tr>
      <th>Melanoma and other malignant neoplasms of skin</th>
      <th>Patients at general hospital, in total</th>
      <th>2019</th>
      <td>3276.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Females</th>
      <th>Years, total</th>
      <th>In situ neoplasms and neoplasms of uncertain or unknown behaviour</th>
      <th>Out-patients</th>
      <th>2019</th>
      <td>11339.0</td>
    </tr>
    <tr>
      <th>40-59 years</th>
      <th>Acute myocardial infarction</th>
      <th>Patients at general hospital, in total</th>
      <th>2019</th>
      <td>440.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Both sexes</th>
      <th>20-39 years</th>
      <th>Influenza and pneumonia</th>
      <th>Number of in-patient stays (discharges)</th>
      <th>2019</th>
      <td>1695.0</td>
    </tr>
    <tr>
      <th>10-19 years</th>
      <th>Non-infective enteritis and colitis</th>
      <th>Number of out-patient consultations</th>
      <th>2019</th>
      <td>7595.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
