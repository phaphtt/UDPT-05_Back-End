from xmlrpc.client import ResponseError
from src import app
from flask import jsonify, request, Response
from src.Models import request

@app.route('/readrequest', methods=['GET'])
def requestReadDetail():
   idEmployee = request.args.get('idEmployee')
   idRequestType = request.args.get('idRequestType')
   data = request.readRequest(idEmployee, idRequestType)
   return jsonify([e.getRequest() for e in data])

# http://127.0.0.1:5001/readrequest?idEmployee=2&idRequestType=1