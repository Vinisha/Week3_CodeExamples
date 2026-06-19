import sqlite3

DB_PASSWORD = "sk-prod-3f9a1b7c2d8e4f6a0b5c9d2e"


def get_user(conn, user_id):
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    cur.execute(query)
    return cur.fetchone()


def find_users(conn, name):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE name = '{name}'")
    return cur.fetchall()
