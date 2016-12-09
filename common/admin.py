from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.core.mail import EmailMessage

from .models import HeadPicture, OurTeam

from .models import Feedback


class FeedbackModelAdmin(admin.ModelAdmin):
    """
    Class for list of feedback questions
    """
    list_display = ("__str__", "email", "subject", "timestamp", "is_reply")
    list_filter = ("subject", "timestamp")
    search_fields = ("subject", "message")

    class Meta:
        model = Feedback

    # A template for a customized change view:
    change_form_template = 'common/change_form.html'

    def response_change(self, request, obj):
        """
        Function for sending answer
        """
        opts = self.model._meta
        pk_value = obj._get_pk_val()
        preserved_filters = self.get_preserved_filters(request)

        if "_send_answer" in request.POST:
            contact_name = request.POST.get('name', '')
            contact_mail = request.POST.get('email', '')
            email = EmailMessage(
                "Курсы Python/Django",
                obj.answer,
                "from@example.com",
                [contact_mail],
                reply_to=['example@example.ru'],
                headers={'Reply-To': contact_mail}
            )
            email.send()
            obj.is_reply = True
            obj.save()
            self.message_user(request, "Ответ отослан")
            redirect_url = reverse('admin:%s_%s_change' %
                               (opts.app_label, opts.model_name),
                               args=(pk_value,),
                               current_app=self.admin_site.name)
            redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
            return HttpResponseRedirect(redirect_url)
        else:
            return super(FeedbackModelAdmin, self).response_change(request, obj)




class HeadImageAdmin(admin.ModelAdmin):
    list_display = ('title','image', 'image_img','interval', 'priority')

class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'photo', 'image_img')


admin.site.register(Feedback, FeedbackModelAdmin)
admin.site.register(HeadPicture, HeadImageAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
