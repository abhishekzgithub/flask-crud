from flask import Flask, redirect, request, jsonify, url_for

from db import User, db
import json

from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/product/<cityid>/users',methods=['GET'])
def get_users(cityid):
    result=User.query.filter_by(cityid=cityid).all()
    data=[result[i].username for i in range(len(result))]
    return jsonify(data)

@app.route('/product/<cityid>/users',methods=['POST'])
def create_user(cityid):
    request_data = request.get_json()
    user=User(username=request_data['name'],cityid=cityid)
    db.session.add(user)
    db.session.commit()
    return "",200
    

@app.route('/product/<cityid>/users/<userid>',methods=['PUT'])
def update_user(cityid, userid):
    request_data = request.get_json()
    user = User.query.filter_by(id=userid).first()
    user.username = request_data['name']
    db.session.commit()
    return "",200
     

@app.route('/product/<cityid>/users/<userid>',methods=['DELETE'])
def delete_user(cityid, userid):
    user=User.query.filter_by(id=userid).first()
    db.session.delete(user)
    db.session.commit()
    return "",200

if __name__ == '__main__':
    HOST_IP = os.getenv("HOST_IP")
    HOST_PORT = os.getenv("HOST_PORT")
    DEBUG=os.getenv("DEBUG")
    app.run(host=HOST_IP, port=HOST_PORT, use_reloader=False,debug=DEBUG)