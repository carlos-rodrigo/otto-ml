import mlflow


def create_experiment(tracking_uri, project_name):
    mlflow_client = mlflow.tracking.MlflowClient(tracking_uri)
    experiment = mlflow_client.get_experiment_by_name(project_name)
    if(experiment == None):
        return mlflow_client.create_experiment(project_name)
    else:
        return experiment.experiment_id
