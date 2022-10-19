from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=215)
    description = models.TextField(max_length=1000)

    class Meta:
        db_table = "post"
