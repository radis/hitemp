# hitemp

Automatically download &amp; parse the latest [HITEMP](https://hitran.org/hitemp/) line 
lists to a Pandas DataFrame: 
- A local cache is created for fast retrieval. 
- Available molecules : ``CH4, CO, N2O, NO, NO2, OH``.
- Not available yet: ``CO2, H2O``.

### Install:

```bash
pip install hitemp
```

### Use:

```python
import hitemp
df = hitemp.fetch("OH")
```

Then use Pandas to explore the database:

```python
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

```python
df = hitemp.fetch("OH", isotope='1,2,3', load_wavenum_min=3500, load_wavenum_max=4500)
```

### References

Cite the HITEMP database (see the [HITRAN website](https://hitran.org/hitemp/) for up-to-date references !)

> [1] L. S. Rothman, I. E. Gordon, R. J. Barber, H. Dothe, R. R. Gamache, A. Goldman, V. Perevalov, S. A. Tashkun, J. Tennyson, "HITEMP, the high-temperature molecular spectroscopic database", J. Quant. Spectrosc. Radiat. Transfer 111, 2139-2150 (2010).

> [2] L. S. Rothman, R. B. Wattson, R. R. Gamache, J. Schroeder, A. McCann, "HITRAN, HAWKS and HITEMP: High-Temperature Molecular Database", Proc. SPIE, Atmospheric Propogation and Remote Sensing IV 2471, 105-111 (1995).

> [3] R. J. Hargreaves, I. E. Gordon, L. S. Rothman, S. A. Tashkun, V. I. Perevalov, S. N. Yurchenko, J. Tennyson, H. S. P. Müller, "Spectroscopic line parameters of NO, NO2, and N2O for the HITEMP database", J. Quant. Spectrosc. Radiat. Transfer 232, 35-53 (2019).

> [4] R. J. Hargreaves, I. E. Gordon, M. Rey, A. V. Nikitin, V. G. Tyuterev, R. V. Kochanov, L. S. Rothman, "An accurate, extensive, and practical line list of methane for the HITEMP database", Astrophys. J. Supp. Ser. 247, 55 (2020).

> [5] G. Li, I. E. Gordon, L. S. Rothman, Y. Tan, S.-M. Hu, S. Kassi, A. Campargue, E. S. Medvedev, "Rovibrational line lists for nine isotopologues of the CO molecule in the X1Σ+ ground electronic state", Astrophys. J. Supp. Ser. 216, 15 (2015).


### Implementation:

Uses the [fetch_hitemp()](https://radis.readthedocs.io/en/latest/source/radis.io.hitemp.html) 
function from the [🌱 RADIS](http://radis.github.io/) line-by-line code: 
- stream HITEMP file from the [HITRAN website](https://hitran.org/hitemp/) 
- unzip and build a local HDF5 file directly, in ``local_databases=~/.radisdb`` by default.
- returns a Pandas DataFrame containing all the lines.
