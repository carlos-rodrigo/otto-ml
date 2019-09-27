import os
import click

from otto.utils import create_file, write_file, create_dirs, create_files, create_docker_file


@click.command()
@click.option('--name', prompt='Project name', default='machine-learning-project')
def init(name):
    """Creating the dir structure for a Machine Learning project with MLflow"""
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
    write_file('', current_dir + '/src/__init__.py')
    create_docker_file()
    print("Done!")
