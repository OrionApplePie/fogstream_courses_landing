from django.contrib import admin
from .models import HeadPicture, OurTeam
# Register your models here.

class HeadImageAdmin(admin.ModelAdmin):
    list_display = ('title','image', 'image_img','interval', 'priority')

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'photo', 'image_img')

admin.site.register(HeadPicture, HeadImageAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
