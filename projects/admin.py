from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'get_tasks_count')
    list_filter = ('created_at', 'owner')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'

    def get_tasks_count(self, obj):
        return obj.get_tasks_count()
    get_tasks_count.short_description = 'Total de Tarefas' 