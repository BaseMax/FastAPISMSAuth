import sys
import requests

# token = "71e35620-1c80-4bda-bf5f-3dd9a5c67747"
# token = "71e35620-1c80-4bda-bf5f-3dd9a5c67747xxxxxx"
# headers = {"X-Token": token}
# response = requests.get("http://localhost:8000/panel", headers=headers)
# print(response.json())
# sys.exit(1)

# define the user data
phone_number = "09153221677"
user_data = {"name": "John Doe", "phone_number": phone_number, "city": "New York"}

# register a new user
response = requests.post("http://localhost:8000/register", json=user_data)
print(response.json())

# login with the user's phone number
login_data = {"phone_number": phone_number}
response = requests.post("http://localhost:8000/login", json=login_data)
print(response.json())

# auth with the user's phone number and verify code
while True:
    verify_code = input("Enter verify code: ")

    # send the verify code to the server
    auth_data = {"phone_number": phone_number, "verify_code": verify_code}
    response = requests.post("http://localhost:8000/auth", json=auth_data)
    print(response.json())

    if response.status_code != 200:
        continue

    # access the user's panel
    token = response.json()["token"]

    headers = {"X-Token": token}
    response = requests.get("http://localhost:8000/panel", headers=headers)
    print(response.json())

    headers = {"X-Token": token}
    response = requests.get("http://localhost:8000/whoiam", headers=headers)
    print(response.json())

    response = requests.get("http://localhost:8000/hi", headers=headers)
    print(response.json())
    break
