import os
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_validate
from sklearn.metrics import average_precision_score, f1_score, recall_score, precision_score,accuracy_score

def benchmark_models(pipeline, list_model, x_train, y_train, x_test, y_test, cv=5, postfix="Base"):
    all_cv_result = []

    for name, model in list_model.items():
        classifier = pipeline.set_params(classifier=model)

        cv_result = cross_validate(
            estimator=classifier,
            X=x_train, y=y_train,
            cv=cv,
            scoring="average_precision",
            return_train_score=True,
            n_jobs=-1 
        )
        
        classifier.fit(x_train, y_train)
        
        y_pred_proba = classifier.predict_proba(x_test)[:, 1]
        y_pred = classifier.predict(x_test)
        test_ap_score = average_precision_score(y_test, y_pred_proba)
        test_f1_score = f1_score(y_test, y_pred)
        test_recall_score = recall_score(y_test, y_pred)
        test_precision_score = precision_score(y_test, y_pred)
        test_accuracy_score = accuracy_score(y_test, y_pred)
        
        all_cv_result.append({
            "name": name + "_" + postfix,
            "ap_test_score": test_ap_score,
            "mean_ap_train_score": np.mean(cv_result["train_score"]),
            "mean_ap_validate_score": np.mean(cv_result["test_score"]),
            "f1_test_score": test_f1_score,
            "recall_test_score": test_recall_score,
            "precision_test_score": test_precision_score,
            "accuracy_test_score": test_accuracy_score,
        })
        
        

    result_df = pd.DataFrame(all_cv_result).sort_values(
        "mean_ap_validate_score", ascending=False
    ).reset_index(drop=True)

    return result_df
