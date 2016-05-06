from django.db import models


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    task_importance = models.IntegerField(max_length=200)
    task_status = models.CharField(max_length=200)
    assignment_date = models.DateTimeField('date assigned')
    due_date = models.DateTimeField('date due')
    completion_date = models.DateTimeField('date completed')
