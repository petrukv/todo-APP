from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    complited = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title