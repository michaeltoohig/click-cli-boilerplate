#!/usr/bin/env python
import os
import shutil


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_directory(dirpath):
    try:
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))
    except:
        pass


def remove_file(filepath):
    try:
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    except FileNotFoundError:
        pass


if __name__ == "__main__":

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if "n" in "{{ cookiecutter.use_alembic | lower }}":
        alembic_file = os.path.join("alembic.ini")
        remove_file(alembic_file)
        alembic_directory = os.path.join("alembic")
        remove_directory(alembic_directory)

    if "n" in "{{ cookiecutter.use_sqlalchemy | lower }}":
        database_directory = os.path.join("{{ cookiecutter.pkg_name }}", "database")
        remove_directory(database_directory)
