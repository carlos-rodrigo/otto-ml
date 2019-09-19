import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="otto-ml",
    version="0.1.1",
    author="Carlos Rodrigo",
    author_email="hi@carlosrodrigo.me",
    description="Otto is a simple Boilerplate for Machine Learning projects integrated with MLflow tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carlos-rodrigo/otto-ml",
    packages=setuptools.find_packages(),
    include_package_data=True,
    py_modules=['otto'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        otto=otto:init
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
