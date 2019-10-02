#!/bin/sh
export TEMP="/private"
export MLFLOW_TRACKING_URI="*MLFLOW_TRACKING_URI*"
export MLFLOW_EXPERIMENT_ID="*MLFLOW_EXPERIMENT_ID*"

docker build -t *project_name* -f Dockerfile .
