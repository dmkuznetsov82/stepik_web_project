from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class QuestionManager(models.Manager):
    def new(self, page, limit=10):
        qs = self.order_by('-id')
        res = []
        if page is not None:
            # qs = qs.filter(id__lt=page)
            qs.filter(id__lt=page)
            # filter(is_published=True)
        for p in qs[:1000]:
            if len(res):
                res.append(p)
            # elif res[-1].category != p.category:
            #     res.append(p)
            if len(res) >= limit:
                break
        return res

    def popular(self, page, limit=10):
        qs = self.order_by('-rating')
        res = []
        if page is not None:
            qs = qs.filter(id__lt=page)
        for p in qs[:1000]:
            if len(res):
                res.append(p)
            # elif res[-1].category != p.category:
            #     res.append(p)
            if len(res) >= limit:
                break
        return res

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True)
    likes = models.ManyToManyField(User, related_name='likes_set')

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True)

