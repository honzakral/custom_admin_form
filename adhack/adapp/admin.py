from django.contrib import admin
from django.db import models
from django import forms

from adhack.adapp.models import PollOption, Poll

class PollOptionInlineAdmin(admin.TabularInline):
    model = PollOption

class PollAdmin(admin.ModelAdmin):
    inlines = [PollOptionInlineAdmin]

    formfield_overrides = {
        models.TextField: {
            'widget': forms.TextInput
        }
    }

admin.site.register(Poll, PollAdmin)

