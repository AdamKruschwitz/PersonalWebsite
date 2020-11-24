from django.db import models
from django.utils import timezone
from . import constants
import datetime



class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published')
    last_modified = models.DateTimeField()

    def was_published_recently(self):
        """
        Returns whether the item was published within the RECENT_THRESHOLD_DAYS
        """
        now = timezone.now()
        return now-datetime.timedelta(days=RECENT_THRESHOLD_DAYS) <= self.pub_date <= now

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE)
    poster_name = models.CharField(max_length=64)
    comment_body = models.CharField(max_length=280)
    post_date = models.DateTimeField('date posted')
