from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
FILE = ROOT / "data" / "processed" / "ridge_tuning_results.csv"

df = pd.read_csv(FILE)

plt.figure(figsize=(8, 5))
plt.plot(df["alpha"], df["MAE"], marker="o")
plt.xscale("log")
plt.xlabel("Ridge Alpha")
plt.ylabel("Mean Absolute Error (MAE)")
plt.title("Ridge Regression: Alpha Tuning")
plt.grid(True)

output = ROOT / "data" / "processed" / "ridge_tuning_mae.png"
plt.savefig(output, dpi=300, bbox_inches="tight")
plt.show()

print("Graph saved to:", output)