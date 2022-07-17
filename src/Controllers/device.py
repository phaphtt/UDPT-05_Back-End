from src import app
from flask import jsonify, request, Response
from src.Models import device
import json


@app.route('/device/listalldevice', methods=['GET'])
def ListAllDevice():
   data = device.list_all_Device()
   return jsonify([t.getInformation() for t in data])