from flask import Flask, render_template


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 31536000


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/merida")
def merida():
    return render_template("merida.html")
