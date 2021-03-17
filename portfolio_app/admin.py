from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certificate)
admin.site.register(Contact)

