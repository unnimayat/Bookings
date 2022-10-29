from flask import Flask,render_template,redirect,url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)  

client = MongoClient('localhost', 27017)

db = client.flask_db
hb = db.hb

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('front.html')

@app.post('/display')
def display():
    data=hb.find()
    return render_template('Example.html',data=data)

if __name__ == '__main__':  
   app.run(debug = True)  