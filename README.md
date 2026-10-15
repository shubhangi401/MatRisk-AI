# MatRisk AI

## Project Overview
MatRisk-AI is a data analytics and machine learning project focused on material properties, financial analysis, and infrastructure risk assessment. The project integrates material property datasets, commodity-related financial data, and historical infrastructure failure records to generate analytical insights.

It includes data preprocessing, feature engineering, financial model comparison, SHAP-based explainability, infrastructure risk summaries, and an interactive Streamlit dashboard. The platform also provides a preliminary rule-based infrastructure risk assessment for educational and analytical purposes.

## Project Objectives

The main objectives of MatRisk AI are:
The main objectives of MatRisk-AI are:

- Analyze material properties and material stability indicators.
- Perform data quality checks, validation, and preprocessing.
- Engineer features from financial and commodity-related datasets.
- Compare Ridge Regression and Random Forest models for financial prediction.
- Evaluate model performance using MAE, RMSE, and R² metrics.
- Analyze historical infrastructure failures by severity, structure type, and failure mode.
- Generate SHAP-based visual explanations of model features.
- Develop a preliminary rule-based infrastructure risk assessment.
- Build an interactive Streamlit dashboard to present analytical results.
- Identify model limitations and explore opportunities for future improvement.
- 
## Main Components

### 1. Material Science
- Material properties dataset ingestion and preprocessing.
- Data quality checks and material data validation.
- Analysis of material categories and stability indicators.
- Exploration of material properties through the Streamlit dashboard.
- Material property summaries for analytical insights.
-

### 2. Financial Analytics

- Financial and commodity-related dataset ingestion and preprocessing.
- Financial feature engineering and data preparation.
- Ridge Regression and Random Forest model training.
- Model comparison using MAE, RMSE, and R² metrics.
- Financial prediction outputs and CSV export.
- Model performance visualization through the Streamlit dashboard.
- SHAP-based model explainability visualization.
- Analysis of model limitations and opportunities for improvement.
### 3. Infrastructure Risk
- Historical infrastructure failure data analysis.
- Failure analysis by severity, structure type, and failure mode.
- Summary statistics for event counts, average repair costs, and loss ratios.
- Preliminary rule-based infrastructure risk assessment using age, corrosion rate, and observed severity.
- Interactive presentation of infrastructure risk summaries through the Streamlit dashboard.
- Identification of limitations and the need for engineering validation.

Note: The preliminary risk assessment is an illustrative rule-based screening tool. It is not a validated engineering model and must not be used independently for real-world structural safety decisions.

### 4. Generative Material Design
4. Advanced Material Design — Future Scope

The current implementation focuses on material property analysis and stability indicators. Advanced generative material design is planned as a potential future enhancement.

Possible future improvements include:

- Target-property-based material generation.
- Generative models such as Generative Adversarial Networks (GANs).
- Cost and material property constraints.
- Physics-based validation of generated materials.
- Multi-objective optimization and Pareto frontier analysis.
### 5. ESG Analysis
Environmental, Social, and Governance (ESG) analysis is a potential future extension of MatRisk-AI. It could help assess the environmental impact and sustainability of different materials.

Possible future enhancements include:

- Carbon intensity comparison of materials.
- Material substitution and sustainability analysis.
- Green premium evaluation.
- ESG scoring based on defined indicators.
- Green bond eligibility analysis, subject to suitable data and criteria.
### 6. Explainable AI
MatRisk-AI includes SHAP-based model explainability to help explore how input features influence model outputs.

Implemented features include:

- SHAP summary visualization.
- Financial model performance analysis.
- Comparison of Ridge Regression and Random Forest results.
- Visual presentation of analytical outputs through the Streamlit dashboard.

Future Scope:

- Local explanations for individual predictions.
- SHAP waterfall plots.
- Partial Dependence Plots (PDP).
- Additional model validation and explainability analysis.

## Dashboard
MatRisk-AI uses Streamlit to provide an interactive dashboard for exploring financial, material, and infrastructure risk analysis.

The dashboard includes:

1. Model Performance: Ridge Regression and Random Forest comparison using MAE, RMSE, and R².
2. Financial Dataset Overview: Dataset statistics and commodity-related visualizations.
3. Model Explainability: SHAP summary visualization.
4. Financial Predictions: Prediction tables and downloadable CSV output.
5. Infrastructure Risk Analysis: Risk summaries by severity, structure type, and failure mode.
6. Historical Failure Analysis: Historical failure records preview and failure mode distribution.
7. Material Risk Analysis: Material categories, stability indicators, and material property previews.
8. Preliminary Infrastructure Risk Assessment: A rule-based screening demonstration using infrastructure age, corrosion rate, and observed severity.

The dashboard is intended for educational and analytical use. Its preliminary risk assessment is not a validated structural safety model.

## MatRisk Lab
MatRisk Lab — Future Scope

MatRisk Lab is a proposed future extension of MatRisk-AI that could provide an interactive environment for exploring material and infrastructure risk scenarios.

Potential future features include:

- Infrastructure asset selection.
- Commodity and material scenario configuration.
- Scenario-based risk analysis.
- Interactive simulation and visualization.
- Educational scoring and feedback mechanisms.

These features are planned enhancements and are not part of the currently implemented dashboard unless explicitly developed and tested.

## Project Structure
## Project Structure

```text
MatRisk-AI/
├── app.py
├── data/
│   ├── raw/
│   │   └── provided/
│   └── processed/
├── models/
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── simulation/
├── .gitignore
└── README.md
```

### Key Directories

