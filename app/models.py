# --[ models.py ]~
# --[ This file defines all of the database tables and views for StudentSplit.
# --[ This file uses SQLAlchemy ORM with declarative base.

# --/
import enum
from sqlalchemy import (
    Column, Integer, String, Numeric, Boolean, DateTime,
    ForeignKey, Enum, Text, UniqueConstraint, CheckConstraint
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func, text

Base = declarative_base()

# --/ !!! >
# --[ This class stores student account information.
# --[ allow_multiple_households is False by default as most students only belong to one household at a time.     
class User(Base):
    __tablename__ = "users"

    id                          = Column(Integer, primary_key=True)
    username                    = Column(String(50),  unique=True, nullable=False)
    email                       = Column(String(255), unique=True, nullable=False)
    password_hash               = Column(String(255), nullable=False)
    name                        = Column(String(100), nullable=False)
    allow_multiple_households   = Column(Boolean, default=False, nullable=False)
    is_active                   = Column(Boolean, default=True,  nullable=False)
    created_at                  = Column(DateTime, server_default=func.now())
    last_active_at              = Column(DateTime, onupdate=func.now())

# --/ !!! >
# --[ This class represents a shared student property, like an apartment or dorm room
# --[ A household groups students together for expense tracking
# --[ created_by stores the user who set the household up
class Household(Base):
    __tablename__ = "households"

    id                          = Column(Integer, primary_key=True)
    name                        = Column(String(100), nullable=False)
    address                     = Column(String(255))
    created_by                  = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at                  = Column(DateTime, server_default=func.now())
    is_active                   = Column(Boolean, default=True, nullable=False)