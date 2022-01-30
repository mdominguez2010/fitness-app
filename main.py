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

    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]

    return render_template("progress.html", items=items)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=DEVELOPMENT_ENV)