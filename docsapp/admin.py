from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'access', 'created_at')
    list_filter = ('access',)
    search_fields = ('title', 'slug', 'description')
