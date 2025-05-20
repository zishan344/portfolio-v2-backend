from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
# from django.contrib.postgres.fields import ArrayField
# Create your models here.



class Skill(models.Model):
  frontend =ArrayField(models.CharField(max_length=50), size=15)
  backend =ArrayField(models.CharField(max_length=50), size=10)
  database =ArrayField(models.CharField(max_length=50), size=5)
  devOps  =ArrayField(models.CharField(max_length=50), size=10)
  Others  =ArrayField(models.CharField(max_length=50), size=15)
  

class Project(models.Model):
  project_name = models.CharField(max_length=50)
  project_title = models.CharField(max_length=100)
  project_cover = CloudinaryField('image')
  stack = ArrayField(models.CharField(max_length=50), size=15)
  github_client = models.CharField(max_length=250)
  github_server = models.CharField(max_length=250)
  github_preview =models.CharField(max_length=250)
  created_at = models.DateTimeField(default=timezone.now)
  
class ProjectImage(models.Model):
  project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name="images")
  image = CloudinaryField('image')
  def __str__(self):
      return f"Image of {self.project.project_name}"