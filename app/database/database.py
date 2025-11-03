from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from app.config import settings


DATABASE_URL = settings.get_sqlite_url()

engine = create_async_engine(url=DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


class WashingMachine(Base):
    __tablename__ = "washing_machines"

    id: Mapped[int] = mapped_column(primary_key=True)
    dorm_number: Mapped[int]
    number: Mapped[int]
    status: Mapped[int]
    time: Mapped[str]


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
