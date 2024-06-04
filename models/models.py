import datetime
from typing import Optional

from sqlalchemy import text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from core.config import DbConfig
db_config = DbConfig()
Base = declarative_base()
engine = create_engine(db_config.database_url, echo=True)


class Todo(Base):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                          onupdate=datetime.datetime.utcnow)
