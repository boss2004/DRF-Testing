from django.contrib import admin
from app.models import (
    Tag,
    Category,
    Post,
    User,
)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(User)