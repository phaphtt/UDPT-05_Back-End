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
            return jsonify({'message':'Gặp sự cố trong việc lấy thông tin nhân viên'})
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
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các nhân viên'})
    else:
        dic = execute.json()
        return jsonify(dic)

@app.route('/employee/update', methods=['PUT'])
def employeeUpdate():
    apiUrl = InformationService.urlEmployeeInfor + '/employee/update'

    headers = {"Content-Type": "application/json"}
    execute = requests.put(apiUrl, data=json.dumps(request.json), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc cập nhật thông tin cá nhân'})
    else:
        return jsonify(1)

#http://127.0.0.1:5001/employee/information?idEmployee=1

@app.route('/employee/addrequestWFH', methods=['POST'])
def addrequestWFH():
    idEmployee = request.json['idEmployee']

    # apiRequestEmployeeInfor = 'http://127.0.0.1:5004' + '/getRequestEmployeeInfor?idEmployee=' + str(idEmployee)
    apiRequestEmployeeInfor = InformationService.urlEmployeeInfor + '/getRequestEmployeeInfor?idEmployee=' + str(idEmployee)
    execute = requests.get(apiRequestEmployeeInfor)
    if(execute.status_code != 200):
            return jsonify({'message':'Không lấy được thông tin nhân viên: ' + idEmployee})
    else:
        requestEmployeeInfor = execute.json()

    employeeFirstName = requestEmployeeInfor[0]
    employeeLastName = requestEmployeeInfor[1]
    idCensor = requestEmployeeInfor[2]
    censorFirstName = requestEmployeeInfor[3]
    censorLastName = requestEmployeeInfor[4]
    positionCensor = requestEmployeeInfor[5]

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
        'reason' : reason,
        'employeeFirstName' : employeeFirstName,
        'employeeLastName' : employeeLastName,
        'censorFirstName' : censorFirstName,
        'censorLastName' : censorLastName,
        'positionCensor' : positionCensor
    }

    
    apiUrl = InformationService.urlEmployeeRequest + '/employee/addrequestWFH'

    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(body), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Thêm thất bại'})
    else:
        return jsonify({'message':'Thêm thành công'})

@app.route('/employee/addrequestCheckoutLate', methods=['POST'])
def addrequestCheckoutLate():
    idEmployee = request.json['idEmployee']

    # apiRequestEmployeeInfor = 'http://127.0.0.1:5004' + '/getRequestEmployeeInfor?idEmployee=' + str(idEmployee)
    apiRequestEmployeeInfor = InformationService.urlEmployeeInfor + '/getRequestEmployeeInfor?idEmployee=' + str(idEmployee)
    execute = requests.get(apiRequestEmployeeInfor)
    if(execute.status_code != 200):
            return jsonify({'message':'Không lấy được thông tin nhân viên: ' + idEmployee})
    else:
        requestEmployeeInfor = execute.json()

    employeeFirstName = requestEmployeeInfor[0]
    employeeLastName = requestEmployeeInfor[1]
    idCensor = requestEmployeeInfor[2]
    censorFirstName = requestEmployeeInfor[3]
    censorLastName = requestEmployeeInfor[4]
    positionCensor = requestEmployeeInfor[5]

    idRequestType = request.json['idRequestType']
    checkoutDate = request.json['checkoutDate']
    reason = request.json['reason']

    body = {
        'idEmployee' : idEmployee,
        'idRequestType' : idRequestType,
        'idCensor' : idCensor,
        'checkoutDate' : checkoutDate,
        'reason' : reason,
        'employeeFirstName' : employeeFirstName,
        'employeeLastName' : employeeLastName,
        'censorFirstName' : censorFirstName,
        'censorLastName' : censorLastName,
        'positionCensor' : positionCensor
    }

    apiUrl = 'http://127.0.0.1:5003/employee/addrequestCheckoutLate'
    # apiUrl = InformationService.urlEmployeeInfor + '/employee/addrequestCheckoutLate'

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
    # apiUrl =  'http://127.0.0.1:5004/readrequest?idEmployee=' + idEmployee + '&idRequestType=' + idRequestType
    apiUrl =  InformationService.urlEmployeeRequest + '/readrequest?idEmployee=' + idEmployee + '&idRequestType=' + idRequestType
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Không lấy được danh sách yêu cầu'})
    else:
        dic = execute.json()
        return jsonify(dic)

# http://127.0.0.1:5001/employee/readrequest?idEmployee=2&idRequestType=1


