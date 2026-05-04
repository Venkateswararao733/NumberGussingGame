from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def home():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0

    message = ""

    if request.method == "POST":
        guess = int(request.form.get("guess"))
        session["attempts"] += 1

        if guess < session["number"]:
            message = "Too low!"
        elif guess > session["number"]:
            message = "Too high!"
        else:
            message = f"🎉 Correct! Attempts: {session['attempts']}"
            session.pop("number", None)
            session.pop("attempts", None)

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)