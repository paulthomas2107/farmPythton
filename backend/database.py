from model import ToDo

import motor.motor_asyncio

# mongodb+srv://rest:Caitlin1966__@cluster0.8crs3.mongodb.net/test?authSource=admin&replicaSet=atlas-x7gn25-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://rest:Caitlin1966__@cluster0.8crs3.mongodb.net')
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(ToDo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document


async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True












