from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Question - вопрос
# title - заголовок вопроса
# text - полный текст вопроса
# added_at - дата добавления вопроса
# rating - рейтинг вопроса (число)
# author - автор вопроса
# likes - список пользователей, поставивших "лайк"
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')

class QuestionManager(models.Manager):
    def new():
        pass

    def popular():
        pass

# Answer - ответ
# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = User

# QuestionManager - менеджер модели Question
# new - метод возвращающий последние добавленные вопросы
# popular - метод возвращающий вопросы отсортированные по рейтингу
