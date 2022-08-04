from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import department

@app.route('/department/list', methods=['GET'])
def listDepartment():
   data = department.listDepartment()
   return jsonify([e.getDepartment() for e in data])
