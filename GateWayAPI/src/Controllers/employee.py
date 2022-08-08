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

    apiUrl = InformationService.url + '/employee/information?idEmployee=' + idEmployee

    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các vaccine'})
    else:
        dic = execute.json()
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
#    id = request.json['id']
#    firstname = request.json['firstname']
#    lastname = request.json['lastname']
#    idDepartment = request.json['idDepartment']
#    position = request.json['position']
#    dayOfBirth = request.json['dayOfBirth']
#    gender = request.json['gender']
#    email = request.json['email']
#    phoneNumber = request.json['phoneNumber']
#    address = request.json['address']
#    maritalStatus = request.json['maritalStatus']
#    Emp = employee.Employee()
#    Emp.updateInformation(id, firstname, lastname, idDepartment, position, dayOfBirth, gender, email, phoneNumber, address, maritalStatus)
    request.json['add'] = 'add'
    print(request.json)
    return jsonify(1)
