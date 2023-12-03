from django.db import models
from django.utils import timezone

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='img/%Y/ %m/ %d')
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