@app.route('/employee/addrequestOT', methods=['POST'])
def requestOTAddDetail():
    idEmployee = request.json['idEmployee']
    # # str(idEmployee) vì request.json nó đọc luôn kiểu dl post lên, còn request.args thì nó string sẵn
    # apiGetIdCensor = 'http://127.0.0.1:5004' + '/getIdCensor?idEmployee=' + str(idEmployee)
    # # apiGetIdCensor = InformationService.urlEmployeeInfor + '/getIdCensor?idEmployee=' + idEmployee
    # execute = requests.get(apiGetIdCensor)
    # if(execute.status_code != 200):
    #     return jsonify({'message':'Không lấy được người kiểm duyệt của nhân viên có mã: ' + idEmployee})
    # else:
    #     idCensor = execute.json()
    #     # return str(idCensor)

    #apiRequestEmployeeInfor = 'http://127.0.0.1:5004' + '/getRequestEmployeeInfor?idEmployee=' + str(idEmployee)
    apiRequestEmployeeInfor = InformationService.urlEmployeeInfor + '/getRequestEmployeeInfor?idEmployee=' + str(idEmployee)
    execute = requests.get(apiRequestEmployeeInfor)
    if(execute.status_code != 200):
            return jsonify({'message':'Không lấy được thông tin nhân viên: ' + idEmployee})
    else:
        requestEmployeeInfor = execute.json()

    employeeFirstName = requestEmployeeInfor[0]
    employeeLastName = requestEmployeeInfor[1]
    idCensor = requestEmployeeInfor[2]
    censorFirstName = requestEmployeeInfor[3]
    censorLastName = requestEmployeeInfor[4]
    positionCensor = requestEmployeeInfor[5]
    
    idRequestType = request.json['idRequestType']
    hourOT = request.json['hourOT']
    dayOT = request.json['dayOT']
    reason = request.json['reason']
    dataAddRequestOT = {'idEmployee': idEmployee, 'idRequestType': idRequestType, 'hourOT': hourOT, 'dayOT': dayOT, 'reason': reason, 'idCensor': idCensor, 'employeeFirstName': employeeFirstName, 'employeeLastName': employeeLastName, 'censorFirstName': censorFirstName, 'censorLastName': censorLastName, 'positionCensor': positionCensor}
    # return dataAddRequestOT

    apiAddRequestOT = InformationService.urlEmployeeRequest + '/addrequestOT'
    # apiAddRequestOT = 'http://127.0.0.1:5003' + '/addrequestOT'

    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiAddRequestOT, data=json.dumps(dataAddRequestOT), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Thêm thất bại'})
    else:
        return jsonify({'message':'Thêm thành công'})

@app.route('/employee/addrequestOFF', methods=['POST'])
def requestOFFAddDetail():
    idEmployee = request.json['idEmployee']

    #apiRequestEmployeeInfor = 'http://127.0.0.1:5004' + '/getRequestEmployeeInfor?idEmployee=' + str(idEmployee)
    apiRequestEmployeeInfor = InformationService.urlEmployeeInfor + '/getRequestEmployeeInfor?idEmployee=' + str(idEmployee)
    execute = requests.get(apiRequestEmployeeInfor)
    if(execute.status_code != 200):
            return jsonify({'message':'Không lấy được thông tin nhân viên: ' + idEmployee})
    else:
        requestEmployeeInfor = execute.json()
        
    employeeFirstName = requestEmployeeInfor[0]
    employeeLastName = requestEmployeeInfor[1]
    idCensor = requestEmployeeInfor[2]
    censorFirstName = requestEmployeeInfor[3]
    censorLastName = requestEmployeeInfor[4]
    positionCensor = requestEmployeeInfor[5]

    idRequestType = request.json['idRequestType']
    startDayOFF = request.json['startDayOFF']
    numberDayOFF = request.json['numberDayOFF']
    noteDayOFF = request.json['noteDayOFF']
    reason = request.json['reason']
    dataAddRequestOFF = {'idEmployee': idEmployee, 'idRequestType': idRequestType, 'numberDayOFF': numberDayOFF, 'startDayOFF': startDayOFF, 'noteDayOFF': noteDayOFF, 'reason': reason, 'idCensor': idCensor, 'employeeFirstName': employeeFirstName, 'employeeLastName': employeeLastName, 'censorFirstName': censorFirstName, 'censorLastName': censorLastName, 'positionCensor': positionCensor}
    # return dataAddRequestOFF

    apiAddRequestOFF = InformationService.urlEmployeeRequest + '/addrequestOFF'
    #apiAddRequestOFF = 'http://127.0.0.1:5003' + '/addrequestOFF'

    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiAddRequestOFF, data=json.dumps(dataAddRequestOFF), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Thêm thất bại'})
    else:
        return jsonify({'message':'Thêm thành công'})

@app.route('/employee/checkin_history', methods=['GET'])
def CheckinHistoryList():
    idEmployee = request.args.get('idEmployee')
    pageno = request.args.get('pageno')

    apiUrl = InformationService.urlEmployeeRequest + '/employee/checkin_history?idEmployee=' + idEmployee + '&pageno=' + pageno
    # apiUrl = 'http://127.0.0.1:5003/employee/checkin_history?idEmployee=' + idEmployee + '&pageno=' + pageno

    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Không lấy được danh sách yêu cầu'})
    else:
        dic = execute.json()
        return jsonify(dic)

@app.route('/employee/checkin', methods=['POST'])
def addCheckin():
    idEmployee = request.json['idEmployee']
    startTime = request.json['startTime']
    
    body = {
        'idEmployee' : idEmployee,
        'startTime' : startTime
    }

    # apiUrl = 'http://127.0.0.1:5003/employee/checkin'
    apiUrl = InformationService.urlEmployeeRequest + '/employee/checkin'

    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(body), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Bạn đã checkin vào trước đó! Xin vui lòng thực hiện checkout.'})
    else:
        return jsonify({'message':'Thêm thành công'})

@app.route('/employee/checkout', methods=['POST'])
def addCheckout():
    idEmployee = request.json['idEmployee']
    
    body = {
        'idEmployee' : idEmployee
    }

    # apiUrl = 'http://127.0.0.1:5003/employee/checkout'
    apiUrl = InformationService.urlEmployeeRequest + '/employee/checkout'

    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(body), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Bạn đã checkout vào trước đó! Xin vui lòng checkout vào ngày mai'})
    else:
        return jsonify({'message':'Checkout thành công'})