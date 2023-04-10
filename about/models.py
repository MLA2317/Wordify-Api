from django.db import models


class About(models.Model):
    full_name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='about/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
