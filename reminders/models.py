from django.db import models

# Create your models here.


class Reminder(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.message
