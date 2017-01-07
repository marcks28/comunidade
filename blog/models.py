from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    published_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to='blog/img/%Y/%m/%d/', blank=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
