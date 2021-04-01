# fetcha

Talk to SSB using Python.


```python
import fetcha as fetcha
import logging
# Turn off INFO-warnings
logging.getLogger().setLevel(logging.WARNING)
```

## Installation


```python
# >> pip install git+https://github.com/dafeda/fetcha.git --upgrade
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




    1422




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




    ['2020M08', '2020M09', '2020M10', '2020M11', '2020M12', '2021M01', '2021M02']




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
      <th>2021M02</th>
      <td>2526071.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M2. Stocks (NOK million)</th>
      <th>2021M02</th>
      <td>2695383.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M3. Stocks (NOK million)</th>
      <th>2021M02</th>
      <td>2697783.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M1. Transactions last 12 months (NOK million)</th>
      <th>2021M02</th>
      <td>359029.0</td>
    </tr>
    <tr>
      <th>Monetary aggregate M2. Transactions last 12 months (NOK million)</th>
      <th>2021M02</th>
      <td>343687.0</td>
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
      <td>2182450.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>2175681.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Monetary aggregate M2. Stocks (NOK million)</th>
      <th>2019M12</th>
      <td>2345545.0</td>
    </tr>
    <tr>
      <th>2020M01</th>
      <td>2364841.0</td>
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
      <td>2182450.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>2175681.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>2300443.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>2340381.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>2374607.0</td>
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
      <td>2182450.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>2175681.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>2300443.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>2340381.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>2374607.0</td>
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
      <td>3.1</td>
      <td>2182450.0</td>
      <td>66236.0</td>
      <td>3.9</td>
      <td>2364841.0</td>
      <td>87622.0</td>
      <td>3.7</td>
      <td>2368402.0</td>
      <td>84912.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>3.2</td>
      <td>2175681.0</td>
      <td>66037.0</td>
      <td>3.8</td>
      <td>2360484.0</td>
      <td>86360.0</td>
      <td>3.7</td>
      <td>2364033.0</td>
      <td>83138.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>7.0</td>
      <td>2300443.0</td>
      <td>148469.0</td>
      <td>7.5</td>
      <td>2489403.0</td>
      <td>170692.0</td>
      <td>7.3</td>
      <td>2492801.0</td>
      <td>167960.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>9.8</td>
      <td>2340381.0</td>
      <td>205486.0</td>
      <td>9.5</td>
      <td>2522315.0</td>
      <td>216155.0</td>
      <td>9.4</td>
      <td>2525731.0</td>
      <td>214558.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>10.9</td>
      <td>2374607.0</td>
      <td>232311.0</td>
      <td>10.2</td>
      <td>2552508.0</td>
      <td>234581.0</td>
      <td>10.1</td>
      <td>2555817.0</td>
      <td>232003.0</td>
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
      <td>2374459.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>2387955.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>2499994.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>2543868.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>2580435.0</td>
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
      <td>-10.02</td>
      <td>949783.6</td>
      <td>-1329.8</td>
      <td>3.1</td>
      <td>2182450.0</td>
      <td>66236.0</td>
      <td>3.9</td>
      <td>2364841.0</td>
      <td>87622.0</td>
      <td>3.7</td>
      <td>2368402.0</td>
      <td>84912.0</td>
    </tr>
    <tr>
      <th>2020M02</th>
      <td>3.32</td>
      <td>955182.0</td>
      <td>3182.0</td>
      <td>3.2</td>
      <td>2175681.0</td>
      <td>66037.0</td>
      <td>3.8</td>
      <td>2360484.0</td>
      <td>86360.0</td>
      <td>3.7</td>
      <td>2364033.0</td>
      <td>83138.0</td>
    </tr>
    <tr>
      <th>2020M03</th>
      <td>541.24</td>
      <td>999997.4</td>
      <td>38556.4</td>
      <td>7.0</td>
      <td>2300443.0</td>
      <td>148469.0</td>
      <td>7.5</td>
      <td>2489403.0</td>
      <td>170692.0</td>
      <td>7.3</td>
      <td>2492801.0</td>
      <td>167960.0</td>
    </tr>
    <tr>
      <th>2020M04</th>
      <td>19.36</td>
      <td>1017547.0</td>
      <td>18928.0</td>
      <td>9.8</td>
      <td>2340381.0</td>
      <td>205486.0</td>
      <td>9.5</td>
      <td>2522315.0</td>
      <td>216155.0</td>
      <td>9.4</td>
      <td>2525731.0</td>
      <td>214558.0</td>
    </tr>
    <tr>
      <th>2020M05</th>
      <td>14.82</td>
      <td>1032174.2</td>
      <td>17398.2</td>
      <td>10.9</td>
      <td>2374607.0</td>
      <td>232311.0</td>
      <td>10.2</td>
      <td>2552508.0</td>
      <td>234581.0</td>
      <td>10.1</td>
      <td>2555817.0</td>
      <td>232003.0</td>
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

    WARNING:fetcha.ssb:Query exceeds SSB limit of 300k rows per transaction. Current query tries to fetch 607104 rows. User a filter
    


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
      '30',
      '01',
      '02',
      '03',
      '34',
      '04',
      '05',
      '06',
      '38',
      '07',
      '08',
      '42',
      '09',
      '10',
      '11',
      '46',
      '12',
      '14',
      '15',
      '50',
      '16',
      '17',
      '18',
      '54',
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
      'Viken',
      'Østfold (-2019)',
      'Akershus (-2019)',
      'Oslo',
      'Innlandet',
      'Hedmark (-2019)',
      'Oppland (-2019)',
      'Buskerud (-2019)',
      'Vestfold og Telemark',
      'Vestfold (-2019)',
      'Telemark (-2019)',
      'Agder',
      'Aust-Agder (-2019)',
      'Vest-Agder (-2019)',
      'Rogaland',
      'Vestland',
      'Hordaland (-2019)',
      'Sogn og Fjordane (-2019)',
      'Møre og Romsdal',
      'Trøndelag - Trööndelage',
      'Sør-Trøndelag (-2017)',
      'Nord-Trøndelag (-2017)',
      'Nordland',
      'Troms og Finnmark - Romsa ja Finnmárku',
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
      <th>Males</th>
      <th>40-59 years</th>
      <th>Influenza and pneumonia</th>
      <th>Number of day cases</th>
      <th>2019</th>
      <td>76.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Females</th>
      <th>20-39 years</th>
      <th>Injuries of upper extremities</th>
      <th>Patients with day cases</th>
      <th>2019</th>
      <td>613.0</td>
    </tr>
    <tr>
      <th>60-69 years</th>
      <th>CONGENITAL MALFORMATIONS</th>
      <th>Number of bed-days</th>
      <th>2019</th>
      <td>290.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Both sexes</th>
      <th rowspan="2" valign="top">20-39 years</th>
      <th>Cardiac dysrhythmias</th>
      <th>Patients with day cases</th>
      <th>2019</th>
      <td>276.0</td>
    </tr>
    <tr>
      <th>PREGNANCY, CHILDBIRTH AND THE PUERPERIUM</th>
      <th>Number of out-patient consultations</th>
      <th>2019</th>
      <td>109637.0</td>
    </tr>
    <tr>
      <th>Females</th>
      <th>60-69 years</th>
      <th>Glaucoma</th>
      <th>Number of day cases</th>
      <th>2019</th>
      <td>253.0</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Both sexes</th>
      <th>Years, total</th>
      <th>Other maternal disorders predominantly related to pregnancy</th>
      <th>In-patients</th>
      <th>2019</th>
      <td>1478.0</td>
    </tr>
    <tr>
      <th>60-69 years</th>
      <th>Diabetes mellitus</th>
      <th>In-patients</th>
      <th>2019</th>
      <td>488.0</td>
    </tr>
    <tr>
      <th>70-79 years</th>
      <th>Other diseases of oesophagus, stomach and duodenum</th>
      <th>Number of bed-days</th>
      <th>2019</th>
      <td>3265.0</td>
    </tr>
    <tr>
      <th>0-9 years</th>
      <th>Malignant neoplasms of female genital organs</th>
      <th>Out-patients</th>
      <th>2019</th>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
