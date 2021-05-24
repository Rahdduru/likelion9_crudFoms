from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    writer = models.CharField(null = False, max_length=15)
    body = models.TextField()

    def __str__(self):
        return self.title