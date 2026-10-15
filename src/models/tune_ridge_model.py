from pathlib import Path

import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path(__file__).resolve().parents[2]
FILE = ROOT / "data" / "processed" / "financial_features_clean.csv"

df = pd.read_csv(FILE)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["date", "commodity"]).reset_index(drop=True)

target = "target_next_day_return"
features = [
    col for col in df.columns
    if col not in ["date", "commodity", target]
]

split_date = df["date"].quantile(0.80)
train = df[df["date"] < split_date]
test = df[df["date"] >= split_date]

X_train, y_train = train[features], train[target]
X_test, y_test = test[features], test[target]

results = []

for alpha in [0.01, 0.1, 1.0, 10.0, 100.0]:
    model = make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        Ridge(alpha=alpha)
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    results.append({
        "alpha": alpha,
        "MAE": mean_absolute_error(y_test, predictions),
        "RMSE": mean_squared_error(y_test, predictions) ** 0.5,
        "R2_Score": r2_score(y_test, predictions)
    })

report = pd.DataFrame(results)
output = ROOT / "data" / "processed" / "ridge_tuning_results.csv"
report.to_csv(output, index=False)

print("\nRidge Regression Tuning Results:")
print(report.round(6).to_string(index=False))
print("\nReport saved to:", output)