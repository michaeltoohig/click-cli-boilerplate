import click

from .widgets import widgets as widgets_cli


@click.group()
@click.version_option()
def cli():
    "{{ cookiecutter.project_short_description }}"


cli.add_command(widgets_cli)
