from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/check' )
def enter_data():
    return render_template('check.html')

@app.route('/award', methods=['POST'])
def get_award():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    num3 = int(request.form['num3'])

    winning_numbers = {11,22,33}
    count = 0
    if num1 in winning_numbers:
        count += 1
    if num2 in winning_numbers:
        count += 1
    if num3 in winning_numbers:
        count += 1

    prize = "Try Again"
    if count == 1:
        prize = "Free Ticket"
    elif count == 2:
        prize = "Concert"
    elif count == 3:
        prize = "$10000"

    return render_template('award.html', prize=prize)

if __name__ == "__main__":
    app.run(host='0.0.0.0')