import pytest
import project0

from project0 import main
def test_fi():
    data = main.fetchincidents("https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-23_daily_arrest_summary.pdf")
    assert data is not None

