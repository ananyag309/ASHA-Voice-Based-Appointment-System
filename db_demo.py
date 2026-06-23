from __future__ import annotations
from sqlalchemy import text
from database import engine, init_db

def run_sql(query: str):
    """ Run a raw SQL query on the same DB used by 'database.py'.

    Example:
        rows = run_sql("SELECT * FROM appointments")
        print(rows)

        new_count = run_sql("INSERT INTO appointments (patient_name, reason, start_time) VALUES ('Alice', 'Annual Checkup', '2022-01-01 10:00:00')")
        print(new_count)
    """
    #init_db()

    with engine.begin() as conn:
        result = conn.execute(text(query))
        return result.fetchall() if result.returns_rows else result.rowcount
query = """SELECT * FROM appointments"""

#query = """INSERT INTO appointments (patient_name, reason, start_time, canceled, created_at) VALUES ('Alice', 'Checkup', '2022-01-01 10:00:00',False,0)"""
print(run_sql(query))
  