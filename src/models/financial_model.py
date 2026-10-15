from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "financial_features_clean.csv"
)

OUTPUT_DIR = PROJECT_ROOT / "models"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def train_financial_model():
    df = pd.read_csv(DATA_FILE)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["date", "commodity"]).reset_index(drop=True)

    target = "target_next_day_return"

    excluded = ["date", "commodity", target]
    features = [col for col in df.columns if col not in excluded]

    # Time-based split: older observations for training,
    # newer observations for testing.
    split_date = df["date"].quantile(0.80)

    train = df[df["date"] < split_date].copy()
    test = df[df["date"] >= split_date].copy()

    X_train = train[features]
    y_train = train[target]
    X_test = test[features]
    y_test = test[target]

    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    importance = pd.Series(
        model.feature_importances_,
        index=features
    ).sort_values(ascending=False)

    print("\nTop 10 Important Features:")
    print(importance.head(10).to_string())

    predictions = model.predict(X_test)
    results = test[["date", "commodity"]].copy()
    results["actual_return"] = y_test.values
    results["predicted_return"] = predictions
    results["absolute_error"] = (
        results["actual_return"] - results["predicted_return"]
    ).abs()

    results_file = OUTPUT_DIR / "financial_predictions.csv"
    results.to_csv(results_file, index=False)

    print("Predictions saved to:", results_file)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)
    print("Financial model training completed!")
    print("Training rows:", len(train))
    print("Testing rows:", len(test))
    print("Split date:", split_date.date())
    print(f"MAE: {mae:.6f}")
    print(f"RMSE: {rmse:.6f}")
    print(f"R2 Score: {r2:.4f}")


if __name__ == "__main__":
    train_financial_model()