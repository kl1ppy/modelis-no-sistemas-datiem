# Modelis no sistēmas datiem — AI4I 2020


Šis projekts izmanto AI4I 2020 Predictive Maintenance Dataset, lai ar mašīnmācīšanos prognozētu, vai iekārtai var būt atteice (`Machine failure`). Dataset ir sintētisks, 10 000 ierakstu, un atspoguļo industriālās apkopes sensoru datus.

## Mapju struktūra

- `dati/ai4i2020.csv` — oriģinālais CSV (lejupielādē no UCI, nepārveido).
- `dati/AVOTS.txt` — avota saite, licence un lejupielādes datums.
- `tirisana.py` — datu tīrīšana un saglabāšana `tirs.csv`.
- `modelis.py` — apmācība, testēšana, accuracy salīdzinājums ar bāzes līniju.
- `rezultati.md` — interpretācija un secinājumi.

## Uzstādīšana

Python 3.10+ un bibliotēkas:

```bash
pip install pandas scikit-learn
```

## Kā palaist

1. Lejupielādē UCI CSV failu `ai4i2020.csv` un ievieto to mapē `dati/`.
2. `dati/AVOTS.txt` ieraksti faktisko lejupielādes datumu.
3. Terminālī projekta mapē izpildi:

```bash
python tirisana.py
python modelis.py
```

## Ko dara skripti

`tirisana.py` sakārto kolonnu nosaukumus, izņem dublikātus un identifikatorus, apstrādā trūkstošās vērtības un izveido `tirs.csv`.

`modelis.py` sadala datus 75% apmācībai un 25% pārbaudei, apmāca Random Forest modeli, un salīdzina tā rezultātu ar vienkāršu bāzes līniju, kas vienmēr prognozē biežāko klasi.
