import sqlite3
from project0.functions import createdb

def test_createdb():
    # Call the function
    createdb()

    # Verify that the table has been created
    db_connect = sqlite3.connect('normanpd.db')
    db = db_connect.cursor()
    db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='incidents'")
    result = db.fetchone()
    assert result[0] == 'incidents'

    # Verify that the table is empty
    db.execute("SELECT COUNT(*) FROM incidents")
    result = db.fetchone()
    assert result[0] == 0

    # Close the connection
    db_connect.close()
