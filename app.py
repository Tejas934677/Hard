from flask import Flask, render_template
from datetime import datetime
import os

api_key = os.getenv("MY_API_KEY")


app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    target = datetime(2028, 8, 1)
    remaining = target - now

    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    return render_template('index.html', days=days, hours=hours, minutes=minutes, seconds=seconds)

if __name__ == '__main__':
    app.run(debug=True)
