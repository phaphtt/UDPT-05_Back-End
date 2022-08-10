import requests
from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
import json
from src.Config import InformationService


#http://127.0.0.1:5001/activity/getall
@app.route('/activity/getall', methods=['GET'])
def listAllActivity():
    apiUrl = InformationService.urlCompanyActivity + '/activity/getall'

    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy danh sách các hoạt động'})
    else:
        dic = execute.json()
        return jsonify(dic)
   
#http://127.0.0.1:5001/activity/information?activityId=2
@app.route('/activity/information', methods=['GET'])
def listActivityDetail():
    idActivity= request.args.get('activityId')
    apiUrl = InformationService.urlCompanyActivity + '/activity/information?activityId=' + idActivity
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc lấy hoạt động yêu cầu'})
    else:
        dic = execute.json()
        return jsonify(dic)
    
#http://127.0.0.1:5001/activity/search?activityName=gio
@app.route('/activity/search', methods=['GET'])
def activitySearch():
    activityName = request.args.get('activityName')
    apiUrl = InformationService.urlCompanyActivity + '/activity/search?activityName=' + activityName
    execute = requests.get(apiUrl)

    if(execute.status_code != 200):
        return jsonify({'message':'Gặp sự cố trong việc tìm kiếm hoạt động'})
    else:
        dic = execute.json()
        return jsonify(dic)

#http://127.0.0.1:5001/employeeActivity/follow/insert POST
# {
#     "idEmployee":1,
#     "idActivity": 1
# }

@app.route('/employeeActivity/follow/insert', methods=['POST'])
def employeeActivityFollowInsert():
    idEmployee = request.json['idEmployee']
    idActivity = request.json['idActivity']
    dataFollow = {'idEmployee': idEmployee, 'idActivity': idActivity}
    apiUrl = InformationService.urlCompanyActivity + '/employeeActivity/follow/insert'
    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(dataFollow), headers=headers)
    
    if(execute.status_code != 200):
        return jsonify({'message':'Thêm thất bại'})
    else:
        return jsonify({'message':'Thêm thành công'})
    
#http://127.0.0.1:5001/employeeActivity/register/insert POST
# {
#     "idEmployee":1,
#     "idActivity": 1
# }
@app.route('/employeeActivity/register/insert', methods=['POST'])
def employeeActivityRegisterInsert():
    idEmployee = request.json['idEmployee']
    idActivity = request.json['idActivity']
    dataFollow = {'idEmployee': idEmployee, 'idActivity': idActivity}
    apiUrl = InformationService.urlCompanyActivity + '/employeeActivity/register/insert'
    headers = {"Content-Type": "application/json"}
    execute = requests.post(apiUrl, data=json.dumps(dataFollow), headers=headers)
    
    if(execute.status_code != 200):
        return jsonify({'message':'Thêm thất bại'})
    else:
        return jsonify({'message':'Thêm thành công'})


