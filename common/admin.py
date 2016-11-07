from django.contrib import admin
from .models import Feedback
from django.core.mail import send_mail


def send_answer(adminmodel, request, queryset):
    for contact in queryset:
        if contact.answer:
            send_mail('Ответ', [contact.answer], 'from@example.com', [contact.email], fail_silently=False)
        adminmodel.message_user(request, "Mail sent successfully ")
    send_answer.short_description = "Послать e-mail выбранным контактам"


class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email", "subject", "timestamp", "message", "answer"]
    list_filter = ["subject", "timestamp"]
    search_fields = ["subject", "message"]
    actions = [send_answer]

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackModelAdmin)


from .models import HeadPicture, OurTeam
# Register your models here.

class HeadImageAdmin(admin.ModelAdmin):
    list_display = ('title','image', 'image_img','interval', 'priority')

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'photo', 'image_img')

admin.site.register(HeadPicture, HeadImageAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
