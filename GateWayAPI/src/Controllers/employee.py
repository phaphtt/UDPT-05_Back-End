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

    apiUrl_infor = InformationService.url + '/employee/information?idEmployee=' + idEmployee

    execute = requests.get(apiUrl_infor)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy thông tin nhân viên'})
    else:
        dic = execute.json()
        apiUrl_department = InformationService.url + '/department/list'

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

    apiUrl = InformationService.url + '/listemployee?idManager=' + idManager + '&pageIndex=' + pageIndex + '&pageSize=' + pageSize

    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các vaccine'})
    else:
        dic = execute.json()
        return jsonify(dic)


@app.route('/employee/update', methods=['PUT'])
def employeeUpdate():
    request.json['add'] = 'add'
    apiUrl = InformationService.url + '/employee/update'

    headers = {"Content-Type": "application/json"}
    execute = requests.put(apiUrl, data=json.dumps(request.json), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các vaccine'})
    else:
        return jsonify(1)


