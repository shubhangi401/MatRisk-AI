from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "data" / "raw" / "provided" / "DS6_historical_failures_2000.csv"
OUTPUT_DIR = ROOT / "data" / "processed"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_FILE)

    # Basic validation
    required = [
        "event_id",
        "structure_type",
        "material",
        "severity",
        "failure_mode",
        "repair_cost_USD",
        "loss_ratio",
    ]

    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Clean key numeric fields
    for col in ["repair_cost_USD", "loss_ratio", "age_at_event_years"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Risk summary by severity
    severity_summary = (
        df.groupby("severity", dropna=False)
        .agg(
            event_count=("event_id", "count"),
            average_repair_cost_USD=("repair_cost_USD", "mean"),
            average_loss_ratio=("loss_ratio", "mean"),
        )
        .reset_index()
    )

    severity_summary.to_csv(
        OUTPUT_DIR / "infrastructure_risk_by_severity.csv",
        index=False,
    )

    # Risk summary by structure type
    structure_summary = (
        df.groupby("structure_type", dropna=False)
        .agg(
            event_count=("event_id", "count"),
            average_repair_cost_USD=("repair_cost_USD", "mean"),
            average_loss_ratio=("loss_ratio", "mean"),
        )
        .reset_index()
        .sort_values("event_count", ascending=False)
    )

    structure_summary.to_csv(
        OUTPUT_DIR / "infrastructure_risk_by_structure.csv",
        index=False,
    )

    # Risk summary by failure mode
    failure_summary = (
        df.groupby("failure_mode", dropna=False)
        .agg(
            event_count=("event_id", "count"),
            average_repair_cost_USD=("repair_cost_USD", "mean"),
            average_loss_ratio=("loss_ratio", "mean"),
        )
        .reset_index()
        .sort_values("event_count", ascending=False)
    )

    failure_summary.to_csv(
        OUTPUT_DIR / "infrastructure_risk_by_failure_mode.csv",
        index=False,
    )

    print(f"Rows analyzed: {len(df):,}")
    print("Infrastructure risk analysis completed.")
    print("Reports saved in:", OUTPUT_DIR)


if __name__ == "__main__":
    main()