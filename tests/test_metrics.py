import pandas as pd
from src.metrics import headcount, turnover_rate
from src.data_generator import generate_employees

def test_headcount_positive():
    df = generate_employees(100)
    assert headcount(df) > 0

def test_turnover_range():
    df = generate_employees(500)
    assert 0 <= turnover_rate(df) <= 1
