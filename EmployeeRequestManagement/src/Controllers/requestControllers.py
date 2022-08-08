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

# http://127.0.0.1:5001/readrequest?idEmployee=2&idRequestType=1

@app.route('/employee/addrequestWFH', methods=['POST'])
def requestWFHAddDetail():
   idRequestType = request.json['idRequestType']
   idEmployee = request.json['idEmployee']
   idCensor = request.json['idCensor']
   startDayWFH = request.json['startDayWFH']
   endDayWFH = request.json['endDayWFH']
   reason = request.json['reason']

   response = requestModels.Request()
   response.addRequestWFH(idRequestType, idEmployee, idCensor, startDayWFH, endDayWFH, reason)
   return {
      'message':'Thêm thành công'
   }