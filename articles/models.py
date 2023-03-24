from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    thumb = models.ImageField(blank=True, default="default.png")
    author = models.ForeignKey(User, default=2 , on_delete=models.CASCADE)

    def __str__(self):
        return self.title