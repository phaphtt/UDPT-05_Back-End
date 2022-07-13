from src import app
from flask import jsonify, request, Response
from src.Models import employee
from src.Models import employee_task

@app.route('/employee/information', methods=['GET'])
def employeeDetail():
   employeeId = request.args.get('employeeId')
   data = employee.employeeInfor(employeeId)
   return jsonify([e.getInformation() for e in data])

@app.route('/employee/update', methods=['POST'])
def employeeUpdate():
   id = request.json['id']
   firstname = request.json['firstname']
   lastname = request.json['lastname']
   idDepartment = request.json['idDepartment']
   position = request.json['position']
   dayOfBirth = request.json['dayOfBirth']
   gender = request.json['gender']
   email = request.json['email']
   phoneNumber = request.json['phoneNumber']
   address = request.json['address']
   maritalStatus = request.json['maritalStatus']
   Emp = employee.Employee()
   Emp.updateInformation(id, firstname, lastname, idDepartment, position, dayOfBirth, gender, email, phoneNumber, address, maritalStatus)
   return {
      'message':'Cập nhật thành công'
   }

@app.route('/employee/listtask', methods=['GET'])
def employeeListTask():
   idEmployee = request.args.get('idEmployee')
   data = employee_task.listTask(idEmployee)
   return jsonify([t.getTaskEmployee() for t in data])