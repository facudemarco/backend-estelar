from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

def getConnection():
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
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None

def getConnectionForLogin():
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
        return connection
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None