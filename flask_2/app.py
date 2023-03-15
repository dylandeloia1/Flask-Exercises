from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.get('/result')
def result():
    num = request.args.get('num')
    try:
        if num.isdigit():
            if int(num) % 2 == 0:
                check = "even"
            else:
                check = "odd"
            message = num + " is an " + check + " integer."
        else:
            message = str(num) + " is not an integer!"
    except:
        message = "No number provided."

    return render_template('result.html',message=message)

if __name__ == "main":
    app.run()