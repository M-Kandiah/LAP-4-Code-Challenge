from flask import Flask, jsonify, request, render_template
from flask_cors import CORS


app = Flask(__name__)

CORS(app)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/users',  methods=['GET', 'POST'])
def users():
    pass

if __name__ == '__main__':
    app.run(debug=True)
