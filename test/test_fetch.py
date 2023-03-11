import pytest
import project0
import sqlite3
from project0 import functions


def test_fi():
   data = functions.fetchincidents('https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-23_daily_arrest_summary.pdf')
   assert data is not None




