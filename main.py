from flask import Flask, render_template
app = Flask(__name__)

DEVELOPMENT_ENV = True

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/progress')
def progress_page():
    items = [
        {'id': 1, 'name': 'Weight'},
        {'id': 2, 'name': 'Strength'},
        {'id': 3, 'name': 'Cardio'}
    ]
    return render_template('progress.html', items=items)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=DEVELOPMENT_ENV)