import pytest
from api.client import APIClient
from faker import Faker

client = APIClient()
faker = Faker()

def test_get_users():
    response = client.get_users()
    assert response.status_code == 200
    assert "data" in response.json()

def test_create_user():
    user_data = {
        "name": faker.name(),
        "job": faker.job()
    }
    response = client.create_user(user_data)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == user_data["name"]
    assert json_data["job"] == user_data["job"]