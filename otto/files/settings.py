import os
import mlflow

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "")
S3_BUCKET = os.getenv("S3_BUCKET", "")
MLFLOW_SERVER_TRACKING_URI = os.getenv("MLFLOW_SERVER_TRACKING_URI", "")

MLFLOW_CLIENT = mlflow.tracking.MlflowClient(MLFLOW_SERVER_TRACKING_URI)
MLFLOW_EXPERIMENT_NAME = '*project_name*'

def setup():
    print('MLFLOW Traking Server URI ->' + MLFLOW_SERVER_TRACKING_URI)
    mlflow.set_tracking_uri(MLFLOW_SERVER_TRACKING_URI)
