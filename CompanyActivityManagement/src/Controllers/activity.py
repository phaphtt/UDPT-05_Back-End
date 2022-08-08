from xmlrpc.client import ResponseError
from src import app
from xmlrpc.client import ResponseError
from flask import jsonify, request, Response
from src.Models import activity

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

#Test: http://127.0.0.1:5005/activity/search?activityName=gio GET
@app.route('/activity/search', methods=['GET'])
def activitySearch():
   activityName = request.args.get('activityName')
   data = activity.ActivitySearch(activityName)
   return jsonify([e.getActivity() for e in data])