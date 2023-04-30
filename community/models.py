from __future__ import unicode_literals
from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse, reverse_lazy

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Community(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic= models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    date_uploaded = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='community_like')

    def posts_liked(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.topic)

    def get_absolute_url(self):
        return reverse('community_detail', kwargs={"slug": str(self.slug)})



class Discussion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='discussions')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    class Meta:
        ordering = ['-date_created',]
    
    def __str__(self):
        return "Comment {} by {}".format(self.content, self.user)
    
    def can_edit(self, user):
        return user == self.user

    def can_delete(self, user):
        return user == self.user

