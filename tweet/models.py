from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class tweet_posts(models.Model):
#   'jc3256-squawker.herokuapp.com'
    post_text = models.CharField(max_length=140)
    post_time = models.DateTimeField('time published')

#    def __str__(self):
#        return self.post_text
