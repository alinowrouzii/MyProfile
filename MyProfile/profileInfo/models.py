from django.db import models
from tinymce.models import HTMLField
from django.utils.timezone import localtime

import os

main_dir = 'profile'
portfolio_dir = 'portfolio'

def get_upload_path(instance, filename):
    return os.path.join(main_dir, filename)

class Education(models.Model):
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True) # blank is for when the education not ended yet
    institute =  models.CharField(max_length=500)
    degree = models.CharField(max_length=500)
    
    def get_from_date(self):
        return self.from_date.strftime("%b %Y")

    def get_to_date(self):
        if self.to_date:
            return self.to_date.strftime("%b %Y")
        else:
            return "to now"
    
class Profile(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    about = HTMLField(blank=True)
    
    profile_photo = models.ImageField(upload_to=get_upload_path, null=True)
    
    email = models.CharField(max_length=500)
    linkedIn = models.CharField(max_length=500, blank=True)
    github = models.CharField(max_length=500, blank=True)
    stackOverFlow = models.CharField(max_length=500, blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    
    
def get_portfolio_upload_path(instance, filename):
    return os.path.join(main_dir, portfolio_dir, filename)

    
class Portfolio(models.Model):
    title = models.CharField(max_length=500)
    description = HTMLField(blank=True)
    
    photo = models.ImageField(upload_to=get_portfolio_upload_path, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_local_date(self):
        return localtime(self.created_at).strftime("%b %d %Y, %H:%M:00")
