import pytest
import requests
from faker import Faker
from pytest_steps import test_steps

fake = Faker()

def test_get_list():
   headers = {
       "Authorization": "pk_194601729_FY9YDRTPZ2F74KJ41BJ35AIODK6VATQE"
   }
   response = requests.get("https://api.clickup.com/api/v2/folder/90157056273/list", headers=headers)
   assert response.status_code == 200, f"Request failed with  body {response.text}"
   for list in response.json()["lists"]:
       print(list["id"])
       id = list["id"]


# def test_create_list():
#    headers = {
#        "Authorization": "pk_194601729_FY9YDRTPZ2F74KJ41BJ35AIODK6VATQE"
#    }
#    body = {
#        "name": fake.email()
#    }
#    response = requests.post("https://api.clickup.com/api/v2/folder/90157056273/list", headers=headers, json=body)
#    assert response.status_code == 201, f"Request failed with  body {response.text}"

def test_update_list():
   headers = {
       "Authorization": "pk_194601729_FY9YDRTPZ2F74KJ41BJ35AIODK6VATQE"
   }
   body = {
       "name": fake.email()
   }
   response = requests.put("https://api.clickup.com/api/v2/list/901511547171", headers=headers, json=body)
   assert response.status_code == 200, f"Request failed with  body {response.text}"

@pytest.mark.parametrize('parameter_name, status', [
       (fake.first_name(), 400),
       ("90157056273", 200),
       ('wqwd', 200)
   ])
def test_get_list(parameter_name, status):
   headers = {
       "Authorization": "pk_194601729_FY9YDRTPZ2F74KJ41BJ35AIODK6VATQE"
   }
   response = requests.get("https://api.clickup.com/api/v2/folder/" + parameter_name + "/list", headers=headers)
   assert response.status_code == status, f"Request failed with  body {response.text}"
   # for list in response.json()["lists"]:
   #     print(list["id"])
   #     id = list["id"]

@test_steps('Create a new list', 'Update a list')
def test_get_listStep():
   headers = {
       "Authorization": "pk_194601729_FY9YDRTPZ2F74KJ41BJ35AIODK6VATQE"
   }
   response = requests.get("https://api.clickup.com/api/v2/folder/90157056273/list", headers=headers)
   assert response.status_code == 200, f"Request failed with  body {response.text}"
   for list in response.json()["lists"]:
       print(list["id"])
       id = list["id"]
   headers = {
       "Authorization": "pk_194601729_FY9YDRTPZ2F74KJ41BJ35AIODK6VATQE"
   }
   yield
   response = requests.get("https://api.clickup.com/api/v2/folder/90157056273/list", headers=headers)
   assert response.status_code == 200, f"Request failed with  body {response.text}"
   for list in response.json()["lists"]:
       print(list["id"])
       id = list["id"]
   yield