from django.contrib import admin
from myapp.models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'credit']
    list_filter = ['grade',]
