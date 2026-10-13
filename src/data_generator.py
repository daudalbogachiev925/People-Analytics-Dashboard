import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_employees(n=2000, seed=42):
    np.random.seed(seed)
    departments = ["Engineering", "Sales", "Marketing", "HR", "Finance", "Support", "Product"]
    levels = ["Junior", "Middle", "Senior", "Lead", "Manager", "Director"]
    locations = ["Moscow", "Berlin", "London", "Remote", "New York"]
    genders = ["M", "F", "Other"]

    rows = []
    for i in range(n):
        hire_date = datetime(2018, 1, 1) + timedelta(days=int(np.random.randint(0, 2500)))
        tenure_days = (datetime(2025, 1, 1) - hire_date).days
        is_active = np.random.random() > 0.15
        termination_date = None
        if not is_active:
            termination_date = hire_date + timedelta(days=int(np.random.randint(90, tenure_days)))
        salary = int(np.random.normal(120000, 40000))
        rows.append({
            "employee_id": f"EMP{i:05d}",
            "department": np.random.choice(departments),
            "level": np.random.choice(levels),
            "location": np.random.choice(locations),
            "gender": np.random.choice(genders, p=[0.55, 0.42, 0.03]),
            "age": int(np.random.normal(33, 8)),
            "hire_date": hire_date.date().isoformat(),
            "termination_date": termination_date.date().isoformat() if termination_date else None,
            "salary": max(salary, 30000),
            "performance_score": round(np.random.normal(3.5, 0.7), 2),
            "engagement_score": round(np.random.uniform(1, 10), 1),
            "manager_id": f"EMP{np.random.randint(0, 200):05d}",
            "is_active": is_active,
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = generate_employees()
    df.to_csv("data/employees.csv", index=False)
    print(f"Generated {len(df)} employees")
