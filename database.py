import sqlite3

DB_NAME = "analysis.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analyses(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        query TEXT,

        result TEXT,

        status TEXT

    )
    """)

    conn.commit()

    conn.close()


def create_record(filename, query):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(

        "INSERT INTO analyses(filename,query,status) VALUES(?,?,?)",

        (filename, query, "processing")

    )

    record_id = cursor.lastrowid

    conn.commit()

    conn.close()

    return record_id


def update_result(record_id, result):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(

        "UPDATE analyses SET result=?, status=? WHERE id=?",

        (result, "completed", record_id)

    )

    conn.commit()

    conn.close()


def get_result(record_id):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM analyses WHERE id=?",

        (record_id,)

    )

    row = cursor.fetchone()

    conn.close()

    return row