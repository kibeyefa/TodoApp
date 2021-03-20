from django.contrib import admin

# Register your models here.
from Todo_list.models import Task

admin.site.register(Task)
