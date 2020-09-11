from flask import Flask, request

app= Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def result_bot():
    return "you are infected!"