from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class SavedExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_id = models.CharField(max_length=100) 
    
    def __str__(self):
        return f"{self.exercise_id} saved by {self.user.username}"