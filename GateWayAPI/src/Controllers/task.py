import requests
from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Config import InformationService
import json


@app.route('/employee/listtask', methods=['GET'])
def requestListTask():
    idEmployee = request.args.get('idEmployee')
    pageIndex = request.args.get('pageIndex')
    pageSize = request.args.get('pageSize')
    status = request.args.get('status')
    apiUrl = InformationService.urlEmployeeTask + '/employee/listtask?idEmployee=' + idEmployee + '&pageIndex=' + pageIndex + '&pageSize=' + pageSize + '&status=' + status
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Không lấy được danh sách yêu cầu'})
    else:
        tasks = execute.json()
        data = {}
        data["listTasks"] = tasks

        apiUrl_infor = InformationService.urlEmployeeInfor + '/employee/information?idEmployee=' + idEmployee

        execute = requests.get(apiUrl_infor)
        if(execute.status_code != 200):
            return jsonify({'message':'Không lấy được danh sách yêu cầu'})
        else:
            employee = execute.json()
            data["employee"]= employee
            return jsonify(data)

# http://127.0.0.1:5001/employee/listtask?idEmployee=1&pageIndex=10&pageSize=10&status=all


@app.route('/employee/taskdetail', methods=['GET'])
def taskDetail():
    idEmployee = request.args.get('idEmployee')
    pageIndex = request.args.get('pageIndex')
    pageSize = request.args.get('pageSize')
    status = request.args.get('status')
    idTask = request.args.get('idTask')
    apiUrl = InformationService.urlEmployeeTask + '/employee/taskdetail?idEmployee=' + idEmployee + '&pageIndex=' + pageIndex + '&pageSize=' + pageSize + '&status=' + status + '&idTask=' + idTask
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Không lấy được dữ liệu'})
    else:
        tasks = execute.json()
        data = {}
        data = tasks

        apiUrl_infor = InformationService.urlEmployeeInfor + '/employee/information?idEmployee=' + idEmployee

        execute = requests.get(apiUrl_infor)
        if(execute.status_code != 200):
            return jsonify({'message':'Không lấy được dữ liệu'})
        else:
            employee = execute.json()
            data["employee"]= employee
            return jsonify(data)

# http://127.0.0.1:5001/employee/taskdetail?idEmployee=1&pageIndex=10&pageSize=10&status=all&idTask=1

@app.route('/employee/task/update', methods=['PUT'])
def updateTaskByEmployee():
    apiUrl = InformationService.urlEmployeeTask + '/employee/task/update'

    headers = {"Content-Type": "application/json"}
    execute = requests.put(apiUrl, data=json.dumps(request.json), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc cập nhật trạng thái công việc'})
    else:
        return jsonify(1)

@app.route('/manage/listtask', methods=['GET'])
def manageListTask():
    idEmployee = request.args.get('idEmployee')
    apiUrl_infor = InformationService.urlEmployeeInfor + '/employee/information?idEmployee=' + idEmployee

    execute = requests.get(apiUrl_infor)
    if(execute.status_code != 200):
        return jsonify({'message':'Không lấy được thông tin nhân viên'})
    else:
        employee = execute.json()
        idDepartment = employee['idDepartment']
        pageIndex = request.args.get('pageIndex')
        pageSize = request.args.get('pageSize')
        status = request.args.get('status')

        apiUrl = InformationService.urlEmployeeTask + '/manage/listtask?idDepartment=' + str(idDepartment) + '&pageIndex=' + pageIndex + '&pageSize=' + pageSize + '&status=' + status
        execute = requests.get(apiUrl)

        if(execute.status_code != 200):
            return jsonify({'message':'Không lấy được danh sách yêu cầu'})
        else:
            dic = execute.json()
            return jsonify(dic)
    