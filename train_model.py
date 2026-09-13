import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

df = pd.read_csv("data/credit_data.csv")
X = df.drop(columns=["credit_risk"])
y = df["credit_risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(max_depth=6, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=250, random_state=42)
}

best_auc = -1
best_model = None

for name, estimator in models.items():
    pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("model", estimator)
    ])
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    proba = pipe.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, proba)
    print(f"{name}: Accuracy={accuracy_score(y_test,pred):.4f}, "
          f"Precision={precision_score(y_test,pred,zero_division=0):.4f}, "
          f"Recall={recall_score(y_test,pred,zero_division=0):.4f}, "
          f"F1={f1_score(y_test,pred,zero_division=0):.4f}, ROC-AUC={auc:.4f}")
    if auc > best_auc:
        best_auc = auc
        best_model = pipe

joblib.dump(best_model, "models/credit_scoring_model.pkl")
print("Saved models/credit_scoring_model.pkl")
