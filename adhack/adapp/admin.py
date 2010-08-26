from django.contrib import admin
from django.db import models
from django import forms

from adhack.adapp.models import PollOption, Poll

class PollOptionInlineAdmin(admin.TabularInline):
    model = PollOption

class PollAdmin(admin.ModelAdmin):
    inlines = [PollOptionInlineAdmin]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'question':
            return forms.RegexField('\?$', error_messages={'invalid': "Question must end with '?'!"})

        return super(PollAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Poll, PollAdmin)

