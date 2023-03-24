from django.db import models

# Create your models here.
class BaseModel(models.Model):
    ids = models.CharField(primary_key=True,max_length=8)
    name = models.CharField(max_length=32)

    class Meta:
        abstract = True