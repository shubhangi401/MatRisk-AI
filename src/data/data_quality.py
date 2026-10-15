from pathlib import Path
import pandas as pd

# Project ke main folder ka path
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Original CSV files ka folder
DATA_DIR = PROJECT_ROOT / "data" / "raw" / "provided"

# Quality report save karne ka folder
REPORT_DIR = PROJECT_ROOT / "data" / "processed"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

def check_csv_files():
    csv_files = sorted(DATA_DIR.glob("*.csv"))

    if not csv_files:
        print(f"No CSV files found in: {DATA_DIR}")
        return

    reports = []

    for file_path in csv_files:
        print(f"\nChecking: {file_path.name}")

        try:
            df = pd.read_csv(file_path)

            report = {
                "file_name": file_path.name,
                "total_rows": len(df),
                "total_columns": len(df.columns),
                "missing_cells": int(df.isna().sum().sum()),
                "duplicate_rows": int(df.duplicated().sum()),
                "duplicate_columns": int(df.columns.duplicated().sum()),
                "memory_MB": round(
                    df.memory_usage(deep=True).sum() / (1024 ** 2), 2
                ),
                "status": "Success",
            }

            reports.append(report)

            print(f"Rows: {report['total_rows']}")
            print(f"Columns: {report['total_columns']}")
            print(f"Missing cells: {report['missing_cells']}")
            print(f"Duplicate rows: {report['duplicate_rows']}")

        except Exception as error:
            print(f"Could not check {file_path.name}: {error}")

            reports.append({
                "file_name": file_path.name,
                "total_rows": None,
                "total_columns": None,
                "missing_cells": None,
                "duplicate_rows": None,
                "duplicate_columns": None,
                "memory_MB": None,
                "status": f"Failed: {error}",
            })

    if reports:
        report_df = pd.DataFrame(reports)
        output_path = REPORT_DIR / "data_quality_report.csv"
        report_df.to_csv(output_path, index=False)

        print("\n--- DATA QUALITY CHECK COMPLETE ---")
        print(report_df.to_string(index=False))
        print(f"\nReport saved at: {output_path}")


if __name__ == "__main__":
    check_csv_files()