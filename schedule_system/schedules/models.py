# schedules/models.py
from django.db import models
class Group(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# schedules/models.py


class Teacher(models.Model):
    name = models.CharField(max_length=100)  # Оставляем только имя

    def __str__(self):
        return self.name



    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
class Room(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
class Schedule(models.Model):
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.subject} ({self.group.name})"