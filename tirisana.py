# Šis skripts sagatavo AI4I datus modelim, saglabājot oriģinālo CSV nemainītu.
import pandas as pd
from pathlib import Path

# Norādām, kur atrodas oriģinālie dati un kur saglabāt tīro failu.
folder = Path(__file__).parent
source = folder / "dati" / "ai4i2020.csv"
output = folder / "tirs.csv"

# Nolasa CSV failu; ja fails nav vietā, parāda saprotamu kļūdu.
if not source.exists():
    raise FileNotFoundError("Ieliec ai4i2020.csv mapē dati/ un palaid skriptu vēlreiz.")
df = pd.read_csv(source)
print(f"Rindu skaits sākumā: {len(df)}")

# Sakārto kolonnu nosaukumus, lai tos vieglāk izmantotu Python kodā.
df.columns = [c.strip() for c in df.columns]

# Noņem pilnīgi vienādas rindas, jo tās nevajadzētu skaitīt kā atsevišķus novērojumus.
df = df.drop_duplicates()

# UID un Product ID ir ierakstu identifikatori, nevis iekārtas darbības rādītāji, tāpēc tos neizmantojam prognozei.
for col in ["UDI", "UID", "Product ID"]:
    if col in df.columns:
        df = df.drop(columns=col)

# Ja kādā kolonnā ir tukšas vērtības, skaitliskās aizpildām ar mediānu, bet tekstuālās ar biežāko vērtību.
for col in df.columns:
    if df[col].isna().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

# Saglabā sakārtotos datus atsevišķā failā, oriģinālu nepārrakstot.
df.to_csv(output, index=False)
print(f"Rindu skaits pēc tīrīšanas: {len(df)}")
print(f"Tīrie dati saglabāti: {output.name}")
