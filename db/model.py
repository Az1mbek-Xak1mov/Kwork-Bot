from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import BIGINT, String, Text, Integer, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.engine import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(BIGINT)
    fullname: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())



class Meal(Base):
    __tablename__ = "meals"
    name: Mapped[str] = mapped_column(String(100))
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    price: Mapped[str] = mapped_column(String(20))
    count:Mapped[int] = mapped_column(BIGINT)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())


class Salat(Base):
    __tablename__ = "salats"

    name: Mapped[str] = mapped_column(String(100))
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    price: Mapped[str] = mapped_column(String(20))
    count:Mapped[int] = mapped_column(BIGINT)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())


class Fast_Food(Base):
    __tablename__ = "fast_foods"
    name: Mapped[str] = mapped_column(String(100))
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    price: Mapped[str] = mapped_column(String(20))
    count:Mapped[int] = mapped_column(BIGINT)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(BIGINT)
    name: Mapped[str] = mapped_column(String(100))
    total_price: Mapped[str] = mapped_column(String(20))
    count:Mapped[int] = mapped_column(BIGINT)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())