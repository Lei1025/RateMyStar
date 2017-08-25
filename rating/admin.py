from django.contrib import admin

# Register your models here.
from rating.models import *

admin.site.register(Article)
admin.site.register(R_User)
admin.site.register(Comment)