from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

