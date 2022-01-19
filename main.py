from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
  """
  Return a friendly HTTP greeting
  """
  print("I am inside hello world")
  return "Hola mundo! Let's get this CD going!"

@app.route("/echo/<name>")
def echo(name):
  print("This was placed in the url: new- %s" % name)
  val = {"new-name": name}
  return jsonify(val)

if __name__ = "__main__":
  app.route(host="127.0.0.1", port=8080, debug=True)
