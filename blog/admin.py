
from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_posted', 'author_id', 'content']

admin.site.register(Post,PostAdmin)
