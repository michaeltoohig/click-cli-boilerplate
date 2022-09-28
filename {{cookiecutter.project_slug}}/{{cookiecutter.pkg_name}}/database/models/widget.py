from sqlalchemy import select, Column, Integer

from {{ cookiecutter.pkg_name }}.database.models.base import Base


class Widget(Base):

    __tablename__ = "widgets"

    id = Column(Integer(), primary_key=True, autoincrement=True)

    def __str__(self):
        return f"<Widget({self.id})>"

    @classmethod
    def get_by_id(cls, db_session, widget_id):
        query = select(cls).filter(cls.id == widget_id)
        return db_session.execute(query).scalars().one()
