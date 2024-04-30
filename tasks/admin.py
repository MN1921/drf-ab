from django.contrib import admin
from .models import Task, CallState


class CallStateAdmin(admin.ModelAdmin):
    list_display = ('task', 'result', 'reason')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'task_type')


admin.site.register(CallState, CallStateAdmin)
admin.site.register(Task, TaskAdmin)

