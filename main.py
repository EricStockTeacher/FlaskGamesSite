from flask import Flask, render_template, request

app = Flask(__name__)

games = {}

@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/data' )
def enter_data():
    return render_template('game.html')

@app.route('/greet', methods=['POST'])
def greet_user():
    name = request.form['username']
    game = request.form['game']
    games[name] = game
    return render_template('greet.html', name=name, game=game)

@app.route('/storage')
def storage():
    return render_template('storage.html', games=games)

if __name__ == "__main__":
    app.run(host='0.0.0.0')