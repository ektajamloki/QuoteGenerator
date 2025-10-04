from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Life is what happens when you're busy making other plans. By John Lennon",
    "The purpose of our lives is to be happy. By Dalai Lama",
    "Get busy living or get busy dying. By Stephen King",
    "You have as much laughter as you have faith. By Martin Luther",
    "The only impossible journey is the one you never begin. By Tony Robbins"
]

@app.route("/quote")
def get_random_quote():
    return {"quote": random.choice(quotes)}

if __name__ == "__main__":
    app.run(debug=True)