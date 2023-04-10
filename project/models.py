from django.db import models
from profile.models import Profile

import profile.models


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=220)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='media/',)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    views = models.IntegerField(default=0)# defoult bu nechi qiymat berish uchun articlaga
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ExtraText(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='subcontent')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class ExtraPicture(models.Model):
    article_text = models.ForeignKey(ExtraText, on_delete=models.CASCADE, related_name='subimage')
    image = models.ImageField('article/', null=True, blank=True)
    is_vite = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_text.description


class Comment(models.Model):
    author = models.ForeignKey('profile.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author.user.get_full_name():
            return f"{self.author.user.get_full_name()}'s comment"
        return f"{self.author.user.username()}'s comment"
