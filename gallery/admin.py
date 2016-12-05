from django.contrib import admin
from gallery.models import Album, Photo


class PhotoAdmin(admin.TabularInline):
    list_display = ('photo_title', 'image_img')
    readonly_fields = ['image_img', ]
    model = Photo
    extra = 3


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_title', )
    model = Album
    inlines = [PhotoAdmin]
admin.site.register(Album, AlbumAdmin)



