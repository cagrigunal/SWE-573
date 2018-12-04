from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Tweet(models.Model):
    tweet_text = models.CharField(max_length=280)
    pub_date = models.DateTimeField('date published')