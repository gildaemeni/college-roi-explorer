from code.extract import get_cost_of_living, extract_salary_data
from code.api_calls import call_entity_recognition

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
def test_extract_salary_data_final():
    df = extract_salary_data(
        "cache/raw/Most-Recent-Cohorts-Field-of-Study.csv",
        "cache/raw/Most-Recent-Cohorts-Institution.csv"
    )
    assert not df.empty
    assert all(col in df.columns for col in ['school', 'state', 'major', 'degree', 'post_grad_earnings'])
    assert df['post_grad_earnings'].dtype == float


def test_entity_recognition_returns_list():
    text = "Barack Obama was born in Hawaii and served as the President of the United States."
    result = call_entity_recognition(text)
    
    assert isinstance(result, list)  # Should return a list
    assert all("text" in entity for entity in result) or result == []  # Valid entity structure or empty