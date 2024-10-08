import os

from sqlalchemy import JSON, String, Text
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_USER = os.getenv("POSTGRES_USER", "swapi")
POSTGRES_DB = os.getenv("POSTGRES_DB", "swapi")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRS_PORT = os.getenv("POSTGRES_PORT", "5431")

PG_DSN = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRS_PORT}/{POSTGRES_DB}"

engine = create_async_engine(PG_DSN)
Session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    pass


class SwapiPeople(Base):

    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    films: Mapped[str] = mapped_column(Text, nullable=True)
    eye_color: Mapped[str] = mapped_column(String(255), nullable=True)
    birth_year: Mapped[str] = mapped_column(String(255), nullable=True)
    species: Mapped[str] = mapped_column(String(255), nullable=True)
    skin_color: Mapped[str] = mapped_column(String(255), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    mass: Mapped[str] = mapped_column(String(255), nullable=True)
    homeworld: Mapped[str] = mapped_column(String(255), nullable=True)
    height: Mapped[str] = mapped_column(String(255), nullable=True)
    hair_color: Mapped[str] = mapped_column(String(255), nullable=True)
    gender: Mapped[str] = mapped_column(Text, nullable=True)
    starships: Mapped[str] = mapped_column(Text, nullable=True)
    vehicles: Mapped[str] = mapped_column(Text, nullable=True)


async def init_orm():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
