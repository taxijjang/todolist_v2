from django.db import models
from django.utils import timezone

class DoTitle(models.Model):
    api_id = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

class DoComment(models.Model):
    title = models.ForeignKey(DoTitle, related_name='docomment', on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment