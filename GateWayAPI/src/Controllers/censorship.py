from operator import methodcaller
import requests
from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
import json
from src.Config import InformationService



#http://127.0.0.1:5001/listrequest/censorship?idCensorship=1&pageIndex=0&pageSize=5&typeRequest=all
@app.route('/listrequest/censorship', methods=['GET'])
def listRequestCensorship():
    idCensorship = request.args.get('idCensorship')
    pageIndex = request.args.get('pageIndex')
    typeRequest = request.args.get('typeRequest')
    pageSize = request.args.get('pageSize')
    requestStatus = request.args.get('requestStatus')

    apiUrl = InformationService.urlEmployeeRequest + '/listrequest/censorship?idCensorship=' + idCensorship + '&pageIndex=' + pageIndex + '&pageSize=' + pageSize + '&typeRequest=' + typeRequest + '&requestStatus=' + requestStatus

    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các yêu cầu'})
    else:
        dic = execute.json()
        return jsonify(dic)


@app.route('/request/update/censorship', methods=['PUT'])
def updateRequestByCensorship():
    apiUrl = InformationService.urlEmployeeRequest + '/request/update/censorship'

    headers = {"Content-Type": "application/json"}
    execute = requests.put(apiUrl, data=json.dumps(request.json), headers=headers)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc cập nhật trạng thái yêu cầu'})
    else:
        return jsonify(1)

#http://127.0.0.1:5001/request/detail?idCensorship=1&pageIndex=0&pageSize=5&typeRequest=all&idRequest=9
@app.route('/request/detail', methods=['GET'])
def requestDetailById():
    idCensorship = request.args.get('idCensorship')
    pageIndex = request.args.get('pageIndex')
    typeRequest = request.args.get('typeRequest')
    pageSize = request.args.get('pageSize')
    idRequest = request.args.get('idRequest')
    requestStatus = request.args.get('requestStatus')

    apiUrl = InformationService.urlEmployeeRequest + '/request/detail?idCensorship=' + idCensorship + '&pageIndex=' + pageIndex + '&pageSize=' + pageSize + '&typeRequest=' + typeRequest + '&idRequest=' + idRequest + '&requestStatus=' + requestStatus

    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các yêu cầu'})
    else:
        dic = execute.json()
        return jsonify(dic)
