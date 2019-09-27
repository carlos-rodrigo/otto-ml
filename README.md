# OTTO
Otto is a simple Boilerplate for Machine Learning projects integrated with MLflow that creates a basic directory structure to organize your code and data.
Otto is strongly based on [Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/), if you need something more complete is a good desition to visit they repo. 

```
├── MLproject
├── README.md
├── Dockerfile
├── build_image.sh
├── .gitignore
├── data
│   ├── processed/
│   └── raw/
├── notebooks/
├── src/
│   ├── data/
│   │   └── __init__.py
│   │   └── data_preparation.py
│   ├── features/
│   │   └── __init__.py
│   ├── models/
│   │   └── __init__.py
│   │   └── model.py
│   ├── train.py
│   ├── settings.py
│   └── __init__.py
└── tests/
```

## Usage

Simple install otto using pip as follows

`pip install otto-ml`

and use otto

`otto --name new-project`

or simple use it with out params and let otto guides you 😉

`otto`

and that's it, Now you can jump to code your model! 

## Ok, but... what this solve?

That is a pretty good question. The first attempt is to simplify the startup of a new machine learning project generating most, not machine-learning related code. Like the configuration of the docker image via `Dockerfile` or the `MLProject` setup and the connection with the Mlflow tracking server if you have set up one using ENV variables. 

But to make it cristal water, let show how it will be a standard use of the `otto` package. 

### The Titanic Competition Example

... In development ...




