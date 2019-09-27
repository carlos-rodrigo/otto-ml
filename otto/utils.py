import os

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
    files = ['MLproject',
             'README.md',
             '.dockerignore',
             'build_image.sh',
             '.gitignore']
    for f in files:
        create_file(f, project_name)

def create_docker_file():
    docker_file = 'Dockerfile'
    keys = ['AWS_ACCESS_KEY_ID',
            'AWS_SECRET_ACCESS_KEY',
            'S3_BUCKET',
            'DB_CONNECTION',
            'MLFLOW_TRACKING_URI']
    docker_content = get_file_content_from_files(docker_file)
    for k in keys:
        wildcarded_key = '*'+k+'*'
        docker_content = search_keyword_and_replace(docker_content, wildcarded_key, os.getenv(k, ''))
    write_file(docker_content, docker_file)
