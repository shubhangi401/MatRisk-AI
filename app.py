from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "processed"

st.set_page_config(
    page_title="MatRisk-AI Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("MatRisk-AI: Financial Risk Dashboard")
st.write("Commodity return prediction and model evaluation")

comparison_file = DATA / "final_model_comparison.csv"
features_file = DATA / "financial_features_clean.csv"
shap_file = DATA / "shap_summary.png"

if comparison_file.exists():
    comparison = pd.read_csv(comparison_file)
    st.subheader("Model Performance")
    st.dataframe(comparison, use_container_width=True)

    st.subheader("MAE Comparison")
    st.bar_chart(comparison.set_index("Model")["MAE"])
else:
    st.warning("Model comparison report not found.")

if features_file.exists():
    df = pd.read_csv(features_file)

    st.subheader("Financial Dataset Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", f"{len(df):,}")
    col2.metric("Commodities", df["commodity"].nunique())
    col3.metric("Features", len(df.columns) - 3)

    st.subheader("Commodity Data")
    commodities = sorted(df["commodity"].dropna().unique())
    selected = st.selectbox("Select commodity", commodities)
    filtered = df[df["commodity"] == selected]

    st.line_chart(
        filtered.set_index("date")["daily_return"]
    )
    st.dataframe(filtered.tail(10), use_container_width=True)

if shap_file.exists():
    st.subheader("Model Explainability (SHAP)")
    st.image(str(shap_file), use_container_width=True)
    # Model Predictions
st.subheader("Model Predictions")

predictions_file = ROOT / "models" / "financial_predictions.csv"

if predictions_file.exists():
    predictions = pd.read_csv(predictions_file)

    st.write("Latest model prediction records:")
    st.dataframe(predictions.tail(10), use_container_width=True)

    st.download_button(
        label="Download Predictions CSV",
        data=predictions.to_csv(index=False),
        file_name="financial_predictions.csv",
        mime="text/csv"
    )
else:
    st.warning("Predictions file not found.")
    # Compare predictions from both models
st.subheader("Ridge vs Random Forest Predictions")

ridge_file = ROOT / "models" / "ridge_predictions.csv"
rf_file = ROOT / "models" / "financial_predictions.csv"

if ridge_file.exists() and rf_file.exists():
    ridge_df = pd.read_csv(ridge_file)
    rf_df = pd.read_csv(rf_file)

    col1, col2 = st.columns(2)

    with col1:
        st.write("Ridge Regression")
        st.dataframe(ridge_df.tail(10), use_container_width=True)

    with col2:
        st.write("Random Forest")
        st.dataframe(rf_df.tail(10), use_container_width=True)
else:
    st.warning("One or both prediction files are missing.")
    # Prediction Error Comparison Chart
st.subheader("Prediction Error Comparison")

if comparison_file.exists():
    comparison = pd.read_csv(comparison_file)

    st.bar_chart(
        comparison.set_index("Model")[["MAE", "RMSE"]]
    )
else:
    st.warning("Model comparison report not found.")
    # Infrastructure Risk Analysis
st.header("Infrastructure Risk Analysis")

risk_reports = {
    "Risk by Severity": DATA / "infrastructure_risk_by_severity.csv",
    "Risk by Structure Type": DATA / "infrastructure_risk_by_structure.csv",
    "Risk by Failure Mode": DATA / "infrastructure_risk_by_failure_mode.csv",
}

for report_title, report_path in risk_reports.items():
    if report_path.exists():
        st.subheader(report_title)
        risk_df = pd.read_csv(report_path)
        st.dataframe(risk_df, use_container_width=True)
    else:
        st.warning(f"Report not found: {report_path.name}")
        # Historical Failure Analysis
st.header("Historical Failure Analysis")

failure_file = (
    ROOT / "data" / "raw" / "provided" / "DS6_historical_failures_2000.csv"
)

if failure_file.exists():
    failure_df = pd.read_csv(failure_file)

    st.write("Historical infrastructure failure records")
    st.metric("Total Failure Records", f"{len(failure_df):,}")

    st.subheader("Failure Records Preview")
    st.dataframe(failure_df.head(20), use_container_width=True)

    st.subheader("Failure Mode Distribution")
    failure_counts = failure_df["failure_mode"].value_counts()
    st.bar_chart(failure_counts)
else:
    st.warning("Historical failure dataset not found.")
    # Material Risk Analysis
st.header("Material Risk Analysis")

material_file = (
    ROOT / "data" / "raw" / "provided" / "DS1_material_properties_5500.csv"
)

if material_file.exists():
    material_df = pd.read_csv(material_file)

    st.metric("Total Materials", f"{len(material_df):,}")

    st.subheader("Material Categories")
    if "category" in material_df.columns:
        st.bar_chart(material_df["category"].value_counts())

    st.subheader("Material Stability")
    if "is_stable" in material_df.columns:
        stability_counts = (
            material_df["is_stable"]
            .fillna("Unknown")
            .astype(str)
            .value_counts()
        )
        st.bar_chart(stability_counts)

    st.subheader("Material Properties Preview")
    st.dataframe(material_df.head(20), use_container_width=True)

else:
    st.warning("Material properties dataset not found.")
    # Preliminary Infrastructure Risk Assessment
st.header("Preliminary Infrastructure Risk Assessment")

st.write(
    "Enter infrastructure details to review a simple "
    "rule-based risk category. This is not a trained model prediction."
)

age = st.number_input(
    "Infrastructure Age (years)",
    min_value=0,
    max_value=200,
    value=20
)

corrosion_rate = st.number_input(
    "Corrosion Rate (mm/year)",
    min_value=0.0,
    max_value=100.0,
    value=0.5,
    step=0.1
)

severity = st.selectbox(
    "Observed Severity",
    ["Low", "Medium", "High", "Critical"]
)

if st.button("Assess Risk"):
    score = 0

    if age >= 50:
        score += 2
    elif age >= 25:
        score += 1

    if corrosion_rate >= 1.0:
        score += 2
    elif corrosion_rate >= 0.5:
        score += 1

    severity_scores = {
        "Low": 0,
        "Medium": 1,
        "High": 2,
        "Critical": 3
    }
    score += severity_scores[severity]

    if score <= 1:
        risk_level = "Low"
    elif score <= 3:
        risk_level = "Medium"
    elif score <= 5:
        risk_level = "High"
    else:
        risk_level = "Critical"

    st.subheader(f"Preliminary Risk Category: {risk_level}")
    st.write(f"Rule-based risk score: {score}/7")
    st.caption(
        "Illustrative screening only. These thresholds are not "
        "validated engineering standards and must not be used "
        "for real-world safety decisions."
    )