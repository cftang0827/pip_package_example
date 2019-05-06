# pip package and setup.py example

This is a very simple example of python package and setup.py, including a `package_data`.

The api read a json file called `model.json` in `data` directory, and print the value. If there's any path bug, the value of json cannot be printed properly.

If there's something wrong in setup.py, after you use `pip install`, you may not find proper `package_data` in your package path.

## Installation by pip + git
You can install the package simply by using
```
pip install git+https://github.com/cftang0827/pip_package_example@master
```

## Tree view of the project
```
├── LICENSE
├── README.md
├── pip_package_example
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── api.cpython-36.pyc
│   ├── api.py
│   └── data
│       ├── __init__.py
│       └── model.json
└── setup.py
```
