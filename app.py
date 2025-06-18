from flask import Flask, request
import json, os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the main page <h1>HELLO</h1>"

@app.route("/<name>")
def birthday(name):
    with open("birthdays.txt") as f:
        birthdays = json.load(f)
    with open("information.txt") as g:
        information = json.load(g)

    birthday = birthdays[name]
    origin = information[name]["origin"]
    current_residence = information[name]["current_residence"]

    return f"Your name is {name} and your birthday is on {birthday}. \
             You are from {origin} and stay at {current_residence}."

# Add a new user to information.txt
@app.route("/add_information", methods=["POST"])
def information():
    data = request.get_json()
    username = data.get("username")
    origin = data.get("origin")
    current_residence = data.get("current_residence")

    # Load existing information
    if os.path.exists("information.txt"):
        with open("information.txt", "r") as f:         # read mode
            info = json.load(f)
    else:
        info = {}

    # Update data
    info[username] = {
        "origin": origin,
        "current_residence": current_residence
    }

    # Write back to file
    with open("information.txt", "w") as f:             # write mode
        json.dump(info, f, indent=4)

    return f"User '{username}' added successfully!", 200


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = int("3000"), debug = True)