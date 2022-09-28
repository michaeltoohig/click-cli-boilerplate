from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from {{ cookiecutter.pkg_name }}.config import DATABASE_URI

engine = create_engine(DATABASE_URI)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)
