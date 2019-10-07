import os
import click

from otto.utils.files import create_file, write_file, create_dirs, create_files, create_docker_file, create_build_image_file
from otto.utils.mlflow import create_experiment

@click.command()
@click.option('--name', prompt='Project name', default='new-project')
@click.option('--tracking-uri', 'tracking_uri',  prompt='Mlflow Tracking Uri', default='')
def init(name, tracking_uri):
    """Creating the dir structure for a Machine Learning project with MLflow"""
    mlflow_experiment_id = 0
    if(tracking_uri == ''):
        tracking_uri = os.getenv('MLFLOW_TRACKING_URI', '')
    if(tracking_uri != ''):
        print("Creating mlflow experiment....")
        mlflow_experiment_id = create_experiment(tracking_uri, name)

    print("Creating directories....")
    create_dirs()
    print("Creating files....")
    create_files(name)

    current_dir = os.getcwd()
    full_dir = current_dir + '/src/models/'

    create_file('model.py', name, full_dir)
    create_file('train.py', name, current_dir + '/src/')
    create_file('settings.py', name, current_dir + '/src/')

    write_file('', full_dir + '__init__.py')
    write_file('', current_dir + '/src/data/__init__.py')
    write_file('', current_dir + '/src/data/data_preparation.py')
    write_file('', current_dir + '/src/utils/__init__.py')
    write_file('', current_dir + '/src/features/__init__.py')
    write_file('', current_dir + '/src/__init__.py')
    create_docker_file(tracking_uri)
    create_build_image_file(tracking_uri, mlflow_experiment_id, name)
    print("Done!")
