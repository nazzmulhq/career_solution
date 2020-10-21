from django.contrib import admin
from BlogSite.models import *
# Register your models here.
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
