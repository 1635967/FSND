import os
import psycopg2
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
con = psycopg2.connect(user = "PC", password = "admin", host = "127.0.0.1", port = "5432", database = "demo")
cur = con.cursor()
#
# rows = cur.execute("SELECT id FROM table2")
#
# for r in rows:
#     print(f"id {r[0]}")
#
# cur.close()
# con.close()

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = '127.0.0.1'        #'<Put your local database url>'
