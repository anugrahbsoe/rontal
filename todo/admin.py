from todo.models import ToDo
from django.contrib import admin
from core.admin import RontalAdmin


class ToDoAdmin(RontalAdmin):
    """
    ToDo administrator
    """

    fields = ['task_master', 'executor', 'task',
              'start_date', 'due_date', 'priority']
    list_display = ('task_master', 'executor', 'task',
                    'start_date', 'due_date', 'priority')


admin.site.register(ToDo, ToDoAdmin)