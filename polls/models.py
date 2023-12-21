import datetime

from django.db import models
from django.utils import timezone

image = models.ImageField(upload_to='polls/images/', null=True, blank=True)

class darcek(models.Model):
    nazov = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    pre = models.CharField(max_length=200)
    cena = models.FloatField(default=0.0)
    pub_date = models.DateTimeField("date published")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nametext




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now