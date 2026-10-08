# MatRisk AI

## Project Overview

MatRisk AI is an AI-driven decision intelligence platform that combines
material science, financial analytics, infrastructure risk modelling,
machine learning, explainability, and ESG analysis.

The project aims to connect material properties and material-market signals
with financial and infrastructure risk decisions.

## Project Objectives

The main objectives of MatRisk AI are:

- Predict material properties using machine learning and crystal graph models.
- Engineer material-science features using Matminer.
- Build financial and commodity-market features.
- Create cross-domain features such as Material Quality Index (MQI),
  Substitution Elasticity, and Green Premium.
- Develop infrastructure risk models using survival analysis and financial
  risk measures.
- Implement physics-informed constraints for material predictions.
- Develop inverse material design using generative modelling.
- Provide ESG and sustainability analysis.
- Build explainable AI using SHAP and Partial Dependence Plots.
- Provide an interactive Streamlit dashboard.
- Build the MatRisk Lab simulator for scenario-based decision making.

## Main Components

### 1. Material Science

- Materials Project and AFLOW data ingestion
- Material data preprocessing
- Matminer feature engineering
- Crystal graph construction
- Crystal Graph Neural Network (CGNN)
- Physics-informed modelling

### 2. Financial Analytics

- Commodity price data
- Technical indicators
- Volatility and momentum features
- Material-market signals
- Commodity prediction
- Backtesting and financial performance analysis

### 3. Infrastructure Risk

- National Bridge Inventory (NBI) data
- Survival analysis
- Probability of Default (PD)
- Loss Given Default (LGD)
- Expected Loss (EL)
- Catastrophe and stress testing models

### 4. Generative Material Design

- Target-property based material generation
- Generative Adversarial Network (GAN)
- Cost constraints
- Physics validation
- Pareto frontier analysis

### 5. ESG Analysis

- Carbon intensity comparison
- Material substitution analysis
- Green premium
- ESG scoring
- Green bond eligibility analysis

### 6. Explainable AI

The project includes:

- SHAP global explanations
- SHAP local explanations
- SHAP waterfall plots
- Partial Dependence Plots (PDP)
- Model performance analysis
- Physics constraint audit

## Dashboard

The Streamlit dashboard contains five major pages:

1. Material Property Explorer
2. Commodity Signal Dashboard
3. Infrastructure Risk Scorer
4. Inverse Material Designer
5. ESG Impact Analyser

## MatRisk Lab

MatRisk Lab is a gamified simulator prototype.

The initial implementation includes:

- Campaign Mode Level 1
- Campaign Mode Level 2
- Infrastructure asset selection
- Commodity position
- Scenario injection
- Basic scoring

## Project Structure

```text
MatRisk-AI/
│
├── .venv/
├── data/
├── src/
├── notebooks/
├── models/
├── tests/
├── dashboard/
├── docs/
├── configs/
├── .gitignore
└── README.md
## Data Sources
...
## Model Training Pipeline
...
## Dashboard Launch
...
## Testing
...
## Documentation
...
## Results
...
## Contributing
...
## IP Attribution
...
## Project Status
...