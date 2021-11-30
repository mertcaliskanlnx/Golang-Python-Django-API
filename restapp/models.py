from django.db import models


class bigdata(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    price = models.FloatField(default=1.00)

    def __str__(self):
        return self.title

        