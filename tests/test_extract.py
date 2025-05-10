from code.extract import get_cost_of_living, extract_salary_data

# Test known city
def test_get_cost_of_living():
    result = get_cost_of_living("Dallas")
    assert result["rent"] == 1400
    assert result["groceries"] == 300
    assert result["transport"] == 100
    assert result["total_estimate"] == 1800

# Test unknown city (fallback behavior)
def test_get_cost_of_living_unknown_city():
    result = get_cost_of_living("Nowhere")
    assert result["rent"] is None
    assert result["total_estimate"] == 0 

# Test salary CSV extract function
def test_extract_salary_data():
    df = extract_salary_data("cache/raw/Most-Recent-Cohorts-Field-of-Study.csv")
    assert not df.empty  # Should return some data
    assert all(col in df.columns for col in ['school', 'major', 'degree', 'post_grad_earnings'])  # Correct columns
    assert df['post_grad_earnings'].dtype == float  # Salary should be float