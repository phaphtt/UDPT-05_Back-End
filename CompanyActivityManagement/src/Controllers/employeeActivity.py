from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import employeeActivity

#Test: http://127.0.0.1:5005/employeeActivity/follow/insert POST
# {
#     "idEmployee":1,
#     "idActivity": 1
# }
@app.route('/employeeActivity/follow/insert', methods=['POST'])
def employeeActivityFollowInsert():
   idEmployee = request.json['idEmployee']
   idActivity = request.json['idActivity']
   EmpA = employeeActivity.EmployeeActivity()
   EmpA.insertFollowInformation(idEmployee, idActivity)
   return jsonify(1)
 
#Test: http://127.0.0.1:5005/employeeActivity/register/insert POST
# {
#     "idEmployee":1,
#     "idActivity": 1
# }
@app.route('/employeeActivity/register/insert', methods=['POST'])
def employeeActivityRegisterInsert():
   idEmployee = request.json['idEmployee']
   idActivity = request.json['idActivity']
   EmpA = employeeActivity.EmployeeActivity()
   EmpA.insertRegisterInformation(idEmployee, idActivity)
   return jsonify(1)