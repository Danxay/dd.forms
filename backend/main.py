import sqlite3
from contextlib import closing

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

origins = [
    "https://dd-forms-danxay.vercel.app",
    "https://dd-forms.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory="../bot/photo"), name="images")


@app.get("/card/{id}")
async def get_data(id: int):
    with closing(sqlite3.connect("../bot/data.db")) as con, con, \
            closing(con.cursor()) as cur:
        cur.execute(f"SELECT * FROM data WHERE id = {id}")
        result = cur.fetchone()
        response = {
            'id': result[0],
            'fullname': result[1],
            'telegram': result[2],
            'vk': result[3],
            'contact': result[4],
            'type': result[5],
            'bio': result[6],
        }
        return response

# uvicorn main:app --host 0.0.0.0 --port 8888
