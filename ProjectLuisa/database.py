import os
import psycopg2
from ProjectLuisa import config

conn = psycopg2.connect(config.DATABASE_URL, sslmode='require')


# SQL queriess


def get_salmonella():
    cur = conn.cursor()
    cur.execute("""SELECT * FROM salmonella;""")
    rows = cur.fetchall()
    return rows


def get_escherichia():
    cur = conn.cursor()
    cur.execute("""SELECT * FROM escherichia;""")
    rows = cur.fetchall()
    return rows


def get_klebsiella():
    cur = conn.cursor()
    cur.execute("""SELECT * FROM klebsiella;""")
    rows = cur.fetchall()
    return rows
