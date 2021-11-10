from flask import Flask, jsonify, request, render_template, redirect
from flask_cors import CORS
from flask_pymongo import PyMongo
import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://mathusankandiah:spaceracepassword@cluster0.kyf40.mongodb.net/lap-4-challenge"
mongo = PyMongo(app)

CORS(app)


@app.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html")


@app.route('/shorten',  methods=['POST'])
def shorten():
    if request.method == 'POST':
        # print(request.method)
        short_id = str(uuid.uuid4())[0:6]
        # print(short_id)
        url = request.form['url']
        # print(url)
        mongo.db.short_urls.insert_one({'short_id' : short_id, 'url' : url})
        full_short_url = f'localhost:5000/{short_id}'
        return render_template("home.html", url = full_short_url)

@app.route('/<short>', methods=['GET'])
def change(short):
    url = mongo.db.short_urls.find_one({'short_id': short})
    if url:
        long_url = url['url']
        if long_url[0:8] == "https://" or long_url[0:7] == "http://":
            print(long_url)
            return redirect(long_url)
        else:
            return redirect(f'https://{long_url}')
    else:
        return redirect('/')


    



if __name__ == '__main__':
    app.run(debug=True)
