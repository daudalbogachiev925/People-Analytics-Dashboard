from src.metrics import (
    headcount, turnover_rate, retention_rate, avg_tenure,
    diversity_ratio, cost_per_hire
)

def compute_kpis(df):
    return {
        "headcount": headcount(df),
        "turnover_rate": round(turnover_rate(df) * 100, 2),
        "retention_rate": round(retention_rate(df) * 100, 2),
        "avg_tenure_years": round(avg_tenure(df), 2),
        "gender_diversity": {k: round(v * 100, 1) for k, v in diversity_ratio(df, "gender").items()},
        "cost_per_hire": round(cost_per_hire(), 2),
    }
