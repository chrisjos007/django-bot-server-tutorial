from django.db import models


class CallCount(models.Model):
    email = models.EmailField()
    fat = models.IntegerField(default=0)
    stupid = models.IntegerField(default=0)
    dumb = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username}"