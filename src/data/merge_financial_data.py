from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "raw" / "provided"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DS2_FILE = DATA_DIR / "DS2_commodity_prices_10yr.csv"
DS4_FILE = DATA_DIR / "DS4_crossdomain_features_daily.csv"


def merge_financial_data():
    ds2 = pd.read_csv(DS2_FILE)
    ds4 = pd.read_csv(DS4_FILE)

    ds2["date"] = pd.to_datetime(ds2["date"])
    ds4["date"] = pd.to_datetime(ds4["date"])

    merged = pd.merge(
        ds2,
        ds4,
        on=["date", "commodity"],
        how="left",
        validate="one_to_one",
        suffixes=("_ds2", "_ds4")
    )

    output_file = OUTPUT_DIR / "merged_financial_data.csv"
    merged.to_csv(output_file, index=False)

    print("Merge completed successfully!")
    print("DS2 rows:", len(ds2))
    print("DS4 rows:", len(ds4))
    print("Merged rows:", len(merged))
    print("Merged columns:", len(merged.columns))
    print("Unmatched DS2 rows:", int(merged["mqi"].isna().sum()))
    print("Saved to:", output_file)


if __name__ == "__main__":
    merge_financial_data()