from django.db import models
from tinymce.models import HTMLField

# Create your models here.

def get_value(key):
    try:
        return StaticData.objects.get(key=key).value
    except:
        return None

class StaticData(models.Model):
    key = models.CharField(max_length=500, unique=True)
    value = HTMLField(blank=True)