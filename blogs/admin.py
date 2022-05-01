from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'in_archive']
    list_filter = ['title', 'in_archive']


admin.site.register(Comments)
admin.site.register(ReplyToComment)
admin.site.register(ReplyToReply)

