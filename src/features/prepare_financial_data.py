from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "financial_features.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "financial_features_clean.csv"
)


def prepare_financial_data():
    df = pd.read_csv(INPUT_FILE)

    # Remove rows where the prediction target is missing
    df = df.dropna(subset=["target_next_day_return"])

    # Keep only rows with complete feature values for now
    feature_columns = [
        col for col in df.columns
        if col not in [
            "date", "commodity", "target_next_day_return"
        ]
    ]

    df = df.dropna(subset=feature_columns)

    df.to_csv(OUTPUT_FILE, index=False)

    print("Financial data preparation completed!")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Missing values:", int(df.isna().sum().sum()))
    print("Saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    prepare_financial_data()