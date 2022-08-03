# pybamm-param: PyBaMM Parameter Optimization Tool

[![pybamm-param](https://github.com/paramm-team/pybamm-param/actions/workflows/test_on_push.yml/badge.svg?branch=main)](https://github.com/paramm-team/pybamm-param/actions/workflows/test_on_push.yml)
[![codecov](https://codecov.io/gh/paramm-team/pybamm-param/branch/main/graph/badge.svg?token=CMFXMUU1SJ)](https://codecov.io/gh/paramm-team/pybamm-param)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**WARNING:** this package is still under development.

This package is provides parameter optimization for PyBaMM (Python Battery Mathematical Modelling) using different optimization techniques. Examples on how to run this package can be found in the [examples folder](./examples)

## How to install?
These installation instructions assume you have Python installed (versions 3.7, 3.8 or 3.9) and that you have also installed the `virtualenv` package which can be done by running
```bash
pip install virtualenv
```

The first step, common across operating systems, is to clone this repository
```bash
git clone git@github.com:muhammedsogut/Pybamm.git
```
and then go into the cloned folder
```bash
cd Pybamm
```

### Linux & MacOS
1. Create a virtual environment (this is strongly recommended to avoid clashes with the dependencies)
```bash
virtualenv env
```

2. Activate the virtual environment
```bash
source env/bin/activate
```
The virtual environment can later be deactivated (if needed) by running
```bash
deactivate
```

3. Install requirements
```bash
pip install -e .[dev]
```

### Windows
1. Create a virtual environment (this is strongly recommended to avoid clashes with the dependencies)
```bash
python -m virtualenv env
```

2. Activate the virtual environment
```bash
env\Scripts\activate.bat
```
The virtual environment can later be deactivated (if needed) by running
```bash
deactivate
```

3. Install requirements
```bash
pip install -e .[dev]
```
