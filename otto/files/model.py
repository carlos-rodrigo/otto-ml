import sys
from settings import MLFLOW_CLIENT, MLFLOW_EXPERIMENT_NAME


# Data Manipulation
import numpy as np
import pandas as pd

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn import model_selection, tree, preprocessing, metrics, linear_model
from sklearn.ensemble import GradientBoostingClassifier

import mlflow
import mlflow.sklearn

mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)
EXPERIMENT_ID = MLFLOW_CLIENT.get_experiment_by_name(MLFLOW_EXPERIMENT_NAME).experiment_id

def train_model():
   with mlflow.start_run(experiment_id=EXPERIMENT_ID):
        # INSERT YOUR CODE HERE #


        #LOG PARAM METRICS & ARTIFACTS EXAMPLES
        mlflow.log_param("learning rate", learning_rate)
        mlflow.log_param("n_estimators", estimators)
        mlflow.log_param("loss", loss)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("accuracy cross-validated", acc_cv)

        mlflow.sklearn.log_model(model, "model")
