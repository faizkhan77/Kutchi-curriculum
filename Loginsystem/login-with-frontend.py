from colorama import Fore
from tqdm import tqdm
import time
import os
import mysql.connector

from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

conn = mysql.connector.connect(
    host="localhost",        # or your DB host
    user="root",             # your MySQL username
    password="root",# your MySQL password
    database="kutchitest"
)

cursor = conn.cursor()

@app.get("/", response_class=HTMLResponse)
def show_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": ""})

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    cursor.execute("SELECT user_id, password FROM credentials WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result:
        user_id, db_password = result
        if password == db_password:
            return templates.TemplateResponse("home.html", {"request": request, "user": username})
        else:
            return templates.TemplateResponse("login.html", {"request": request, "error": "Incorrect password."})
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "User not found."})

@app.get("/signup", response_class=HTMLResponse)
def show_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request, "error": ""})

@app.post("/register")
def register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...)
):
    cursor.execute("SELECT * FROM credentials WHERE username = %s", (username,))
    if cursor.fetchone():
        return templates.TemplateResponse("signup.html", {"request": request, "error": "User already exists."})
    
    cursor.execute("INSERT INTO credentials (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    user_id = cursor.lastrowid

    cursor.execute("INSERT INTO user_info (user_id, name, age, gender) VALUES (%s, %s, %s, %s)",
                   (user_id, name, age, gender))
    conn.commit()

    return RedirectResponse("/", status_code=302)
