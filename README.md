# hitemp

Automatically download &amp; parse [HITEMP](https://hitran.org/hitemp/) line 
lists to a Pandas DataFrame

### Install:

```
!pip install hitemp
```

### Use:

```python
import hitemp
df = hitemp.fetch("OH")
```

Then use Pandas to explore the database:

```
>>> print(df.columns)
Index(['id', 'iso', 'wav', 'int', 'A', 'airbrd', 'selbrd', 'El', 'Tdpair',
       'Pshft', 'globu', 'globl', 'locu', 'locl', 'ierr', 'iref', 'lmix', 'gp',
       'gpp'],
      dtype='object')
>>> print(df[(df.wav >= 3500) & (df.wav <= 4500)]
       id  iso          wav           int  ...          iref  lmix     gp    gpp
14828  13    1  3500.146273  1.640000e-81  ...   6 5 2 1 1 0         20.0   24.0
14829  13    1  3500.297514  1.140000e-79  ...   6 5 2 1 1 0          8.0    4.0
14830  13    1  3500.355242  1.140000e-79  ...   6 5 2 1 1 0          8.0    4.0
14831  13    1  3501.004093  1.244000e-39  ...   6 5 2 1 1 0         44.0   40.0
14832  13    1  3501.122970  8.624000e-82  ...   6 5 2 1 1 0         36.0   32.0
   ..  ...          ...           ...  ...           ...   ...    ...    ...
17214  13    1  4496.516599  1.104000e-72  ...   6 5 2 1 1 0        100.0  100.0
17215  13    1  4497.231675  4.559000e-78  ...   6 5 2 1 1 0        144.0  144.0
17216  13    1  4497.606660  2.283000e-83  ...   6 5 2 1 1 0        176.0  176.0
17217  13    1  4497.990947  8.971000e-71  ...   6 5 2 1 1 0         72.0   72.0
17218  13    1  4499.552570  3.759000e-64  ...   6 5 2 1 1 0        132.0  128.0

[2391 rows x 19 columns]
```

Get only specific isotope, or wavenumber range (the whole database is still downloaded 
on the first call):

```
df = hitemp.fetch("OH", isotope='1,2,3', load_wavenum_min=3500, load_wavenum_max=4500)
```

### Implementation:

Uses the [🌱 RADIS](http://radis.github.io/) 
[fetch_hitemp()](https://radis.readthedocs.io/en/latest/source/radis.io.hitemp.html) 
function : 
Stream HITEMP file from the [HITRAN website](https://hitran.org/hitemp/) 
Unzip and build a local HDF5 file directly, in ``local_databases=~/.radisdb`` by default.
Returns a Pandas DataFrame containing all the lines.