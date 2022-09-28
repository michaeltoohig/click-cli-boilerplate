from enum import Enum
from functools import wraps
{%- if "y" in cookiecutter.include_cli_tables | lower %}
from tabulate import tabulate
{%- endif %}
{%- if "y" in cookiecutter.include_cli_charts | lower %}
from termgraph.module import BarChart, Data
{%- endif %}

import click

{%- if "y" in cookiecutter.use_sqlalchemy | lower %}
from {{ cookiecutter.pkg_name }}.database.session import Session


def use_db_session(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        with Session() as db_session:
            func(db_session, *args, **kwargs)

    return wrapper_func

{%- endif %}
{%- if "y" in cookiecutter.include_cli_tables | lower %}

def print_table(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        data = func(*args, **kwargs)
        click.echo(tabulate(data))

    return wrapper_func

{%- endif %}
{%- if "y" in cookiecutter.include_cli_charts | lower %}

def print_chart(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        data, labels = func(*args, **kwargs)
        chart = BarChart(Data(data, labels))
        chart.draw()

    return wrapper_func

{%- endif %}

class EnumType(click.Choice):
    def __init__(self, enum: Enum, case_sensitive=False):
        self.__enum = enum
        super().__init__(
            choices=[item.value for item in enum], case_sensitive=case_sensitive
        )

    def convert(self, value, param, ctx):
        if value is None or isinstance(value, Enum):
            return value

        converted_str = super().convert(value, param, ctx)
        return self.__enum(converted_str)