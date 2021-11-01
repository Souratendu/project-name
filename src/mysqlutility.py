import mysql.connector

USER = ''
HOST = ''
PASSWORD = ''
DATABASE = ''

def get_connection():
    cnx = mysql.connector.connect(user=USER, password=PASSWORD,
                                host=HOST,
                                database=DATABASE)
    return cnx

def close_connection(cnx):
    cnx.close()