from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'due_date', 'priority', 'status')
    list_filter = ('priority', 'status', 'project', 'due_date')
    search_fields = ('title', 'description') 