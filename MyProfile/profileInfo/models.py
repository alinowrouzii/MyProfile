from django.db import models
from tinymce.models import HTMLField
import os

main_dir = 'profile'
portfolio_dir = 'portfolio'

def get_upload_path(instance, filename):
    return os.path.join(main_dir, filename)

class Education(models.Model):
    from_date = models.DateField()
    to_date = models.DateField(blank=True) # blank is for when the education not ended yet
    institute =  models.CharField()
    degree = models.CharField()
    
class Profile(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    about = HTMLField(blank=True)
    
    profile_photo = models.ImageField(upload_to=get_upload_path, null=True)
    
    email = models.CharField()
    linkedIn = models.CharField(blank=True)
    github = models.CharField(blank=True)
    stackOverFlow = models.CharField(blank=True)
    facebook = models.CharField(blank=True)
    
    
def get_portfolio_upload_path(instance, filename):
    return os.path.join(main_dir, portfolio_dir, filename)

    
class Portfolio(models.Model):
    title = models.CharField()
    description = models.CharField(blank=True)
    
    photo = models.ImageField(upload_to=get_portfolio_upload_path, null=True)
    
    