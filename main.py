###### IN DEVELOPMENT #########

from flask import Flask, render_template

DEVELOPMENT_ENV = True

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")
    
@app.route("/progress")
def progress():
    return render_template("progress.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=DEVELOPMENT_ENV)