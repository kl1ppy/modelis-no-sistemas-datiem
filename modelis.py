"""Apmāca Random Forest un salīdzina to ar biežākās klases bāzes līniju."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.dummy import DummyClassifier

CSV = Path("tirs.csv")


def main():
    if not CSV.exists():
        raise FileNotFoundError("Nav tirs.csv. Vispirms palaid: python tirisana.py")
    df = pd.read_csv(CSV)
    y = df["class"].astype(str)
    X = df.drop(columns=["class"])
    # Teksta/ne-skaitliskas kolonnas pārvēršam kategorijās; skaitliskās paliek skaitliskas.
    categorical = X.select_dtypes(include=["object", "category"]).columns.tolist()
    numeric = X.select_dtypes(exclude=["object", "category"]).columns.tolist()
    preprocess = ColumnTransformer([
        ("num", Pipeline([("impute", SimpleImputer(strategy="median"))]), numeric),
        ("cat", Pipeline([("impute", SimpleImputer(strategy="most_frequent"))]), categorical),
    ])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = Pipeline([
        ("prep", preprocess),
        ("classifier", RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced", n_jobs=-1)),
    ])
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    model_acc = accuracy_score(y_test, prediction)
    baseline = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
    base_acc = accuracy_score(y_test, baseline.predict(X_test))
    print("Accuracy (modelis) | Accuracy (bāzes līnija)")
    print(f"{model_acc:.4f}            | {base_acc:.4f}")
    print("\nKlases pārskats:\n", classification_report(y_test, prediction, zero_division=0))
    print("Confusion matrix (rindas=īstā klase, kolonnas=prognoze):\n", confusion_matrix(y_test, prediction))
    print("Piezīme: 'pos' klase ir reta; accuracy viena pati var slēpt kļūdas. Apskati arī recall.")

if __name__ == "__main__":
    main()
