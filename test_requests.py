import requests

# GET request to find out information about user
response = requests.get("http://localhost:3000/Taimoor")
print("Response:", response.text)

# POST request to send information
data = {
    "username": "NewGuy",
    "origin": "India",
    "current_residence": "Maple Hall"
}
post_response = requests.post("http://localhost:3000/add_information", json=data)
print("POST Response:", post_response.text)