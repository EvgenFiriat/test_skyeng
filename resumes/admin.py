from django.contrib import admin

# Register your models here.
from resumes.models import Resume, Specialty

admin.site.register(Resume)
admin.site.register(Specialty)
