import asyncio
import datetime

import aiohttp
from more_itertools import chunked

from models import Session, SwapiPeople, init_orm

MAX_CHUNK = 10


async def get_people(person_id, session):
    async with session.get(
        f"https://swapi.py4e.com/api/people/{person_id}/"
    ) as response:
        json_data = await response.json()
        return json_data


async def insert_people(list_people_json, people_id_chunk):
    async with Session() as session:
        orm_objects = []
        for person, id_chunk in zip(list_people_json, people_id_chunk):
            if person == None:
                pass
            else:
                list_people_json = SwapiPeople(id=int(id_chunk),
                                birth_year=person['birth_year'],
                                eye_color=person["eye_color"],
                                films=person["films"],
                                gender=person["gender"],
                                hair_color=person["hair_color"],
                                height=person["height"],
                                homeworld=person["homeworld"],
                                mass=person["mass"],
                                name=person["name"],
                                skin_color=person["skin_color"],
                                species=person["species"],
                                starships=person["starships"],
                                vehicles=person["vehicles"])
                orm_objects.append(list_people_json)
        session.add_all(orm_objects)
        await session.commit()


async def main():
    await init_orm()
    async with aiohttp.ClientSession() as session:
        people_ids = chunked(range(1, 101), MAX_CHUNK)
        for people_ids_chunk in people_ids:
            print(people_ids_chunk)
            coros = [get_people(people_id, session) for people_id in people_ids_chunk]
            results = await asyncio.gather(*coros)
            asyncio.create_task(insert_people(results))

        main_task = asyncio.current_task()
        current_tasks = asyncio.all_tasks()
        current_tasks.remove(main_task)
        await asyncio.gather(*current_tasks)


start = datetime.datetime.now()
asyncio.run(main())
print(datetime.datetime.now() - start)
