import sqlite3
import os
# import pandas as pd


def get(q):
    db_folder = os.path.join('assets', 'database')
    conn = sqlite3.connect(os.path.join(db_folder, 'sqlite.db'))
    cur = conn.cursor()
    cur.execute(q)
    rows, columns = cur.fetchall(), [i[0] for i in cur.description]
    cur.close()
    return columns, rows

