from src import app
from flask import jsonify, request
from src.Models import employee

@app.route('/employee', methods=['GET'])
def employeeDetail():
   data = employee.employeeInfor()
   return jsonify(data)