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

def extract_salary_data(csv_path: str) -> pd.DataFrame:
    """
    Reads the College Scorecard Field-of-Study CSV,
    filters to tech majors, and returns cleaned DataFrame.
    """
    df = pd.read_csv(csv_path, low_memory=False)

    # Filter to only tech-related majors
    tech_keywords = ['computer', 'data', 'information', 'informatics', 'technology']
    df = df[df['CIPDESC'].str.lower().str.contains('|'.join(tech_keywords), na=False)]

    # Select only relevant columns, including degree
    df = df[['INSTNM', 'CIPDESC', 'CREDDESC', 'EARN_MDN_5YR']].copy()
    df.columns = ['school', 'major', 'degree', 'post_grad_earnings']

    # Clean the earnings column
    df = df[df['post_grad_earnings'].apply(lambda x: str(x).replace('.', '', 1).isdigit())]
    df['post_grad_earnings'] = df['post_grad_earnings'].astype(float)

    return df

# Test Functions 
if __name__ == "__main__":
    # Salary Data
    df = extract_salary_data("cache/raw/Most-Recent-Cohorts-Field-of-Study.csv")
    print(df.head())
    df.to_csv("cache/cleaned/salary_data.csv", index=False)

    # Cost of Living (mocked)
    print(get_cost_of_living("Syracuse"))