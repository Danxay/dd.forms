from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import uvicorn



class App:

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
        while True:
        try:
            con = sqlite3.connect("../bot/data.db")
            cursor = con.cursor()
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
            con.close()
            return response
            break

app = App()

uvicorn.run("main:app", host="0.0.0.0", port=300, log_level="info")

# uvicorn main:app --host 0.0.0.0 --port 8888
