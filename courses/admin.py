from django.contrib import admin
from courses.models import Courses


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('courses_name_course', 'courses_date_begin', 'courses_date_end')
    models = Courses
admin.site.register(Courses, CoursesAdmin)




