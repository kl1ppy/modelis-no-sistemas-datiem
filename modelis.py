# Šis skripts apmāca modeli prognozēt, vai iekārta piedzīvos atteici.
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, balanced_accuracy_score, recall_score, confusion_matrix

# Ielādējam iepriekš sagatavotos datus.
folder = Path(__file__).parent
data_path = folder / "tirs.csv"
if not data_path.exists():
    raise FileNotFoundError("Vispirms palaid tirisana.py, lai izveidotu tirs.csv.")
df = pd.read_csv(data_path)

# Prognozējam kopējo atteici; citi atteices veidi netiek izmantoti, lai nepieļautu mērķa noplūdi.
target = "Machine failure"
if target not in df.columns:
    raise ValueError(f"Datu failā nav mērķa kolonnas '{target}'. Pārbaudi CSV.")
leak_columns = [c for c in ["TWF", "HDF", "PWF", "OSF", "RNF"] if c in df.columns]
X = df.drop(columns=[target] + leak_columns)
y = df[target]

# Sadalām datus treniņa un testa daļā, saglabājot līdzīgu atteiču proporciju abās daļās.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Teksta kategorijas (Type) pārveido skaitļos, bet skaitliskos rādītājus atstāj nemainīgus.
cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
num_cols = X.select_dtypes(include=["number"]).columns.tolist()
preprocess = ColumnTransformer(
    transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
                 ("num", "passthrough", num_cols)]
)

# Random Forest apvieno vairākus lēmumu kokus, lai noteiktu atteices risku.
model = Pipeline(steps=[
    ("prep", preprocess),
    ("classifier", RandomForestClassifier(n_estimators=150, class_weight="balanced", random_state=42))
])
model.fit(X_train, y_train)

# Aprēķinām modeļa rezultātus uz testa datiem, kurus modelis treniņā nav redzējis.
predictions = model.predict(X_test)
model_accuracy = accuracy_score(y_test, predictions)
model_balanced = balanced_accuracy_score(y_test, predictions)
model_recall = recall_score(y_test, predictions, zero_division=0)

# Bāzes līnija vienmēr prognozē biežāko klasi; tā palīdz saprast, vai modelis ir labāks par vienkāršu minēšanu.
majority = y_train.mode()[0]
baseline_predictions = [majority] * len(y_test)
baseline_accuracy = accuracy_score(y_test, baseline_predictions)
baseline_balanced = balanced_accuracy_score(y_test, baseline_predictions)

print("\nREZULTĀTI (testa dati)")
print(f"Modeļa accuracy: {model_accuracy:.3f} | Bāzes accuracy: {baseline_accuracy:.3f}")
print(f"Modeļa balanced accuracy: {model_balanced:.3f} | Bāzes balanced accuracy: {baseline_balanced:.3f}")
print(f"Modeļa recall (atteices klase): {model_recall:.3f}")
print("Konfūzijas matrica [ [TN, FP], [FN, TP] ]:")
print(confusion_matrix(y_test, predictions, labels=[0, 1]))
print(f"Bāzes līnija prognozē klasi: {majority}")
