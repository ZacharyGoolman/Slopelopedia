from django.contrib import admin
from .models import Location   
from .models import Comment
from.models import Reply


# Register your models here.
admin.site.register(Location)
admin.site.register(Comment)
admin.site.register(Reply)

