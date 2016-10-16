from django.conf.urls import url
from mission import views

urlpatterns = [
    url(r'^add/$', views.add_mission, name="add_mission"),
    url(r'^get_all/$', views.get_all_missions, name="get_all_missions"),
    url(r'^get/$', views.get_mission_details, name="get_mission_details"),
    url(r'^join/$', views.join_mission, name="join_mission"),
    url(r'^processing/upload/$', views.finish_task, name="finish_task"),
    url(r'^processing/get_unfinished_tasks/$', views.get_unfinished_tasks, name="get_unfinished_tasks")
]


