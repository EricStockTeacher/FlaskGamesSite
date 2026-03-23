from flask import Flask, render_template, request, session, flash
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = "filesystem"

Session(app)

#app.secret_key = "mysecretkey"
#games = {}

@app.route('/')
def hello_world():
    if "games" not in session:
        flash("Welcome to the site, please add a game to get started!!")
    return render_template("main.html")

@app.route('/data' )
def enter_data():
    return render_template('game.html')

@app.route('/greet', methods=['POST'])
def greet_user():
    game_name = request.form['game']
    platform = request.form['platform']
    value = request.form['value']
    year = request.form['year']

    if "games" in session:
        session["games"][game_name] = {'platform':platform, 'value':value, 'year':year}
    else:
        session["games"] = {}
        session["games"][game_name] = {'platform': platform, 'value': value, 'year': year}

    flash(f"Game {game_name} added!!")
    #session[game_name] = {'platform':platform, 'value':value, 'year':year}
    return render_template('game.html')

@app.route('/display')
def display():
    print(session)
    return render_template('display.html', games=session.get("games", {}))

if __name__ == "__main__":
    app.run(host='0.0.0.0')