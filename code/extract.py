import pandas as pd
# Cost Data (mocked)
def get_cost_of_living(city: str) -> dict:
    """
    Get the cost of living in a city
    """
    sample_data = {
    "Syracuse": {"rent": 1100, "groceries": 350, "transport": 120},
    "Dallas": {"rent": 1400, "groceries": 300, "transport": 100},
    "Atlanta": {"rent": 1500, "groceries": 320, "transport": 110}
    }

    data = sample_data.get(city, {"rent": None, "groceries": None, "transport": None})
    total = sum(v for v in data.values() if v)
    return {
        "city": city,
        "rent": data["rent"],
        "groceries": data["groceries"],
        "transport": data["transport"],
        "total_estimate": total
    }

def extract_salary_data(field_csv: str, inst_csv: str) -> pd.DataFrame:
    """
    Merge field of study data with institution-level data to get state info.
    """
    # Load both files
    field_df = pd.read_csv(field_csv, low_memory=False)
    inst_df = pd.read_csv(inst_csv, usecols=['UNITID', 'INSTNM', 'STABBR'])

    # Filter tech majors
    tech_keywords = ['computer', 'data', 'information', 'informatics', 'technology']
    field_df = field_df[field_df['CIPDESC'].str.lower().str.contains('|'.join(tech_keywords), na=False)]

    # Merge on UNITID to get STABBR (state)
    merged = pd.merge(field_df, inst_df, on='UNITID', how='left')

    # Select final columns
    merged = merged[['INSTNM_y', 'STABBR', 'CIPDESC', 'CREDDESC', 'EARN_MDN_5YR']].copy()
    merged.columns = ['school', 'state', 'major', 'degree', 'post_grad_earnings']

    # Clean salary column
    merged = merged[merged['post_grad_earnings'].apply(lambda x: str(x).replace('.', '', 1).isdigit())]
    merged['post_grad_earnings'] = merged['post_grad_earnings'].astype(float)

    return merged

# Test Functions 
if __name__ == "__main__":
    df = extract_salary_data(
        "cache/raw/Most-Recent-Cohorts-Field-of-Study.csv",
        "cache/raw/Most-Recent-Cohorts-Institution.csv"
    )
    print(df.head())
    df.to_csv("cache/cleaned/salary_data.csv", index=False)