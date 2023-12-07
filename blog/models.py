from django.db import models


class Post(models.Model):
    title = models.CharField(primary_key=True, max_length=1000)
    data = models.DateField()
    author = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
