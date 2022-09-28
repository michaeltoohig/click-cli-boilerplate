{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![python](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/dev.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graphs/badge.svg)](https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

{% else %}
{% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Documentation: <https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}>
* GitHub: <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>
* PyPI: <https://pypi.org/project/{{ cookiecutter.project_slug }}/>
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}

## Features

* TODO

## Usage

Activate the local environment (gives access to installed packages required for this tool to work)

    poetry shell

For help, run:

    poetry run {{ cookiecutter.project_slug }} --help

For crontab usage example:

    */5 * * * cd /path/to/{{ cookiecutter.project_slug }} && . /path/to/pypoetry/virtualenv/bin/activate && {{ cookiecutter.project_slug }} [COMMAND] >> logs/`date +\%Y-\%m-\%d`.log 2>&1
    0 0 * * * /usr/bin/find /path/to/{{ cookiecutter.project_slug }}/logs -name "*.log" -type f -mtime +7 -exec rm -f {} \;

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd {{ cookiecutter.project_slug }}
    poetry shell
    poetry install

To run the tests:

    pytest

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [michaeltoohig/click-cli-boilerplate](https://github.com/michaeltoohig/click-cli-boilerplate) project template.
