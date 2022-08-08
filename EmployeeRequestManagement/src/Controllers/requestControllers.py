from xmlrpc.client import ResponseError
from src import app
from flask import jsonify, request, Response
from src.Models import requestModels

@app.route('/readrequest', methods=['GET'])
def requestReadDetail():
   idEmployee = request.args.get('idEmployee')
   idRequestType = request.args.get('idRequestType')
   data = requestModels.readRequest(idEmployee, idRequestType)
   return jsonify([e.getRequest() for e in data])

# http://127.0.0.1:5003/readrequest?idEmployee=3&idRequestType=1


@app.route('/addrequestOT', methods=['POST'])
def requestOTAddDetail():
   idEmployee = request.json['idEmployee']
   idRequestType = request.json['idRequestType']
   hourOT = request.json['hourOT']
   dayOT = request.json['dayOT']
   reason = request.json['reason']

   response = requestModels.Request()
   response.addRequestOT(idRequestType, idEmployee, hourOT, dayOT, reason)
   if (response):
      return "Thêm thành công"
   return "Thêm thất bại"

# http://127.0.0.1:5001/addrequestOT



