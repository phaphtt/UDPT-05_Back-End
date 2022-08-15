from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import employee_task

@app.route('/employee/listtask', methods=['GET'])
def listEmployee():
   idEmployee = request.args.get('idEmployee')
   pageIndex = request.args.get('pageIndex')
   pageSize = request.args.get('pageSize')
   status = request.args.get('status')
   data = employee_task.listTask(idEmployee, pageIndex, pageSize, status)
   return jsonify([t.getTaskEmployee() for t in data])
