from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class ProjectImage(models.Model):
  name = models.CharField(max_length=50)
  image = CloudinaryField('image')
  def __str__(self):
      return self.name
  

""" class Project(models.Model):
  project_name = models.CharField(max_length=50)
  project_title = models.CharField(max_length=100)
  # project_cover = image field
  # project_images = image table
  # technology = models. //should be add array
  github_client = models.models.CharField()
  github_server = models.models.CharField()
  github_preview = models.models.CharField() """
  
