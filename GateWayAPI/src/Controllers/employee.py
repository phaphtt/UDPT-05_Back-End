from operator import methodcaller
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


#http://127.0.0.1:5001/listrequest/censorship?idCensorship=1&pageIndex=0&pageSize=5&typeRequest=all
@app.route('/listrequest/censorship', methods=['GET'])
def listRequestCensorship():
    idCensorship = request.args.get('idCensorship')
    pageIndex = request.args.get('pageIndex')
    typeRequest = request.args.get('typeRequest')
    pageSize = request.args.get('pageSize')

    apiUrl = InformationService.urlEmployeeRequest + '/listrequest/censorship?idCensorship=' + idCensorship + '&pageIndex=' + pageIndex + '&pageSize=' + pageSize + '&typeRequest=' + typeRequest

    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các yêu cầu'})
    else:
        dic = execute.json()
        return jsonify(dic)


@app.route('/employee/update', methods=['PUT'])
def employeeUpdate():
    apiUrl = InformationService.urlEmployeeInfor + '/employee/update'
    headers = {"Content-Type": "application/json"}
    execute = requests.put(apiUrl, data=json.dumps(request.json), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc cập nhật thông ti cá nhân'})
    else:
        return jsonify(1)


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


@app.route('/employee/addrequestOT', methods=['POST'])
def requestOTAddDetail():
    idEmployee = request.json['idEmployee']
    # str(idEmployee) vì request.json nó đọc luôn kiểu dl post lên, còn request.args thì nó string sẵn
    apiGetIdCensor = 'http://127.0.0.1:5004' + '/getIdCensor?idEmployee=' + str(idEmployee)
    # apiGetIdCensor = InformationService.urlEmployeeInfor + '/getIdCensor?idEmployee=' + idEmployee
    execute = requests.get(apiGetIdCensor)
    if(execute.status_code != 200):
        return jsonify({'message':'Không lấy được người kiểm duyệt của nhân viên có mã: ' + idEmployee})
    else:
        idCensor = execute.json()
        # return str(idCensor)
        
    idRequestType = request.json['idRequestType']
    hourOT = request.json['hourOT']
    dayOT = request.json['dayOT']
    reason = request.json['reason']
    dataAddRequestOT = {'idEmployee': idEmployee, 'idRequestType': idRequestType, 'hourOT': hourOT, 'dayOT': dayOT, 'reason': reason, 'idCensor': idCensor}
    # return dataAddRequestOT

    apiAddRequestOT = InformationService.urlEmployeeRequest + '/addrequestOT'

    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiAddRequestOT, data=json.dumps(dataAddRequestOT), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Thêm thất bại'})
    else:
        return jsonify({'message':'Thêm thành công'})



@app.route('/employee/addrequestOFF', methods=['POST'])
def requestOFFAddDetail():
    idEmployee = request.json['idEmployee']
    apiGetIdCensor = 'http://127.0.0.1:5004' + '/getIdCensor?idEmployee=' + str(idEmployee)
    # apiGetIdCensor = InformationService.urlEmployeeInfor + '/getIdCensor?idEmployee=' + idEmployee
    execute = requests.get(apiGetIdCensor)
    if(execute.status_code != 200):
        return jsonify({'message':'Không lấy được người kiểm duyệt của nhân viên có mã: ' + idEmployee})
    else:
        idCensor = execute.json()
        # return str(idCensor)
        
    idRequestType = request.json['idRequestType']
    startDayOFF = request.json['startDayOFF']
    numberDayOFF = request.json['numberDayOFF']
    noteDayOFF = request.json['noteDayOFF']
    reason = request.json['reason']
    dataAddRequestOFF = {'idEmployee': idEmployee, 'idRequestType': idRequestType, 'numberDayOFF': numberDayOFF, 'startDayOFF': startDayOFF, 'noteDayOFF': noteDayOFF, 'reason': reason, 'idCensor': idCensor}
    # return dataAddRequestOT

    apiAddRequestOFF = InformationService.urlEmployeeRequest + '/addrequestOFF'

    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiAddRequestOFF, data=json.dumps(dataAddRequestOFF), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Thêm thất bại'})
    else:
        return jsonify({'message':'Thêm thành công'})
