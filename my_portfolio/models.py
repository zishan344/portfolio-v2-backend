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
  description = models.TextField(default="")
  display_project = models.BooleanField(default=False)
  project_cover = CloudinaryField('image')
  stack = ArrayField(models.CharField(max_length=50, blank=True), size=15,default=list, null=True,blank=True)
  github_client = models.CharField(max_length=250)
  github_server = models.CharField(max_length=250)
  project_preview =models.CharField(max_length=250)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
      return f"{self.project_name} - {self.project_title}"

  

class ProjectImage(models.Model):
  project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name="images")
  image = CloudinaryField('image')
  def __str__(self):
      return f"Image of {self.project.project_name}"

class Blog(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = CloudinaryField('image')
  display_blog = models.BooleanField(default=False)
  blog_preview = models.CharField(max_length=250)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
      return f"{self.title}"
  