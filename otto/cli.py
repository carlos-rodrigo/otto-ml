import os
import errno
import click

_FILES_DIR = os.path.dirname(os.path.abspath(__file__)) + '/files/'
_PROJECT_NAME_WILDCARD = "*project_name*"
def create_dirs():
    dirs = ['/data',
            '/data/processed',
            '/data/raw',
            '/notebooks',
            '/src',
            '/src/models',
            '/src/data',
            '/src/features',
            '/tests']

    for d in dirs:
        current_dir = os.getcwd()
        full_dir = current_dir + d
        if not os.path.exists(full_dir):
            try:
                os.mkdir(full_dir)
            except OSError as exc: # Guard against race condition
                print(exc)

def get_file_content_from_files(file_name):
    full_path_file = _FILES_DIR + file_name
    with open(full_path_file, 'r') as reader:
        file_content = reader.read()
        return file_content

def write_file(content, file_path):
    with open(file_path, 'w') as writer:
        writer.write(content)

def search_keyword_and_replace(content, keyword, content_to_be_inserted):
    return content.replace(keyword, content_to_be_inserted)


def create_file(file_name, project_name, extra_path=''):
    file_content = get_file_content_from_files(file_name)
    file_content = search_keyword_and_replace(file_content,_PROJECT_NAME_WILDCARD, project_name)

    write_file(file_content, extra_path + file_name)

def create_files(project_name):
    files = ['Dockerfile',
            'MLproject',
            'README.md',
            '.env',
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

    current_dir = os.getcwd()
    full_dir = current_dir + '/src/models/'
    create_file('model.py', name, full_dir)
    write_file('', full_dir + '__init__.py')
    write_file('', current_dir + '/src/data/__init__.py')
    write_file('', current_dir + '/src/data/data_preparation.py')
    write_file('', current_dir + '/src/__init__.py')
    create_file('train.py', name, current_dir + '/')

    print("Done!")
