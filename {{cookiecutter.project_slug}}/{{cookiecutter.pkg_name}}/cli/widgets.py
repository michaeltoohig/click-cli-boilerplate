import click

from {{ cookiecutter.pkg_name }}.loggerfactory import LoggerFactory
{%- if "y" in cookiecutter.use_sqlalchemy | lower %}
from {{ cookiecutter.pkg_name }}.database.models import Widget
from {{ cookiecutter.pkg_name }}.cli.utils import use_db_session
{%- endif %}
{%- if "y" in cookiecutter.include_cli_tables | lower %}
from {{ cookiecutter.pkg_name }}.cli.utils import print_table
{%- endif %}
{%- if "y" in cookiecutter.include_cli_charts | lower %}
from {{ cookiecutter.pkg_name }}.cli.utils import print_chart
{%- endif %}

logger = LoggerFactory.get_logger("widgets")


@click.group()
@click.pass_context
def widgets(ctx):
    pass

{% if "y" in cookiecutter.use_sqlalchemy | lower %}

@widgets.command()
@click.argument("widget_id", type=click.INT)
@use_db_session
def details(db_session, widget_id):
    """Details of a widget."""
    widget = Widget.get_by_id(db_session, widget_id)
    click.echo(widget)

{% endif %}
{% if "y" in cookiecutter.include_cli_tables | lower %}

@widgets.command()
@print_table
def show_table():
    table_demo = [
        {"id": 1, "name": "Widget 1"},
        {"id": 2, "name": "Widget 2"},
    ]
    return [
        (
            i.get("id"),
            i.get("name"),
        )
        for i in table_demo
    ]

{% endif %}
{% if "y" in cookiecutter.include_cli_charts | lower %}

@widgets.command()
@print_chart
def show_chart():
    data = [1, 2]
    labels = ["Widget 1", "Widget 2"]
    return data, labels
{% endif %}
