from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "provided"
    / "DS1_material_properties_5500.csv"
)

OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_material_data():
    if not DATA_FILE.exists():
        print("Error: Material dataset file not found.")
        print(DATA_FILE)
        return

    df = pd.read_csv(DATA_FILE)

    print("Material data loaded successfully!")
    print("Total records:", len(df))
    print("Total columns:", len(df.columns))
    print("\nColumn names:")
    print(df.columns.tolist())

    output_file = OUTPUT_DIR / "material_data_summary.csv"

    summary = pd.DataFrame({
        "column_name": df.columns,
        "data_type": [str(dtype) for dtype in df.dtypes],
        "missing_values": df.isna().sum().values
    })

    summary.to_csv(output_file, index=False)

    print("\nSummary saved to:", output_file)


if __name__ == "__main__":
    load_material_data()