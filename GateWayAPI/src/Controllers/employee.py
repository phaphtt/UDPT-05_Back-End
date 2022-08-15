import requests
from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
import json
from src.Config import InformationService

#http://127.0.0.1:5001/employee/information?idEmployee=1
@app.route('/employee/information', methods=['GET'])
def employeeDetail():
    idEmployee = request.args.get('idEmployee')

    apiUrl_infor = InformationService.urlEmployeeInfor + '/employee/information?idEmployee=' + idEmployee

    execute = requests.get(apiUrl_infor)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy thông tin nhân viên'})
    else:
        dic = execute.json()
        apiUrl_department = InformationService.urlEmployeeInfor + '/department/list'

        execute = requests.get(apiUrl_department)
        if(execute.status_code != 200):
            return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các vaccine'})
        else:
            dic_temp = execute.json()
            dic['list_department'] = dic_temp
            return dic

#http://127.0.0.1:5001/listemployee?idManager=1&pageIndex=1&pageSize=5
@app.route('/listemployee', methods=['GET'])
def listEmployee():
    idManager = request.args.get('idManager')
    pageIndex = request.args.get('pageIndex')
    pageSize = request.args.get('pageSize')

    apiUrl = InformationService.urlEmployeeInfor + '/listemployee?idManager=' + idManager + '&pageIndex=' + pageIndex + '&pageSize=' + pageSize

    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các vaccine'})
    else:
        dic = execute.json()
        return jsonify(dic)


@app.route('/employee/update', methods=['PUT'])
def employeeUpdate():
    request.json['add'] = 'add'
    apiUrl = InformationService.urlEmployeeInfor + '/employee/update'

    headers = {"Content-Type": "application/json"}
    execute = requests.put(apiUrl, data=json.dumps(request.json), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các vaccine'})
    else:
        return jsonify(1)

#http://127.0.0.1:5001/employee/information?idEmployee=1
# @app.route('/employee/checkin_history', methods=['GET'])
# def listEmployeeCheckin():
#    idEmployee = request.args.get('idEmployee')

#    apiUrl = InformationService.urlEmployeeRequest + '/employee/checkin_history?idEmployee=' + idEmployee

#    execute = requests.get(apiUrl)

#    if(execute.status_code != 200):
#       return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các vaccine'})
#    else:
#       dic = execute.json()
#       return dic

@app.route('/employee/addrequestWFH', methods=['POST'])
def addrequestWFH():
    idEmployee = request.json['idEmployee']
    getCensorIdUrl = 'http://127.0.0.1:5004/getIdCensor?idEmployee=' + str(idEmployee)
    executeCensorId = requests.get(getCensorIdUrl)
    idCensor = executeCensorId.json()

    idRequestType = request.json['idRequestType']
    startDayWFH = request.json['startDayWFH']
    endDayWFH = request.json['endDayWFH']
    reason = request.json['reason']

    body = {
        'idEmployee' : idEmployee,
        'idRequestType' : idRequestType,
        'idCensor' : idCensor,
        'startDayWFH' : startDayWFH,
        'endDayWFH' : endDayWFH,
        'reason' : reason
    }

    apiUrl = 'http://127.0.0.1:5003/employee/addrequestWFH'

    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(body), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Thêm thất bại'})
    else:
        return jsonify({'message':'Thêm thành công'})

# body: {
#    "idEmployee" : 2,
#     "idRequestType": 2,
#     "idCensor": 3,
#     "startDayWFH": "'2022-07-14'",
#     "endDayWFH": "'2022-07-24'",
#     "reason":"'cuoi vo'"
# }

@app.route('/employee/readrequest', methods=['GET'])
def requestReadDetail():
    idEmployee = request.args.get('idEmployee')
    idRequestType = request.args.get('idRequestType')
    apiUrl = InformationService.urlEmployeeRequest + '/readrequest?idEmployee=' + idEmployee + '&idRequestType=' + idRequestType
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Không lấy được danh sách yêu cầu'})
    else:
        dic = execute.json()
        return jsonify(dic)
        
# http://127.0.0.1:5001/employee/readrequest?idEmployee=2&idRequestType=1
