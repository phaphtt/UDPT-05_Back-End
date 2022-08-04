from src import app
from flask import jsonify, request, Response
from src.Models import deviceRequest

@app.route('/deviceRequest/insert', methods=['POST'])
def deviceRequestInsert():
   idEmployee = request.json['idEmployee']
   requestName = request.json['requestName']
   type = request.json['type']
   reason = request.json['reason']
   noteRequest = request.json['noteRequest']
   Dre= deviceRequest.DeviceRequest()
   Dre.insertInformation(idEmployee, requestName, type, reason, noteRequest)
   return {
      'message':'Thêm thành công'
   }
   
@app.route('/deviceRequest/listdeviceRequestByEmpId', methods=['GET'])
def ListdeviceRequestByEmpId():
   idEmployeee = request.args.get('idEmployee')
   data = deviceRequest.ListDeviceRequestByEmployeeId(idEmployeee)
   return jsonify([t.getInformation() for t in data])

@app.route('/deviceRequest/listdeviceRequestById', methods=['GET'])
def ListdeviceRequestById():
   id = request.args.get('id')
   data = deviceRequest.ListDeviceRequestById(id)
   return jsonify([t.getInformation() for t in data])

@app.route('/deviceRequest/listalldeviceRequest', methods=['GET'])
def ListAllDeviceRequest():
   data = deviceRequest.list_all_DeviceRequest()
   return jsonify([t.getInformation() for t in data])

@app.route('/deviceRequest/listdeviceRequestByStatus', methods=['GET'])
def ListdeviceRequestByStatus():
   requestStatus = request.args.get('requestStatus')
   data = deviceRequest.list_DeviceRequestByStatus(requestStatus)
   return jsonify([t.getInformation() for t in data])

@app.route('/deviceRequest/update_form/ITManager', methods=['POST'])
def deviceRequestUpdateFormByITManager():
   requestStatus = request.json['requestStatus']
   requestITRejectReason = request.json['requestITRejectReason']
   idITManager = request.json['idITManager']
   id = request.json['id']
   Dre= deviceRequest.DeviceRequest()
   Dre.updateInformationByITManager(requestStatus, requestITRejectReason, idITManager, id)
   return {
      'message':'Cập nhật thành công'
   }
   
@app.route('/deviceRequest/update_form/Presindent', methods=['POST'])
def deviceRequestUpdateFormByPresindent():
   requestStatus = request.json['requestStatus']
   requestManagerRejectReason = request.json['requestManagerRejectReason']
   id = request.json['id']
   Dre= deviceRequest.DeviceRequest()
   Dre.updateInformationByPresident(requestStatus, requestManagerRejectReason, id)
   return {
      'message':'Cập nhật thành công'
   }