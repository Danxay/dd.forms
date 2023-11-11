from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import sqlite3

app = FastAPI()

origins = [
    "https://dd-forms-danxay.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

con = sqlite3.connect("../bot/data.db")
cursor = con.cursor()

app.mount("/images", StaticFiles(directory="../bot/photo"), name="images")

@app.get("/card/{id}")
async def get_data(id: int):
    cursor.execute(f"SELECT * FROM data WHERE id = {id}")
    result = cursor.fetchone()
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
