import pandas as pd
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

# Quick test
if __name__ == "__main__":
    print(get_cost_of_living("Syracuse"))
