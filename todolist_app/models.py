from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskList(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    task = models.CharField(max_length=400)
    done = models.BooleanField(default=False)
    date_done = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) :
          return self.task + " ----  Completed:   " +  str(self.done)