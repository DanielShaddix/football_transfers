import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# @python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.question_text

    def was_published_reccently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



# @python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    autor = models.CharField(max_length=50, blank=True)


class Addition(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Addition = models.CharField(max_length=200)


class Transfers_List(models.Model):
    id = models.IntegerField(primary_key=True)
    last_names = models.CharField(max_length=50)
    names = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    club = models.CharField(max_length=50)
    price = models.IntegerField(default=1)

    def __str__(self):
        return self.last_names




# class transfer(models.Model):
#     clubls = models.t
    # def __str__(self):
    #     return self.choice_text


# class Table(models.Model):
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     integer = models.IntegerField()


# Create your models here.
