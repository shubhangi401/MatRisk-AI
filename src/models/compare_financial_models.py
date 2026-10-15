from pathlib import Path

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
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

models = {
    "Ridge Regression": make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        Ridge(alpha=1.0)
    ),
    "Random Forest": make_pipeline(
        SimpleImputer(strategy="median"),
        RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
    )
}

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    results = test[["date", "commodity"]].copy()
    results["actual_return"] = y_test.values
    results["predicted_return"] = predictions
    results["absolute_error"] = (
        results["actual_return"] - results["predicted_return"]
    ).abs()

    if name == "Ridge Regression":
        output_file = ROOT / "models" / "ridge_predictions.csv"
    else:
        output_file = ROOT / "models" / "financial_predictions.csv"

    results.to_csv(output_file, index=False)
    print(f"\n{name} predictions saved to: {output_file}")

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    print(f"MAE: {mae:.6f}")
    print(f"RMSE: {rmse:.6f}")
    print(f"R2 Score: {r2:.4f}")