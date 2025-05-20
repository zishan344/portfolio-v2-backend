from django.contrib import admin
from my_portfolio.models import ProjectImage,Project,Skill
# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Skill)
