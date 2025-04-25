import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    config = {
        'user': os.getenv('USER'),
        'password': os.getenv('PASSWORD'),
        'host': os.getenv('HOST'),
        'database': os.getenv('DATABASE'),
        'raise_on_warnings': True,
        'port': os.getenv('PORT')
    }

    try:
        connection = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        return None

if __name__ == "__main__":
    conn = get_connection()
    if conn:
        conn.close()
