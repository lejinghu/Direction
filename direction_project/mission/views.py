from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.models import User

from funcs.json_response import *
from funcs.decorators import load_json_data, login_required

from mission.models import Mission, Task, Relation, Finished

def convert_to_datetime(str):
    """
    str is like "1995 09 08 12 50"
    """
    elements = str.split()
    for i in range(len(elements)):
        elements[i] = int(elements[i])
    return datetime(elements[0], elements[1], elements[2], elements[3], elements[4])
        

@login_required
@load_json_data('tasks', 'min_member_count', 'max_member_count', 'start_time', 'end_time', 'title', 'description')
def add_mission(request, received_data={}):

    start_time = convert_to_datetime(received_data['start_time'])
    end_time = convert_to_datetime(received_data['end_time'])

    mission = Mission(title=received_data['title'], 
                      description=received_data['description'], 
                      min_member_count=int(received_data['min_member_count']),
                      max_member_count=int(received_data['max_member_count']),
                      start_time=start_time,
                      end_time=end_time, 
                      creator=request.user)
    mission.save()

    for task in received_data['tasks']:
        Task(num=task['num'], lng=task['lng'], lat=task['lat'], description=task['description'], mission=mission).save()

    return true_json_response(msg="Mission added successfully")

@login_required
def get_all_missions(request):
    print datetime.today()
    missions = Mission.objects.filter(end_time__gt=datetime.today())
    data = []
    for mission in missions:
        json_data = {"id": mission.id,
                     "title": mission.title,
                     "description": mission.description,
                     "start_time": mission.start_time,
                     "end_time": mission.end_time,
                     "min_member_count": mission.min_member_count,
                     "max_member_count": mission.max_member_count}
        st_task = mission.tasks.filter(num=0)[0]
        json_data['st_lng'] = float(st_task.lng) #[NOTICE]
        json_data['st_lat'] = float(st_task.lat) #[NOTICE]
        data.append(json_data)
    return true_json_response(data=data, msg="Get all missions successfully")

@login_required
@load_json_data("id")
def get_mission_details(request, received_data={}):
    id = int(received_data['id'])
    mission = Mission.objects.get(id=id)
    data = {"title": mission.title,
            "description": mission.description,
            "min_member_count": mission.min_member_count,
            "max_member_count": mission.max_member_count,
            "start_time": mission.start_time,
            "end_time": mission.end_time,
            "creator": mission.creator.username,
            "tasks": []}
    tasks = Task.objects.filter(mission=mission).order_by('num')
    for task in tasks:
        dict_data = {"num": task.num,
                     "lng": float(task.lng),
                     "lat": float(task.lat),
                     "description": task.description,}
        data["tasks"].append(dict_data)

    return true_json_response(data=data, msg="Get mission details successfully")

@login_required
@load_json_data("id")
def join_mission(request, received_data):
    id = int(received_data["id"])
    mission = Mission.objects.get(id=id)
    relation = Relation.objects.get_or_create(user=request.user)[0]
    if relation.joining_mission == None:
        relation.joining_mission = mission
        relation.save()
        return true_json_response(msg="Join mission successfully")
    else:
        return false_json_response(msg="You can't not join two missions at the same time")

@login_required
def finish_task(request):
    num = request.POST['num']
    lng = request.POST['lng']
    lat = request.POST['lat']

    mission = request.user.relation.joining_mission
    task = Task.objects.get(mission=mission, num=num)
    Finished(user=request.user, task=task, img=request.FILES['picture']).save()

    return true_json_response(msg="Task finished")
