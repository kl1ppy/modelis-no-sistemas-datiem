"""Notīra Scania APS datus, saglabājot oriģinālo failu."""
from pathlib import Path
import pandas as pd

DATA_DIR = Path("dati")
INPUT = DATA_DIR / "aps_failure_training_set.csv"
OUTPUT = Path("tirs.csv")


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f"Nav atrasts {INPUT}. Vispirms lejupielādē datu kopu; instrukcija README.md.")
    # UCI failam ir 20 paskaidrojošas rindas pirms tabulas; 'na' ir trūkstošo vērtību marķieris.
    df = pd.read_csv(INPUT, skiprows=20, na_values=["na"])
    before = len(df)
    # Dublikātus noņemam, lai vienādi novērojumi nepārsvarotu mācīšanās laikā.
    df = df.drop_duplicates()
    # Kolonnas, kurās pilnīgi visas vērtības trūkst, nevar sniegt informāciju modelim.
    df = df.dropna(axis=1, how="all")
    # Neizmantoto trūkstošo vērtību aizpildām ar kolonnas mediānu; mērķa 'class' kolonna netiek aizpildīta.
    for col in df.columns:
        if col != "class" and df[col].isna().any() and pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
    # Ja mērķa klase nav norādīta, šo rindu nevar izmantot uzraudzītai apmācībai.
    df = df.dropna(subset=["class"])
    df.to_csv(OUTPUT, index=False)
    print(f"Rindu skaits sākumā: {before}")
    print(f"Rindu skaits pēc tīrīšanas: {len(df)}")
    print(f"Saglabāts: {OUTPUT}")

if __name__ == "__main__":
    main()
