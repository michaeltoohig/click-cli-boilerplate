import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

{%- if "y" in cookiecutter.use_sqlalchemy | lower %}
DATABASE_URI = os.environ.get("DATABASE_URI")
{%- endif %}