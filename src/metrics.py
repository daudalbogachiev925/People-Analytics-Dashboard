import pandas as pd
import numpy as np
from datetime import datetime

def headcount(df, date=None):
    date = pd.Timestamp(date) if date else pd.Timestamp.today()
    df = df.copy()
    df["hire_date"] = pd.to_datetime(df["hire_date"])
    df["termination_date"] = pd.to_datetime(df["termination_date"], errors="coerce")
    active = df[(df["hire_date"] <= date) & ((df["termination_date"].isna()) | (df["termination_date"] > date))]
    return len(active)

def turnover_rate(df, year=2024):
    df = df.copy()
    df["termination_date"] = pd.to_datetime(df["termination_date"], errors="coerce")
    term = df[df["termination_date"].dt.year == year]
    avg_hc = headcount(df)
    return len(term) / avg_hc if avg_hc > 0 else 0

def retention_rate(df, cohort_year=2023):
    df = df.copy()
    df["hire_date"] = pd.to_datetime(df["hire_date"])
    df["termination_date"] = pd.to_datetime(df["termination_date"], errors="coerce")
    cohort = df[df["hire_date"].dt.year == cohort_year]
    if len(cohort) == 0:
        return 0
    still = cohort[cohort["termination_date"].isna() | (cohort["termination_date"] > pd.Timestamp.today())]
    return len(still) / len(cohort)

def avg_tenure(df):
    df = df.copy()
    df["hire_date"] = pd.to_datetime(df["hire_date"])
    df["termination_date"] = pd.to_datetime(df["termination_date"], errors="coerce").fillna(pd.Timestamp.today())
    df["tenure_years"] = (df["termination_date"] - df["hire_date"]).dt.days / 365
    return df["tenure_years"].mean()

def headcount_by_department(df):
    return df[df["is_active"]].groupby("department").size().to_dict()

def diversity_ratio(df, column="gender"):
    active = df[df["is_active"]]
    return active[column].value_counts(normalize=True).to_dict()

def cost_per_hire(total_recruiting_cost=500000, hires=25):
    return total_recruiting_cost / hires if hires else 0
