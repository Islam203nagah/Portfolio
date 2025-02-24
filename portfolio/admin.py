from django.contrib import admin
from .models import (About,
    ResumeItem,Service,SiteStatistic,
    Skill, Project, BlogPost, ContactMessage
)


admin.site.register(About)
admin.site.register(ResumeItem)
admin.site.register(SiteStatistic)
admin.site.register(Service)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(BlogPost)
admin.site.register(ContactMessage)

