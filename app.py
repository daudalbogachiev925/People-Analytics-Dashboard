import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_generator import generate_employees
from src.kpis import compute_kpis
from src.filters import apply_filters
from src.metrics import headcount_by_department

st.set_page_config(page_title="People Analytics Dashboard", layout="wide")
st.title("📊 People Analytics Dashboard")

@st.cache_data
def load():
    try:
        return pd.read_csv("data/employees.csv")
    except FileNotFoundError:
        df = generate_employees()
        df.to_csv("data/employees.csv", index=False)
        return df

df = load()

st.sidebar.header("Фильтры")
dept = st.sidebar.selectbox("Department", ["All"] + sorted(df["department"].unique()))
loc = st.sidebar.selectbox("Location", ["All"] + sorted(df["location"].unique()))
lvl = st.sidebar.selectbox("Level", ["All"] + sorted(df["level"].unique()))

filtered = apply_filters(df, dept, loc, lvl)
kpis = compute_kpis(filtered)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Headcount", kpis["headcount"])
c2.metric("Turnover", f"{kpis['turnover_rate']}%")
c3.metric("Retention", f"{kpis['retention_rate']}%")
c4.metric("Avg Tenure", f"{kpis['avg_tenure_years']} лет")

st.subheader("Headcount по департаментам")
hc = headcount_by_department(filtered)
st.bar_chart(pd.Series(hc))

st.subheader("Распределение зарплат")
fig = px.histogram(filtered, x="salary", color="level", nbins=40)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Diversity по полу")
div = filtered[filtered["is_active"]]["gender"].value_counts()
st.plotly_chart(px.pie(values=div.values, names=div.index), use_container_width=True)

st.subheader("Performance vs Engagement")
fig2 = px.scatter(filtered, x="engagement_score", y="performance_score",
                  color="department", size="salary", hover_data=["employee_id"])
st.plotly_chart(fig2, use_container_width=True)
