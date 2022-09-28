# Click CLI Boilerplate

Cookiecutter template for a Click CLI project.

## Features

This tool will create Python Click CLI project with the following features:

* [Poetry](https://python-poetry.org/): Manage dependency, build and release
* Testing with [Pytest](https://pytest.org) (unittest is still supported out of the box)
* Code coverage report and endorsed by [Codecov](https://codecov.io)
* Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
* Lint code with [Flake8](https://flake8.pycqa.org) and [Flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
* Command line interface using [Click](https://click.palletsprojects.com/en/8.0.x/) (optional)
* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/michaeltoohig/click-cli-boilerplate.git
```

# Credits

This repo is forked from [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage), which is forked from [zillionare/python-project-wizard](https://github.com/zillionare/python-project-wizard), which originally forked from [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
