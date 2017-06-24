from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    def new():
        pass

    def popular():
        pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=True)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

