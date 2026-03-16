from api.client import APIClient
from jsonschema import validate

client = APIClient()

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"}
    },
    "required": ["id", "email", "first_name", "last_name", "avatar"]
}

def test_get_users_contract():
    response = client.get_users(page=1)  # page=1 hozzáadva
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    
    json_response = response.json()
    assert "data" in json_response, "Missing 'data' in response"
    
    data = json_response["data"][0]
    validate(instance=data, schema=user_schema)