import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

files = package_files('otto/files')
setuptools.setup(
    name="otto-ml",
    version="0.1.30",
    author="Carlos Rodrigo",
    author_email="hi@carlosrodrigo.me",
    description="Otto is a simple Boilerplate for Machine Learning projects integrated with MLflow tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carlos-rodrigo/otto-ml",
    packages=setuptools.find_packages(),
    package_data={"otto": files},
    install_requires=[
        'click>=7.0',
        'numpy',
        'pandas',
        'mlflow'
    ],
    extras_require={
        'extras':[
            "scikit-learn; python_version >= '3.5'",
            # scikit-learn 0.20 is the last version to support Python 2.x  & Python 3.4.
            "scikit-learn==0.20; python_version < '3.5'",
            'boto3>=1.7.12',
        ],
    },
    entry_points='''
        [console_scripts]
        otto=otto.cli:init
    ''',    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
