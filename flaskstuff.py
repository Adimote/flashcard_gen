from flask import Flask, request, send_file, render_template
from csv import reader, writer
import os.path
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    if os.path.isfile('flashcards.html'):
        return send_file('flashcards.html')
    else:
        return render_template('404.html'), 404


@app.route("/data", methods=['POST'])
def hello():
    data = {}

    if os.path.isfile('gotits.csv'):
        with open('gotits.csv','r') as f:
            r = reader(f)
            data = {q:int(c) for q,c in r}
            for key,value in request.form.items():
                data.setdefault(key,0)
                data[key] += 1
                print(f"{key}: {data[key]} {value}")
    with open('gotits.csv','w') as f:
        w = writer(f)
        for key,value in data.items():
            w.writerow([key,value])
    return ""
