from django.contrib import admin
from .models import *

# Register your models here.



class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'community', 'date_created', 'active')
    list_filter = ('active', 'date_created')
    search_fields = ('user', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class CommunityAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created')
    list_filter = ('tags', 'date_created')
    search_fields = ('title', 'content')
    autocomplete_fields = ('tags',)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(Discussion)
