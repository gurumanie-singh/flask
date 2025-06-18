from flask import Flask
import json

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



if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = int("3000"), debug = True)