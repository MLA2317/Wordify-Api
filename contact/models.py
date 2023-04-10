from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name}'s request"

