import streamlit as st
import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    matthews_corrcoef,
    confusion_matrix,
    classification_report
)

st.set_page_config(
    page_title="Aviation Satisfaction Classification",
    layout="wide"
)

st.title(
    "Aviation Customer Satisfaction Prediction"
)

models = {
    "Logistic Regression":
        "models/logistic_regression.pkl",

    "Decision Tree":
        "models/decision_tree.pkl",

    "KNN":
        "models/knn.pkl",

    "SVM":
        "models/svm.pkl"
}

selected_model = st.selectbox(
    "Select ML Model",
    list(models.keys())
)

uploaded_file = st.file_uploader(
    "Upload Test Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    TARGET = "satisfaction"

    X = df.drop(TARGET, axis=1)
    y = df[TARGET]

    target_encoder = joblib.load(
        "models/target_encoder.pkl"
    )

    y = target_encoder.transform(y)

    model = joblib.load(
        models[selected_model]
    )

    preds = model.predict(X)

    probs = model.predict_proba(X)[:,1]

st.subheader("Evaluation Metrics")

st.write(
    "Accuracy:",
    round(accuracy_score(y,preds),4)
)

st.write(
    "AUC:",
    round(roc_auc_score(y,probs),4)
)

st.write(
    "Precision:",
    round(precision_score(y,preds),4)
)

st.write(
    "Recall:",
    round(recall_score(y,preds),4)
)

st.write(
    "F1:",
    round(f1_score(y,preds),4)
)

st.write(
    "MCC:",
    round(
        matthews_corrcoef(y,preds),
        4
    )
)

st.subheader("Confusion Matrix")

cm = confusion_matrix(y,preds)

st.dataframe(cm)

st.subheader(
    "Classification Report"
)

report = classification_report(
    y,
    preds,
    output_dict=True
)

st.dataframe(
    pd.DataFrame(report).transpose()
)

results = pd.read_csv(
    "model_results.csv"
)

st.subheader(
    "Model Comparison"
)

st.dataframe(results)