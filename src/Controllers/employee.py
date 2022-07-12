from src import app
from flask import jsonify, request, Response
from src.Models import employee
import json

@app.route('/employee/information', methods=['GET'])
def employeeDetail():
   employeeId = request.args.get('employeeId')
   data = employee.employeeInfor(employeeId)
   return jsonify([e.getInformation() for e in data])