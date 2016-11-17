from django.contrib import admin
from registration.models import  Party


class PartyAdmin(admin.ModelAdmin):
    list_display = ('party_name', 'party_fullname', 'party_login')
    models = Party
admin.site.register(Party, PartyAdmin)
