from django.db import models
from django.contrib.auth.models import User

STATUS = ((1, "Not Started"), (2, "In Progress"), (3, "Complete"))

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user"
    )
    name = models.CharField(max_length=200)
    notes = models.TextField(default=" ", null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name