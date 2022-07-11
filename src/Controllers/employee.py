from src import app
from flask import jsonify, request, Response
from src.Models import employee
import json

@app.route('/employee', methods=['GET'])
def employeeDetail():
   data = employee.employeeInfor()
   return jsonify([e.getEmployee() for e in data])