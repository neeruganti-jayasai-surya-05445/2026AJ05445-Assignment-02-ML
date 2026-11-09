#### 2026AJ05445-Assignment-02-ML
Repo created for Assignment 02 (Machine Learning Course)

## Aviation Passenger Satisfaction Classification

---

### 1. Problem Statement

Customer satisfaction is one of the most important indicators of service quality in the aviation industry. Airlines collect passenger feedback on various aspects of travel such as inflight service, seating comfort, cleanliness, check-in process, baggage handling, flight delays, and overall travel experience.

The objective of this assignment is to predict whether a passenger is satisfied or dissatisfied based on travel-related features, using Machine Learning Classification Models. This can help airlines improve customer experience, identify factors affecting passenger satisfaction, and make data-driven business decisions.

---

### 2. Dataset Description

---

| Attribute | Details |
|------------|---------|
| Dataset Name | Binary Aviation Satisfaction Dataset |
| Source | Kaggle |
| Dataset Link | https://www.kaggle.com/datasets/arseniyshutko/binary-aviation-satisfaction-129k |
| Dataset Overview | The dataset contains approximately 129,000 passenger records collected from airline customers. |
| Problem Type | Binary Classification |
| Target Variable | Satisfaction |

---

### 3. GitHub Repository Link

---

**Repository URL:** https://github.com/neeruganti-jayasai-surya-05445/2026AJ05445-Assignment-02-ML.git

---

### 4. Models Used

---

The following machine learning classification algorithms were implemented:
1. Logistic Regression
2. Decision Tree Classifier
3. K-Nearest Neighbors (KNN)
4. Support Vector Machine (SVM)

---

### 5. Model Comparison Table

---

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|--------------|----------|-----|-----------|--------|----------|-----|
| Logistic Regression | 0.8738126496254537 | 0.9269070420036241| 0.8673291011132579 | 0.8377321603128055 | 0.8522737546333966 | 0.7425423437999803 |
| Decision Tree | 0.9447061549154375 | 0.9863458284345978 | 0.9520390315750713 | 0.9190438105394118 | 0.9352504973774642 | 0.8874488378841241 |
| KNN | 0.9293381728318789 | 0.9714268737016285 | 0.9439366814284368 | 0.8902514884919577 | 0.9163084240373182 | 0.856354238289842 |
| Support Vector Machine | 0.9530851803228049 | 0.9886039144919649 | 0.9570205791294846 | 0.9339731627121657 | 0.9453564200584664 | 0.9044718880344019 |

---

### 6. Observations

| ML Model Name | Observation about Model Performance |
|---------------|-------------------------------------|
| Logistic Regression | Logistic Regression provided a strong baseline performance with an Accuracy of 87.38% and an AUC of 0.9269. The model demonstrated good generalization capability but was less effective than the non-linear models in capturing complex relationships within the aviation satisfaction data. |
| Decision Tree | Decision Tree achieved a high Accuracy of 94.47% and an AUC of 0.9863. The model successfully captured non-linear patterns in the dataset and produced strong Precision, Recall, and MCC scores, making it a highly competitive classifier. |
| K-Nearest Neighbors (KNN) | KNN delivered strong classification performance with an Accuracy of 92.93% and an AUC of 0.9714. While it effectively classified passenger satisfaction levels, its performance was slightly lower than Decision Tree and SVM, particularly in Recall and MCC. |
| Support Vector Machine (SVM) | SVM achieved the best overall performance across all evaluation metrics. With an Accuracy of 95.31%, AUC of 0.9886, F1 Score of 0.9454, and MCC of 0.9045, it provided the most balanced and reliable predictions for passenger satisfaction classification. |
| Overall Winner for Dataset | **Support Vector Machine (SVM)** is the best-performing model for this dataset. It achieved the highest Accuracy, AUC, F1 Score, and MCC, indicating superior classification capability and excellent class separation performance. |

---

### 7. Evaluation Metrics Used

---

The following evaluation metrics were used to assess all models:
1. Accuracy
2. AUC Score
3. Precision
4. Recall
5. F1 Score
6. Matthews Correlation Coefficient (MCC)

---

### 8. Streamlit Web Application

---

**Application URL:** https://2026aj05445-assignment-02-mlgit-uy4ej2apphm9jkcgt3bdn9p.streamlit.app/

The application provides the following features:
1. **Dataset Upload:** Upload test_data.csv file
2. **Model Selection:** Logistic Regression, Decision Tree, KNN, SVM
3. **Evaluation Metrics Display:** Accuracy, AUC Score, Precision, Recall, F1 Score, MCC Score
4. **Performance Visualization:** Confusion Matrix, Classification Report

---

### 9. Requirements

```bash
numpy
pandas
matplotlib
scikit-learn
kagglehub
streamlit
joblib
seaborn
```

---

### 10. Conclusion

---
 
Among all the evaluated machine learning models, the Support Vector Machine (SVM) demonstrated the best predictive performance on the Aviation Passenger Satisfaction dataset. Its superior AUC, F1 Score, and MCC indicate that it not only achieved high classification accuracy but also maintained an excellent balance between Precision and Recall. Therefore, SVM was selected as the final recommended model for this classification problem.

---