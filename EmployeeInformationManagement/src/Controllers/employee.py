from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import employee


@app.route('/employee/information', methods=['GET'])
def employeeDetail():
   idEmployee = request.args.get('idEmployee')
   data = employee.employeeInfor(idEmployee)
   return jsonify(data.getInformation())

@app.route('/employee/update', methods=['PUT'])
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
   return jsonify(1)

@app.route('/listemployee', methods=['GET'])
def listEmployee():
   idManager = request.args.get('idManager')
   pageIndex = request.args.get('pageIndex')
   pageSize = request.args.get('pageSize')
   data = employee.ListEmployee(idManager, pageIndex, pageSize)
   return jsonify([e.getInformation() for e in data])



# @app.route('/employee/listtask', methods=['GET'])
# def employeeListTask():
#    idEmployee = request.args.get('idEmployee')
#    pageIndex = request.args.get('pageIndex')
#    pageSize = request.args.get('pageSize')
#    status = request.args.get('status')
#    data = employee_task.listTask(idEmployee, pageIndex, pageSize, status)
#    return jsonify([t.getTaskEmployee() for t in data])