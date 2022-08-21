from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import employee_task

@app.route('/employee/listtask', methods=['GET'])
def listTask():
   idEmployee = request.args.get('idEmployee')
   pageIndex = request.args.get('pageIndex')
   pageSize = request.args.get('pageSize')
   status = request.args.get('status')
   data = employee_task.listTask(idEmployee, pageIndex, pageSize, status)
   return jsonify([t.getTaskEmployee() for t in data])

@app.route('/employee/taskdetail', methods=['GET'])
def taskDetail():
   idEmployee = request.args.get('idEmployee')
   pageIndex = request.args.get('pageIndex')
   pageSize = request.args.get('pageSize')
   status = request.args.get('status')
   idTask = request.args.get('idTask')
   data = employee_task.taskDetailById(idEmployee, pageIndex, pageSize, status,idTask)
   return jsonify(data)

@app.route('/employee/task/update', methods=['PUT'])
def taskUpdateByCensorship():
   idTask = request.json['idTask']
   status = request.json['status']
   t = employee_task.EmployeeTask()
   t. updateTaskByEmployee(idTask, status)
   return jsonify(1)


@app.route('/manage/listtask', methods=['GET'])
def listTaskManage():
   idDepartment = request.args.get('idDepartment')
   pageIndex = request.args.get('pageIndex')
   pageSize = request.args.get('pageSize')
   status = request.args.get('status')
   data = employee_task.listTaskByIdDepartment(idDepartment, pageIndex, pageSize, status)
   return jsonify([t.getTaskEmployee() for t in data])