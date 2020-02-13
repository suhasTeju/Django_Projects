from django.db import models

class Do(models.Model):
    date=models.DateTimeField()
    task=models.CharField(max_length=200)

    def __str__(self):
        return (self.task)
