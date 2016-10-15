from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Mission(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    min_member_count = models.IntegerField()
    max_member_count = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creator = models.ForeignKey(User, related_name="created_missions")
    joineders = models.ManyToManyField(User, related_name="joined_missions")

    def __str__(self):
        return self.title.encode("utf-8")

class Task(models.Model):
    mission = models.ForeignKey(Mission, related_name="tasks")
    num = models.IntegerField()
    lng = models.DecimalField(max_digits=16, decimal_places=12)
    lat = models.DecimalField(max_digits=16, decimal_places=12)
    description = models.TextField()
    
    def __str__(self):
        return self.mission.__str__() + "#" + self.num.__str__()

class Relation(models.Model):
    user = models.OneToOneField(User, related_name="relation")
    joining_mission = models.ForeignKey(Mission, related_name="joiners", null=True, default=None)

    def __str__(self):
        return self.user.__str__() + " " + self.joining_mission.__str__()

class Finished(models.Model):
    user = models.ForeignKey(User, related_name="finished")
    task = models.ForeignKey(Task, related_name="finished")
    img = models.ImageField(upload_to="static/images", blank=True)

    def __str__(self):
        return self.user.__str__() + "#" + self.task.__str__()
