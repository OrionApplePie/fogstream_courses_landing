from django.contrib import admin
from courses.models import Course


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_begin', 'date_end')
    models = Course
admin.site.register(Course, CoursesAdmin)




