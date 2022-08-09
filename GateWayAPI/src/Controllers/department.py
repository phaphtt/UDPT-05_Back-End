import requests
from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
import json
from src.Config import InformationService


#http://127.0.0.1:5001/department/list
@app.route('/department/list', methods=['GET'])
def listDepartment():
    apiUrl = InformationService.url + '/department/list'

    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các vaccine'})
    else:
        dic = execute.json()
        return jsonify(dic)
