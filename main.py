from fitness_app import app

DEVELOPMENT_ENV = True

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080 ,debug=DEVELOPMENT_ENV)
    