from django.db import models
from core.models import RontalModel
from userauth.models import User


class ToDo(RontalModel):
    """
    Tas model
    """

    task_master = models.ForeignKey(User, related_name='todo_task_masters')
    executor = models.ForeignKey(User, related_name='todo_executors')
    task = models.TextField()
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    priority = models.IntegerField()