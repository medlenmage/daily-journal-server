from models.entries import Entries
import sqlite3
import json

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.concept,
            a.entry,
            a.date,
            a.moodId
        FROM entries a
        """)


        entries = []


        dataset = db_cursor.fetchall()


        for row in dataset:

            entry = Entries(row['id'], row['concept'], row['entry'], row['date'], row['moodId'])

            entries.append(entry.__dict__)

    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.concept,
            a.entry,
            a.date,
            a.moodId
        FROM entries a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        entry = Entries(data['id'], data['concept'],
                            data['entry'], data['date'],
                            data['moodId'])

        return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))
