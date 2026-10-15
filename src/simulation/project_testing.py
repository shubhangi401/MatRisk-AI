from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "data" / "processed"
MODELS = ROOT / "models"

def main():
    checks = [
        ("Financial features", PROCESSED / "financial_features_clean.csv"),
        ("Model comparison", PROCESSED / "final_model_comparison.csv"),
        ("Risk by severity", PROCESSED / "infrastructure_risk_by_severity.csv"),
        ("Risk by structure", PROCESSED / "infrastructure_risk_by_structure.csv"),
        ("Risk by failure mode", PROCESSED / "infrastructure_risk_by_failure_mode.csv"),
        ("SHAP visualization", PROCESSED / "shap_summary.png"),
        ("Ridge predictions", MODELS / "ridge_predictions.csv"),
        ("Random Forest predictions", MODELS / "financial_predictions.csv"),
    ]

    results = []

    for name, path in checks:
        exists = path.exists()
        rows = None
        columns = None

        if exists and path.suffix == ".csv":
            try:
                df = pd.read_csv(path)
                rows = len(df)
                columns = len(df.columns)
                status = "PASS" if rows > 0 else "CHECK: EMPTY"
            except Exception as exc:
                status = f"ERROR: {exc}"
        else:
            status = "PASS" if exists else "MISSING"

        results.append({
            "component": name,
            "status": status,
            "rows": rows,
            "columns": columns,
            "path": str(path)
        })

    report = pd.DataFrame(results)
    output = PROCESSED / "project_testing_report.csv"
    report.to_csv(output, index=False)

    print(report[["component", "status", "rows", "columns"]].to_string(index=False))
    print(f"\nTesting report saved to: {output}")

if __name__ == "__main__":
    main()