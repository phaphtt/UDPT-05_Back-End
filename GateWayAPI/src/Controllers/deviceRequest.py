import requests
from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
import json
from src.Config import InformationService

#http://127.0.0.1:5001/device/listAllDevice
@app.route('/device/listAllDevice', methods=['GET'])
def ListAllDevice():
    apiUrl = InformationService.urlDeviceRequest + '/device/listalldevice'
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các thiết bị'})
    else:
        dic = execute.json()
        return jsonify(dic)

#http://127.0.0.1:5001/deviceRequest/insert
# {
#    "idEmployee":2,
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
    dataFollow = {'idEmployee': idEmployee, 'requestName': requestName, 'type': type, 'reason': reason, 'noteRequest': noteRequest}
    apiUrl = InformationService.urlDeviceRequest + '/deviceRequest/insert'
    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(dataFollow), headers=headers)
    
    if(execute.status_code != 200):
        return jsonify({'message':'Thêm thất bại'})
    else:
        return jsonify({'message':'Thêm thành công'})
    
#http://127.0.0.1:5001/deviceRequest/listdeviceRequestByEmpId?idEmployee=2
@app.route('/deviceRequest/listdeviceRequestByEmpId', methods=['GET'])
def ListdeviceRequestByEmpId():
    idEmployeee = request.args.get('idEmployee')
    apiUrl = InformationService.urlDeviceRequest + '/deviceRequest/listdeviceRequestByEmpId?idEmployee=' + idEmployeee
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc tìm kiếm danh sách yêu cầu thiết bị'})
    else:
        dic = execute.json()
        return jsonify(dic)
    
#http://127.0.0.1:5001/deviceRequest/listdeviceRequestById?id=1
@app.route('/deviceRequest/listdeviceRequestById', methods=['GET'])
def ListdeviceRequestById():
    id = request.args.get('id')
    apiUrl = InformationService.urlDeviceRequest + '/deviceRequest/listdeviceRequestById?id=' + id
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc tìm kiếm danh sách yêu cầu thiết bị'})
    else:
        dic = execute.json()
        return jsonify(dic)

#http://127.0.0.1:5001/deviceRequest/listAllDeviceRequest
@app.route('/deviceRequest/listAllDeviceRequest', methods=['GET'])
def ListAllDeviceRequest():
    apiUrl = InformationService.urlDeviceRequest + '/deviceRequest/listalldeviceRequest'
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc tìm kiếm danh sách yêu cầu thiết bị'})
    else:
        dic = execute.json()
        return jsonify(dic)
    
#http://127.0.0.1:5001/deviceRequest/listdeviceRequestByStatus
@app.route('/deviceRequest/listdeviceRequestByStatus', methods=['POST'])
def ListdeviceRequestByStatus():
    requestStatus = request.json['requestStatus']
    dataFollow = {'requestStatus': requestStatus}
    apiUrl = InformationService.urlDeviceRequest + '/deviceRequest/listdeviceRequestByStatus'
    execute = requests.get(apiUrl)

    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(dataFollow), headers=headers)
    
    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố khi tìm kiếm đơn yêu cầu'})
    else:
        dic = execute.json()
        return jsonify(dic)

#http://127.0.0.1:5001/deviceRequest/update_form/ITManager
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
    dataFollow = {'id': id, 'idITManager': idITManager, 'requestITRejectReason': requestITRejectReason, 'requestStatus': requestStatus}
    apiUrl = InformationService.urlDeviceRequest + '/deviceRequest/update_form/ITManager'
    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(dataFollow), headers=headers)
    
    if(execute.status_code != 200):
        return jsonify({'message':'Cập nhật thất bại'})
    else:
        return jsonify({'message':'Cập nhật thành công'})
    
#http://127.0.0.1:5001/deviceRequest/update_form/Presindent
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
    dataFollow = {'id': id, 'requestManagerRejectReason': requestManagerRejectReason, 'requestStatus': requestStatus}
    apiUrl = InformationService.urlDeviceRequest + '/deviceRequest/update_form/Presindent'
    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(dataFollow), headers=headers)
    
    if(execute.status_code != 200):
        return jsonify({'message':'Cập nhật thất bại'})
    else:
        return jsonify({'message':'Cập nhật thành công'})