from datetime import datetime, timezone, timedelta

from app.database.database import async_session
from app.database.database import WashingMachine
from sqlalchemy import select, update


def get_time():
    offset = timedelta(hours=3)
    msk_tz = timezone(offset, name='MSK')
    return datetime.now(tz=msk_tz).strftime("%Y-%m-%d %H:%M")


async def add_machine(dorm_number, machine_number):
    machine = await get_machine(dorm_number, machine_number)
    if not machine:
        async with async_session() as session:
            session.add(WashingMachine
                (
                dorm_number=dorm_number,
                number=machine_number,
                time=get_time(),
                status=1
            )
            )
            await session.commit()



async def get_machine(dorm_number, machine_number):
    async with async_session() as session:
        machine = await session.scalar(select(WashingMachine)
                                       .where(WashingMachine.number == machine_number)
                                       .where(WashingMachine.dorm_number == dorm_number))
        return machine


async def update_machine(dorm_number, machine_number, status):
    async with (async_session() as session):
        stmp = (
            update(WashingMachine)
            .where(WashingMachine.number == machine_number)
            .where(WashingMachine.dorm_number == dorm_number)
            .values(status=status)
            .values(time=get_time())
        )
        await session.execute(stmp)
        await session.commit()
