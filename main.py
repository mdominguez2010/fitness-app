###### IN PROCESS #########

from flask import Flask, render_template

DEVELOPMENT_ENV = True

app = Flask(__name__)


@app.route("/")
def index():
    # return render_template("index.html")
    return "<h1>Hello world!<h1>"
    
@app.route("/about/<username>")
def about_page(username):
    # return render_template("about.html")
    return f"<h1>This is the about page of {username}<h1>"

# @app.route("/about")
# def about():
#     return render_template("about.html", app_data=app_data)


# @app.route("/service")
# def service():
#     return render_template("service.html", app_data=app_data)


# @app.route("/contact")
# def contact():
#     return render_template("contact.html", app_data=app_data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=DEVELOPMENT_ENV)

########################### OLD FLASK APP ###############################

# from flask import Flask
# from flask import jsonify
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     """Return a friendly HTTP greeting."""
#     print("I am inside hello world")
#     return 'Hello World! CD, what is good in the hood dude?'

# @app.route('/echo/<name>')
# def echo(name):
#     print(f"This was placed in the url: new-{name}")
#     val = {"new-name": name}
#     return jsonify(val)

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8080, debug=True)
