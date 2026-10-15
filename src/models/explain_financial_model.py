from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import shap
from sklearn.ensemble import RandomForestRegressor

ROOT = Path(__file__).resolve().parents[2]
FILE = ROOT / "data" / "processed" / "financial_features_clean.csv"

df = pd.read_csv(FILE)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["date", "commodity"]).reset_index(drop=True)

target = "target_next_day_return"
features = [
    col for col in df.columns
    if col not in ["date", "commodity", target]
]

split_date = df["date"].quantile(0.80)
train = df[df["date"] < split_date]

X_train = train[features]
y_train = train[target]

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

sample = X_train.sample(
    n=min(200, len(X_train)),
    random_state=42
)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(sample)

plt.figure()
shap.summary_plot(shap_values, sample, show=False)
output = ROOT / "data" / "processed" / "shap_summary.png"
plt.savefig(output, dpi=300, bbox_inches="tight")
plt.close()

print("SHAP summary plot saved to:", output)