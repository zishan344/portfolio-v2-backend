from django.contrib import admin
from my_portfolio.models import ProjectImage,Project,Skill,Blog
# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Skill)
admin.site.register(Blog)
