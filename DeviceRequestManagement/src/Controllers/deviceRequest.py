from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import deviceRequest


#Test: http://127.0.0.1:5006/deviceRequest/insert POST
# {
#     "idEmployee":2,
#    "requestName": "abc",
#    "type": "Phần cứng",
#    "reason": "xyz",
#    "noteRequest": "123"
# }
@app.route('/deviceRequest/insert', methods=['POST'])
def deviceRequestInsert():
   idEmployee = request.json['idEmployee']
   requestName = request.json['requestName']
   type = request.json['type']
   reason = request.json['reason']
   noteRequest = request.json['noteRequest']
   Dre= deviceRequest.DeviceRequest()
   Dre.insertInformation(idEmployee, requestName, type, reason, noteRequest)
   return jsonify(1)
   
#Test: http://127.0.0.1:5006/deviceRequest/listdeviceRequestByEmpId?idEmployee=2 GET 
@app.route('/deviceRequest/listdeviceRequestByEmpId', methods=['GET'])
def ListdeviceRequestByEmpId():
   idEmployeee = request.args.get('idEmployee')
   data = deviceRequest.ListDeviceRequestByEmployeeId(idEmployeee)
   return jsonify([t.getInformation() for t in data])

#Test: http://127.0.0.1:5006/deviceRequest/listdeviceRequestById?id=1 GET 
@app.route('/deviceRequest/listdeviceRequestById', methods=['GET'])
def ListdeviceRequestById():
   id = request.args.get('id')
   data = deviceRequest.ListDeviceRequestById(id)
   return jsonify([t.getInformation() for t in data])

#Test: http://127.0.0.1:5006/deviceRequest/listalldeviceRequest GET 
@app.route('/deviceRequest/listalldeviceRequest', methods=['GET'])
def ListAllDeviceRequest():
   data = deviceRequest.list_all_DeviceRequest()
   return jsonify([t.getInformation() for t in data])

#Test: http://127.0.0.1:5006/deviceRequest/listdeviceRequestByStatus POST 
@app.route('/deviceRequest/listdeviceRequestByStatus', methods=['POST'])
def ListdeviceRequestByStatus():
   requestStatus =  request.json['requestStatus']
   dataA = deviceRequest.list_DeviceRequestByStatus(requestStatus)
   return jsonify([e.getInformation() for e in dataA])

#Test: http://127.0.0.1:5006/deviceRequest/update_form/ITManager POST
# {
#    "id": 1,
#    "idITManager": 2,
#    "requestITRejectReason": "",
#    "requestStatus":"Tạm duyệt"
# }
@app.route('/deviceRequest/update_form/ITManager', methods=['POST'])
def deviceRequestUpdateFormByITManager():
   requestStatus = request.json['requestStatus']
   requestITRejectReason = request.json['requestITRejectReason']
   idITManager = request.json['idITManager']
   id = request.json['id']
   Dre= deviceRequest.DeviceRequest()
   Dre.updateInformationByITManager(id, idITManager, requestITRejectReason, requestStatus)
   return jsonify(1)
   
#Test: http://127.0.0.1:5006/deviceRequest/update_form/Presindent POST
# {
#    "id": 1,
#    "requestManagerRejectReason": "",
#    "requestStatus":"Thành công"
# }   
@app.route('/deviceRequest/update_form/Presindent', methods=['POST'])
def deviceRequestUpdateFormByPresindent():
   requestStatus = request.json['requestStatus']
   requestManagerRejectReason = request.json['requestManagerRejectReason']
   id = request.json['id']
   Dre= deviceRequest.DeviceRequest()
   Dre.updateInformationByPresident(id, requestManagerRejectReason, requestStatus)
   return jsonify(1)