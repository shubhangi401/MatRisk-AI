from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "merged_financial_data.csv"
)

OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def create_financial_features():
    df = pd.read_csv(INPUT_FILE)
    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values(["commodity", "date"]).copy()

    # Target: next trading observation's daily return
    df["target_next_day_return"] = (
        df.groupby("commodity")["daily_return"].shift(-1)
    )

    # Keep existing indicators based on historical data
    feature_columns = [
        "close",
        "volume",
        "daily_return",
        "return_5d",
        "return_21d",
        "volatility_5d_ann",
        "volatility_21d_ann",
        "volatility_63d_ann",
        "sma_21",
        "sma_63",
        "bollinger_z",
        "rsi_14",
        "macd",
        "macd_signal",
        "momentum_10d",
        "momentum_21d",
        "term_spread",
        "mqi",
        "supply_disruption_prob",
        "substitution_elasticity",
        "green_premium_per_kg",
        "carbon_intensity_virgin",
        "carbon_intensity_recycled",
        "herfindahl_index",
        "mqi_5d_trend",
        "mqi_21d_trend",
        "mqi_63d_trend",
    ]

    # Check that all requested features exist
    missing_columns = [
        col for col in feature_columns if col not in df.columns
    ]

    if missing_columns:
        print("Missing feature columns:", missing_columns)
        return

    # Save feature dataset without deleting missing values
    output_columns = [
        "date",
        "commodity",
        *feature_columns,
        "target_next_day_return",
    ]

    output_file = OUTPUT_DIR / "financial_features.csv"
    df[output_columns].to_csv(output_file, index=False)

    print("Financial feature engineering completed!")
    print("Total rows:", len(df))
    print("Feature columns:", len(feature_columns))
    print(
        "Rows with missing target:",
        int(df["target_next_day_return"].isna().sum()),
    )
    print("Saved to:", output_file)


if __name__ == "__main__":
    create_financial_features()