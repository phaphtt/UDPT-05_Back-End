from src import app
from flask import jsonify, request, Response
from src.Models import employeeActivity
import json

@app.route('/employeeActivity/follow/insert', methods=['POST'])
def employeeActivityFollowInsert():
   idEmployee = request.json['idEmployee']
   idActivity = request.json['idActivity']
   EmpA = employeeActivity.EmployeeActivity()
   EmpA.insertFollowInformation(idEmployee, idActivity)
   return {
      'message':'Thêm thành công'
   }
   
@app.route('/employeeActivity/register/insert', methods=['POST'])
def employeeActivityRegisterInsert():
   idEmployee = request.json['idEmployee']
   idActivity = request.json['idActivity']
   EmpA = employeeActivity.EmployeeActivity()
   EmpA.insertRegisterInformation(idEmployee, idActivity)
   return {
      'message':'Thêm thành công'
   }