import pandas as pd
from pathlib import Path
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

ROOT = Path(__file__).resolve().parents[2]

files = {
    "Ridge Regression": ROOT / "models" / "ridge_predictions.csv",
    "Random Forest": ROOT / "models" / "financial_predictions.csv",
}

results = []

for model_name, file_path in files.items():
    df = pd.read_csv(file_path)

    mae = mean_absolute_error(
        df["actual_return"], df["predicted_return"]
    )
    rmse = np.sqrt(mean_squared_error(
        df["actual_return"], df["predicted_return"]
    ))
    r2 = r2_score(
        df["actual_return"], df["predicted_return"]
    )

    results.append({
        "Model": model_name,
        "MAE": mae,
        "RMSE": rmse,
        "R2_Score": r2,
    })

report = pd.DataFrame(results)
output_path = ROOT / "data" / "processed" / "final_model_comparison.csv"
report.to_csv(output_path, index=False)

print("\nFinal Model Comparison:")
print(report.round(6).to_string(index=False))
print("\nReport saved to:", output_path)