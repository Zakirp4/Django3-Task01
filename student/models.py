from django.db import models

class StudentList(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    roll = models.IntegerField()
    std_class = models.CharField(max_length=302, blank=True)
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.name

