from flask import Flask, render_template, request

app = Flask(__name__)

students = {
    "Dylan D'Eloia": "Robotics Club",
    "James Gull": "Weekly Web Design",
    "James Ohara": "Computer Ethics Club"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        org = request.form['org']
        students[name] = org
        return render_template('register.html',students=students)
    else:
        return render_template('register.html',students=students)


if __name__ == "main":
    app.run()