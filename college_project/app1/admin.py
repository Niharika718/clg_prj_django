from django.contrib import admin

# Register your models here.
from .models import department,faculty,student,course

admin.site.register(department)
admin.site.register(faculty)
admin.site.register(course)
admin.site.register(student)