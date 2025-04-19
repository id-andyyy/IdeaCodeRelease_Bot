from sqlalchemy import Column, Integer, Float, Boolean, Text, JSON, ForeignKey, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__: str = 'users'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    tg_id: Column = Column(Integer, unique=True, nullable=False)
    group_name: Column = Column(String)
    group_id: Column = Column(String)
