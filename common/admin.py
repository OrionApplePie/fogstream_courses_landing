from django.contrib import admin
from .models import Feedback
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.core.mail import EmailMessage
from django.contrib import messages


def send_answer(adminmodel, request, queryset):
    for contact in queryset:
        if contact.answer:
            send_mail('Ответ', [contact.answer], 'from@example.com', [contact.email], fail_silently=False)
        adminmodel.message_user(request, "Mail sent successfully ")
    send_answer.short_description = "Послать e-mail выбранным контактам"


class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email", "subject", "timestamp"]
    list_filter = ["subject", "timestamp"]
    search_fields = ["subject", "message"]
    actions = [send_answer]

    class Meta:
        model = Feedback

    # A template for a customized change view:
    change_form_template = 'common/change_form.html'

    def response_change(self, request, obj):
        opts = self.model._meta
        pk_value = obj._get_pk_val()
        preserved_filters = self.get_preserved_filters(request)

        if "_send_answer" in request.POST:
            # handle the action on your obj
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
            self.message_user(request, "Answer is sended")
            redirect_url = reverse('admin:%s_%s_change' %
                               (opts.app_label, opts.model_name),
                               args=(pk_value,),
                               current_app=self.admin_site.name)
            redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
            return HttpResponseRedirect(redirect_url)
        else:
            return super(FeedbackModelAdmin, self).response_change(request, obj)

admin.site.register(Feedback, FeedbackModelAdmin)
