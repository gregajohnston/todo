from django.db import models


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    assignment_date = models.DateTimeField('date assigned')


class Deadline(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    deadline_text = models.CharField(max_length=200)
    due_date = models.DateTimeField('date due')
