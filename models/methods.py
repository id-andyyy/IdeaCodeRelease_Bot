from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from config_data.config import load_config, Config
from models.models import User

config: Config = load_config(r'.env')
engine: AsyncEngine = create_async_engine(
    f'sqlite+aiosqlite:///{config.db.db_name}.db')
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def create_user(tg_id: int, group_name: str, group_id: int) -> bool:
    async with async_session() as session:
        async with session.begin():
            new_user = User(tg_id=tg_id, group_name=group_name,
                            group_id=group_id)
            session.add(new_user)
            try:
                await session.commit()
                return True
            except IntegrityError:
                await session.rollback()
                return False


async def get_user_group(tg_id: int) -> dict[str, int | str] | None:
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User.group_id, User.group_name).where(User.tg_id == tg_id))
            user_group = result.first()
            if user_group:
                return {'group_id': user_group[0], 'group_name': user_group[1]}
            return None


async def update_user_group(tg_id: int, group_name: str, group_id: int) -> bool:
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.tg_id == tg_id))
            user = result.scalar_one_or_none()
            if user:
                user.group_name = group_name
                user.group_id = group_id
                await session.commit()
                return True
            await create_user(tg_id, group_name, group_id)
            return True
