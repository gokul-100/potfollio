from django.contrib import admin
from .models import Post,Comment,TagLine,Author
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(TagLine)
admin.site.register(Author)

# Register your models here.
