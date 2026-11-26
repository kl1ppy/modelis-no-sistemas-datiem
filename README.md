# Modelis no sistēmas datiem — Scania APS atteices

Šis projekts izmanto Scania kravas automašīnu gaisa spiediena sistēmas (APS) datus, lai klasificētu, vai ieraksts saistīts ar APS komponentes atteici (`pos`) vai ne (`neg`). Datu kopā ir anonimizēti sensora/operacionālie rādītāji.


## Datu iegūšana
1. Atver UCI datu kopas lapu: https://archive.ics.uci.edu/dataset/421/aps+failure+at+scania+trucks
2. Lejupielādē zip arhīvu un izpako to.
3. Ievieto `aps_failure_training_set.csv` mapē `dati/`.
4. `dati/AVOTS.txt` ieraksti faktisko lejupielādes datumu.

Datu fails ir liels, tāpēc tas šajā sagatavotajā mapē nav iekļauts. Pievieno oriģinālo CSV failu `dati/` mapē un GitHub repo. **Neizmaini oriģinālu.**

## Uzstādīšana
Python 3.10+ ieteicams.

```bash
pip install pandas scikit-learn
```

## Darbināšana

```bash
python tirisana.py
python modelis.py
```

Skripts `t irisana.py` (nosaukums bez atstarpēm: `t irisana.py`) nolasa oriģinālu, atzīmē `na` kā trūkstošas vērtības, noņem dublikātus, izmet pilnīgi tukšas kolonnas un skaitliskajās pazīmēs aizpilda trūkstošos datus ar mediānu. Tas izveido `tirs.csv`.

`modelis.py` sadala datus 75% apmācībai un 25% testam, apmāca Random Forest un salīdzina tā accuracy ar DummyClassifier biežākās klases bāzes līniju. Izvada arī precision/recall/F1 un confusion matrix.

## Failu struktūra

```text
.
├── dati/
│   ├── aps_failure_training_set.csv  # oriģinālais, lejupielādētais fails
│   └── AVOTS.txt
├── tirisana.py
├── modelis.py
├── tirs.csv                         # izveidojas pēc tīrīšanas
├── rezultati.md
└── README.md
```

## Svarīgi ierobežojumi
Šie dati ir vēsturisku kravas automašīnu APS mērījumu piemēri, nevis tiešsaistes diagnostika. Modelis var kļūdīties; tas nedrīkst automātiski izlemt, vai transportlīdzeklis ir drošs ekspluatācijai. Prognozi var izmantot tikai kā papildu signālu, lai tehniķis pārbaudītu transportlīdzekli.
