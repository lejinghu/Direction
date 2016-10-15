from django.contrib import admin
from mission.models import Mission, Task, Relation, Finished

admin.site.register(Mission)
admin.site.register(Task)
admin.site.register(Relation)
admin.site.register(Finished)
# Register your models here.