- `app.py`: Streamlit dashboard application.
- `data/raw/provided/`: Original input datasets.
- `data/processed/`: Cleaned datasets, analysis reports, model evaluation results, and visualizations.
- `models/`: Saved model prediction outputs.
- `src/data/`: Data quality, validation, ingestion, and merging scripts.
- `src/features/`: Feature engineering and financial data preparation scripts.
- `src/models/`: Model training, comparison, tuning, and explainability scripts.
- `src/simulation/`: Infrastructure risk analysis and testing scripts.
- `README.md`: Project overview, setup instructions, features, and limitations.

### Data Sources

MatRisk-AI uses the provided project datasets for material property analysis, financial modelling, and infrastructure risk assessment.

The main datasets include:

- DS1 — Material Properties: Material characteristics, stability indicators, density, band gap, and mechanical properties.
- DS2 — Commodity Prices: Historical commodity price data for financial analysis.
- DS3 — Infrastructure Bridges: Bridge and infrastructure-related records for potential risk analysis.
- DS4 — Cross-Domain Features: Daily cross-domain data used in financial data integration.
- DS5 — Element Prices: Monthly element price information.
- DS6 — Historical Failures: Historical infrastructure failure records, including severity, repair costs, loss ratios, and failure modes.

The project also includes a sample dataset workbook and a dataset README document.

Data Handling: Original input files are stored in "data/raw/provided/", while generated analysis reports and processed datasets are saved in "data/processed/".

Dataset availability does not imply that every dataset is currently used in a model. The implemented analysis depends on the relevant columns and processing scripts.

### Model Training Pipeline
The financial modelling workflow in MatRisk-AI consists of the following stages:

1. Data Quality Checks: Inspect input data for quality issues.
2. Data Validation: Validate material data and required fields.
3. Data Integration: Merge the relevant financial and cross-domain datasets.
4. Feature Engineering: Create features for financial modelling.
5. Data Preparation: Clean the financial features and prepare data for modelling.
6. Model Training: Train Ridge Regression and Random Forest models.
7. Model Evaluation: Compare model performance using MAE, RMSE, and R².
8. Hyperparameter Tuning: Evaluate different Ridge Regression alpha values.
9. Explainability: Generate a SHAP summary visualization.
10. Dashboard Integration: Present model metrics, predictions, and analytical results through Streamlit.

The current financial models show limited predictive performance. Further feature engineering, validation, and model development are required before practical deployment.

## Dashboard Launch
### Prerequisites
- Python 3.11
- Git
- The project datasets in the expected directory structure

### Setup Instructions

1. Clone or download the project repository.
2. Open a terminal in the project root directory.
3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the environment on Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the Streamlit dashboard:

   ```bash
   python -m streamlit run app.py
   ```

7. Open the local URL displayed in the terminal.

**Note:** Ensure that `requirements.txt` exists and includes the packages required by the project before following the installation instructions.

### Testing
MatRisk-AI includes a basic project testing script to check the availability and readability of important output files.

Tests Performed

- Financial feature dataset verification.
- Model comparison report verification.
- Infrastructure risk report verification by severity, structure type, and failure mode.
- SHAP visualization file verification.
- Ridge Regression prediction file verification.
- Random Forest prediction file verification.

Test Results

The project testing script completed successfully, and all eight file checks returned "PASS".

The checks confirmed that the expected output files were available and that the CSV files could be read successfully.

Note: These checks verify file availability and readability. They do not establish model accuracy, scientific validity, or real-world infrastructure safety.
 ### Results:

Financial Model Comparison

The project evaluated Ridge Regression and Random Forest models using a chronological train-test split.

Model| MAE| RMSE| R²
Ridge Regression| 0.016534| 0.021171| -0.0014
Random Forest| 0.016557| 0.021188| -0.0031

Key Observations

- Ridge Regression performed slightly better than Random Forest on the evaluated dataset.
- Both models produced R² values close to zero and slightly below zero, indicating limited predictive performance on the test data.
- Hyperparameter tuning did not produce a substantial improvement.
- The project generated financial prediction outputs and a SHAP summary visualization.
- Infrastructure risk summaries were generated by severity, structure type, and failure mode.
- Material property and historical failure information are presented through the Streamlit dashboard.

Interpretation

These results represent the current experimental implementation. Additional feature engineering, validation, and model development are needed before the financial models can be considered useful for practical prediction.

### Limitations
- The financial models currently show limited predictive performance.
- The current evaluation does not establish that the models will generalize to new datasets.
- The infrastructure risk assessment uses illustrative rules and is not a validated engineering safety model.
- Material property analysis is limited to the available dataset fields and implemented analysis.
- Further independent validation is required before practical deployment.

Future Scope

- Improve financial model performance through feature engineering and systematic validation.
- Evaluate additional machine learning algorithms.
- Develop more comprehensive infrastructure risk models using validated engineering data.
- Extend material property analysis with additional datasets and scientific methods.
- Add interactive filters and more detailed dashboard visualizations.
- Explore ESG analysis and generative material design as future enhancements.
- Improve automated testing and project documentation.

### Conclusion
MatRisk-AI demonstrates the integration of data analytics, machine learning, material property analysis, and infrastructure risk assessment within an interactive Streamlit dashboard.

The project includes financial data preprocessing, feature engineering, Ridge Regression and Random Forest model comparison, SHAP-based visualization, historical infrastructure failure summaries, and a preliminary rule-based risk assessment.

The evaluation highlights the importance of model validation, as the current financial models show limited predictive performance. The project provides a foundation for further experimentation, improved risk analysis, and future development of more advanced analytical capabilities.
