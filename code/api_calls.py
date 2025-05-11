import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def call_entity_recognition(text: str) -> list:
    """
    Calls the CENT API's Azure entity recognition service and returns entities.
    """
    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    headers = {
        "x-api-key": os.getenv("CENT_API_KEY"),
        "Content-Type": "application/json"
    }

    # This is the CORRECT Azure-style payload CENT expects
    payload = {
        "documents": [
            {
                "id": "1",
                "language": "en",
                "text": text
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        try:
            entities = data["results"]["documents"][0]["entities"]
            return entities
        except Exception as e:
            print("Valid API call but no entities returned:", e)
            return []
    else:
        raise Exception(f"API call failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    text = "Syracuse University is located in New York and has strong data programs."
    print(f"Text being sent: '{text}'")

    entities = call_entity_recognition(text)
    print(entities)

    if entities:
        df = pd.DataFrame(entities)
        df.to_csv("cache/cleaned/api_entities.csv", index=False)
        print("✅ Entities saved to cache/cleaned/api_entities.csv")
    else:
        print("⚠️ No entities to save.")
