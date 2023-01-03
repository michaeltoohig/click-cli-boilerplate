import logging

import click

from {{ cookiecutter.pkg_name }}.logging import configure_logger
from .widgets import widgets as widgets_cli


@click.group()
@click.version_option()
@click.option(
    "--strict",
    is_flag=True,
    default=False,
    help="Format log messages appropriate for production use.",
)
@click.option("-v", "--verbose", count=True, help="Show more log messages.")
def cli(strict, verbose):
    "{{ cookiecutter.project_short_description }}"
    log_levels = {0: logging.WARN, 1: logging.INFO, 2: logging.DEBUG}
    idx = min(verbose, 2)
    level = log_levels[idx]
    configure_logger(strict, level)


cli.add_command(widgets_cli)
