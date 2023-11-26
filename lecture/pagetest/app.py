from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

REGISTRANTS = {}

SPROTS = [
    "Baseball",
    "Basketball",
    "Soccer"
]

@app.route('/')
def index():
    return render_template('index.html', sports=SPROTS)


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    if not name:
        return render_template('failure.html')
    
    sport = request.form.get('sport')
    if sport not in SPROTS:
        return render_template('failure.html')
    REGISTRANTS[name] = sport
    print(registrants)
    return render_template('success.html')


@app.route('/registrants', methods=['GET'])
def registrants():
    return render_template('registrants.html', registrants=REGISTRANTS)