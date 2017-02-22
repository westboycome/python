from django.db import models
from django.contrib import  admin
class Article(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=20)
    content = models.TextField(null=True)

admin.site.register(Article)

def __unicode__(self):
        return self.title