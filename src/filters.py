def apply_filters(df, department=None, location=None, level=None):
    if department and department != "All":
        df = df[df["department"] == department]
    if location and location != "All":
        df = df[df["location"] == location]
    if level and level != "All":
        df = df[df["level"] == level]
    return df
