# tests/test_extract.py

from code.extract import get_cost_of_living

def test_get_cost_of_living():
    result = get_cost_of_living("Dallas")
    assert result["rent"] == 1400
    assert result["groceries"] == 300
    assert result["transport"] == 100
    assert result["total_estimate"] == 1800

def test_get_cost_of_living_unknown_city():
    result = get_cost_of_living("Nowhere")
    assert result["rent"] is None
    assert result["total_estimate"] == 0  # Since it skips None
