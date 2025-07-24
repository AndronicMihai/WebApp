import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():
    conn = mysql.connector.connect(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )
    return conn
