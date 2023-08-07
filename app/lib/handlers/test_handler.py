from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.schemas.test_schemas import EventsSchema
from app.setting import get_settings
from app.lib.postgres.models import Events

settings = get_settings()


connection = f'postgresql+asyncpg://{settings.POSTGRESQL_USER}:{settings.POSTGRESQL_PASS}@localhost/{settings.POSTGRESQL_DB}'
engine = create_async_engine(connection, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)



async def create_event(event: EventsSchema) -> Events:
    async with async_session() as session:
        new_event = Events(title=event.title,
                           description=event.description,
                           datetime=event.datetime.replace(tzinfo=None))
        session.add(new_event)
        await session.commit()

        return new_event


async def get_events() -> List[Events]:
    async with async_session() as session:
        stmt = select(Events)
        result = await session.execute(stmt)
        events = result.scalars().all()
        return events