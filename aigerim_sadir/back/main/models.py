from django.db import models
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class Post(models.Model):
    title=models.CharField(max_length=80)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    created_at=models.DateTimeField(auto_now=True)
    body=models.CharField(max_length=5000)
    like_count = models.IntegerField(default=0,null=True)
    # objects = PostManager()
    def __str__(self):
        return '{}: {}'.format(self.title, self.created_by)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at':self.created_at,
            
            'body':self.body,
            'like_count':self.like_count
        }