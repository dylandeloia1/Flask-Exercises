from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    current_time = now.strftime("%A, %B %d %Y %-I:%M:%S %p")
    return render_template('index.html',time=current_time)

if __name__ == "main":
    app.run()
