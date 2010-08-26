from django.contrib import admin
from django.db import models
from django import forms

from adhack.adapp.models import PollOption, Poll

class PollOptionInlineAdmin(admin.TabularInline):
    model = PollOption

class MyWhackyForm(forms.Form):
    name = forms.CharField(max_length=30)

    def __init__(self, data=None, files=None, instance=None, **kwargs):
        self._instance = instance

        initial = kwargs.setdefault('initial', {})
        if instance:
            initial['name'] = instance.name

        super(MyWhackyForm, self).__init__(data, files, **kwargs)

    def save_m2m(self):
        pass

    def save(self, commit=True):
        obj = self._instance or Poll()

        obj.name = self.cleaned_data['name']
        obj.question = 'Do you really think %s is true?' % self.cleaned_data['name']
        if commit:
            obj.save()

        return obj

class PollAdmin(admin.ModelAdmin):
    inlines = [PollOptionInlineAdmin]
    list_display = ('name','question', )

    def get_form(self, request, obj=None, **kwargs):
        return MyWhackyForm

admin.site.register(Poll, PollAdmin)

