from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from databases import Database

app = FastAPI()
# database = Database("sqlite:///data.db")

app.mount("/images", StaticFiles(directory="../bot/photo"), name="images")

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

@app.get("/card/{id}")
async def get_data(id: int):
    query = "SELECT * FROM data"
    # results = await database.fetch_all(query=query)
    data = {id: id}
    return data

# uvicorn main:app --host 0.0.0.0 --port 8888
