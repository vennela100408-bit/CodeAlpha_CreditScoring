# CodeAlpha - Credit Scoring Model

Machine Learning Internship — Task 1.

## Objective
Predict an individual's creditworthiness using financial history.

## Models
- Logistic Regression
- Decision Tree
- Random Forest

The training script compares Accuracy, Precision, Recall, F1-Score and ROC-AUC and saves the best model as `models/credit_scoring_model.pkl`.

## Run locally
```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Then open the Local URL shown by Streamlit.

## Project structure
- `app.py` — Streamlit user interface
- `data/credit_data.csv` — sample financial dataset
- `models/credit_scoring_model.pkl` — trained model
- `model_results.csv` — model evaluation results
- `requirements.txt` — dependencies
