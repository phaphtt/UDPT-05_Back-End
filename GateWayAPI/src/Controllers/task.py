from operator import methodcaller
import requests
from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
import json
from src.Config import InformationService

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