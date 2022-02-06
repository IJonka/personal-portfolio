from django.db import models

class Bloging(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=False)
    description = models.TextField(max_length=1250)

    def __str__(self):
        return self.title
