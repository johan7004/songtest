from django.contrib import admin
from .models import Songs 
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'number',)
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Songs, ArticleAdmin)