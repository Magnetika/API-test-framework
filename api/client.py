import requests

BASE_URL = "https://reqres.in/api"

class APIClient:
    def get_users(self, page=1):
        # page paraméter hozzáadása
        return requests.get(f"{BASE_URL}/users", params={"page": page})

    def create_user(self, data):
        return requests.post(f"{BASE_URL}/users", json=data)

    def update_user(self, user_id, data):
        return requests.put(f"{BASE_URL}/users/{user_id}", json=data)

    def delete_user(self, user_id):
        return requests.delete(f"{BASE_URL}/users/{user_id}")