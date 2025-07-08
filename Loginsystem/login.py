from colorama import Fore
from tqdm import tqdm
import time
import os
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",        # or your DB host
    user="root",             # your MySQL username
    password="root",# your MySQL password
    database="kutchitest"
)

cursor = conn.cursor()

def login(username, password):
    cursor.execute("SELECT user_id, password FROM credentials WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        user_id, db_password = result
        if password == db_password:
            Home(user=username, status="login")
        else:
            return "Username matched but password is incorrect"
    else:
        return "User does not exist. Please register first."


def register(username, password):
    # Check if user already exists
    cursor.execute("SELECT * FROM credentials WHERE username = %s", (username,))
    if cursor.fetchone():
        print(Fore.RED + "User already exists! Please login instead.")
        return

    # Insert into credentials
    cursor.execute("INSERT INTO credentials (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()

    user_id = cursor.lastrowid  # Get the new user's ID

    # print(user_id)

    # Ask for additional info
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")

    # Insert into user_info
    cursor.execute("INSERT INTO user_info (user_id, name, age, gender) VALUES (%s, %s, %s, %s)",
                   (user_id, name, age, gender))
    conn.commit()

    print(Fore.GREEN + f"Registration successful! Welcome {username} :)")
    Home(user=username, status="register")


def Home(user, status, show_loading=True):
    if show_loading:
        for i in tqdm(range(1, 10)):
            time.sleep(0.1)
    
    if status == "login":
        print(Fore.GREEN + f"WELCOME BACK {user} TO THE HOME PAGE")
    else:
        print(Fore.GREEN + f"Signin Successful, Welcome {user} to our website :)")

    print("This is my content bro")

    logout = input("Logout? ")

    if logout.lower() in ["y", "yes"]:
        print("logging out...")
        os._exit(status=0)
    else:
        print("ok 🙂")
        # Call Home again without loading next time
        Home(user=user, status=status, show_loading=False)


while True:
    print("Choose one")
    print("1. Login")
    print("2. Register")

    user = int(input(">> "))

    if user == 1:
        print("Login page")
        user_username = input("Enter Username: ")
        user_password = input("Enter Password: ")

        x = login(username=user_username, password=user_password)
        if x:
            print(x)

    elif user == 2:
        print("Signup page")
        user_username = input("Enter Username: ")
        user_password = input("Enter Password: ")
        register(username=user_username, password=user_password)

    else:
        print("Sorry, invalid input")