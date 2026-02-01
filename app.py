import os
from flask import Flask, render_template, request
from pymongo import MongoClient
import random

app = Flask(__name__)

# Use environment variable for MongoDB URI, fallback to default for local testing
mongo_uri = os.environ.get("MONGO_URI", "mongodb://admin:admin123@mongodb:27017/gameDB?authSource=admin")
client = MongoClient(mongo_uri)
db = client.guessdb
collection = db.guesses

SECRET_NUMBER = random.randint(1, 10)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        print("POST RECEIVED")
        print("FORM DATA:", request.form)

        guess = request.form.get("guess")

        if not guess:
            return "No guess received", 400

        try:
            guess_int = int(guess)
            print("GUESS INT:", guess_int)

            collection.insert_one({"guess": guess_int})
            print("Inserted into Mongo")

            if guess_int == SECRET_NUMBER:
                message = "🎉 Correct!!"
            elif guess_int < SECRET_NUMBER:
                message = "📉 Too low!!"
            else:
                message = "📈 Too high!!"

        except Exception as e:
            print("ERROR:", e)
            return f"Error occurred: {e}", 500

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
