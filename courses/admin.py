from django.contrib import admin
from courses.models import Courses, Party


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('courses_name_course', 'courses_date_begin', 'courses_date_end')
    models = Courses
admin.site.register(Courses, CoursesAdmin)


class PartyAdmin(admin.ModelAdmin):
    list_display = ('party_name', 'party_fullname', 'party_login')
    models = Party
admin.site.register(Party, PartyAdmin)

