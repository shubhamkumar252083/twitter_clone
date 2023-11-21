from django.contrib import admin

# Register your models here.
from .models import *

class CommentsAndStatusAdmin(admin.ModelAdmin):

    def user_id_detail(self, obj):
        return obj.user_id.email

    list_display = ["id", "user_id_detail","status", "tweet_id"]

admin.site.register(Tweet)
admin.site.register(CommentsAndStatus, CommentsAndStatusAdmin)
admin.site.register(Hashtag)