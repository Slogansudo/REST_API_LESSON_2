from django.contrib import admin
from .models import Artist, Album, Songs
# Register your models here.

admin.site.register([Artist, Album, Songs])

