from flask import Flask
from datetime import datetime

def get_time():
    formatted_time = datetime.now().strftime("%A, %d. %B %Y %H:%M:%S")
    return formatted_time

app = Flask(__name__)

@app.route('/')
def something():
    cur_time = get_time()
    text = "Welcome! Current datetime is {}".format(cur_time)
    return text

if __name__  == '__main__':
    app.run(host="0.0.0.0", port=5000)