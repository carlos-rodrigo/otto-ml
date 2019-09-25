# OTTO
Otto is a simple Boilerplate for Machine Learning projects integrated with MLflow that creates a basic directory structure to organize your code and data.
Otto is strongly based on [Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/), if you need something more complete is a good desition to visit his repo. 

```
├── MLproject
├── README.md
├── Dockerfile
├── .env
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

and that's it!  😝

...someone says "ok, but how supposedly I will use this directory structure in practice" go to the Wiki to find out. 



