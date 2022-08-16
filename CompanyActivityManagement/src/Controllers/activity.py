from xmlrpc.client import ResponseError
from ..Models.activity import Activity
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import activity

#https://company-activity.herokuapp.com/
#Test: http://127.0.0.1:5005/activity/getall GET
@app.route('/activity/getall', methods=['GET'])
def list_all_acitvity():
   data = activity.list_all_Activity()
   return jsonify([e.getActivity() for e in data])


#Test: http://127.0.0.1:5005/activity/information?activityId=2 GET
@app.route('/activity/information', methods=['GET'])
def activityDetail():
   activityId = request.args.get('activityId')
   data = activity.ActivityInfor(activityId)
   return jsonify([e.getActivity() for e in data])

#Test: http://127.0.0.1:5005/activity/search POST
@app.route('/activity/search', methods=['POST'])
def activitySearch():
   activityName = request.json['activityName']
   dataA = activity.ActivitySearch(activityName)
   return jsonify([e.getActivity() for e in dataA])