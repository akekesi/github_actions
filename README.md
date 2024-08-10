# Sample Project

## Description
Sample project for:
- Virtual Envirnment
- Folder Structure
- \_\_init\_\_.py
- unittest
- GitHub Actions

## Setup
- Shell Scripts
    - [Installation of Python 3.12.0](https://www.python.org/downloads/release/python-3120/)
    - Set up virtual environment and install packages:

        ```$. venv_setup.sh```
    - Unset virtual environment:

        ```$. venv_unset.sh```
- Manually
    - [Installation Python 3.12.0](https://www.python.org/downloads/release/python-3120/)
    - Installation of packages

        ```pip install -r requirements.txt```

## Run scripts as a module
```
$ python -m src.func_00
$ python -m src.class_00
$ python -m test.test_func_00
$ python -m test.test_class_00
$ python -m unittest discover test
```
