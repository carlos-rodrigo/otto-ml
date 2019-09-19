import os
import errno
import click

_FILES_DIR = os.path.dirname(os.path.abspath(__file__)) + '/files/'
def create_dirs():
    dirs = ['/data',
            '/data/processed',
            '/data/raw',
            '/notebooks',
            '/src',
            '/tests']

    for d in dirs:
        current_dir = os.getcwd()
        full_dir = current_dir + d
        if not os.path.exists(full_dir):
            try:
                os.mkdir(full_dir)
            except OSError as exc: # Guard against race condition
                print(exc)

def create_file(file_name, project_name):
    full_path_file = _FILES_DIR + file_name
    with open(full_path_file, 'r') as reader:
        conda_content = reader.read()
    conda_content = conda_content.replace("*project_name*", project_name)

    with open(file_name, 'w') as writer:
        writer.write(conda_content)



def create_files(project_name):
    files = ['conda.yaml',
            'MLproject',
            'README.md',
            '.gitignore']

    for f in files:
        create_file(f, project_name)

@click.command()
@click.option('--name', prompt='Project name', default='machine-learning-project')
def init(name):
    """Creating the dir structure for a Machine Learning project with MLflow"""
    print("Creating directories....")
    create_dirs()
    print("Creating files....")
    create_files(name)
