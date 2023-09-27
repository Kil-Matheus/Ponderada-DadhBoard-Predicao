from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import pandas as pd
import uvicorn
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import jwt
from datetime import datetime, timedelta
import psycopg2
import teste
import subprocess
import streamlit as st
from time import sleep
import streamlit as st

# Connect to database
db_conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="senha",
    host="db",
    port="5432"
)

SECRET_KEY = '96195d62f35e6015ca2ac7e676ad3377'
ALGORITHM = 'HS256'

# Create the app
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request):
    try:
        data = await request.json()
        username = data.get("username")
        password = data.get("password")
        print(username, password)

        db_conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="senha",
            host="db",
            port="5432"
            )
        
        cursor = db_conn.cursor()
        cursor.execute(f"SELECT * FROM usuario WHERE username='{username}' AND senha='{password}'")
        db_conn.commit()
        result = cursor.fetchone()
        
        if result is not None:
            payload = {
                "user": username,
                "exp": datetime.utcnow() + timedelta(seconds=30)
            }
            jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
            return {"access_token": jwt_token}
        else:
            return {"error": "Invalid username or password"}
        
    except psycopg2.Error as e:
        raise Exception(f'Erro ao selecionar: {e}')
    
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    subprocess.Popen(["streamlit", "run", "teste.py"])
    return """
        <html>
            <head>
            </head>
            <body>
                <iframe src="http://localhost:8501" width="100%" height="600"></iframe>
            </body>
        </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)