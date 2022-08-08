from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import login
import json

@app.route('/login', methods=['GET'])
def Login():
   username = request.args.get('username')
   password = request.args.get('password')
   data = login.checkLogin(username, password)
   return json.dumps(data)

# http://127.0.0.1:5001/login?username='vtlong'&password='long1234'