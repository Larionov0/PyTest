from django.contrib import admin

# Register your models here.
from .models import Pack, Question

admin.site.register(Pack)
admin.site.register(Question)
