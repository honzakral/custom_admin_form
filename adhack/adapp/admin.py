from django.contrib import admin
from django.db import models
from django import forms

from adhack.adapp.models import PollOption, Poll

class MyWhackyForm(forms.Form):
    subject = forms.CharField(max_length=30)
    adverb = forms.CharField(max_length=30)
    adjective =  forms.CharField(max_length=30)

    options = forms.CharField(widget=forms.Textarea)

    def __init__(self, data=None, files=None, instance=None, **kwargs):
        self._instance = instance
        super(MyWhackyForm, self).__init__(data, files, **kwargs)

    def save_m2m(self):
        opts = self.cleaned_data['options'].split('\n')
        for opt in opts:
            self._instance.polloption_set.create(text=opt.strip())


    def save(self, commit=True):
        obj = self._instance or Poll()

        obj.name = self.cleaned_data['subject']
        obj.question = 'Do you really think %(subject)s is %(adverb)s %(adjective)s?' % self.cleaned_data
        if commit:
            obj.save()

        self._instance = obj

        return obj

class PollAdmin(admin.ModelAdmin):
    list_display = ('name','question', )
    declared_fieldsets = [
        (None, {'fields': ('subject', )}),
        ('Extra', {'fields': (('adverb', 'adjective',), )}),
        ('Options', {'fields': ('options', )}),
    ]

    def get_form(self, request, obj=None, **kwargs):
        return MyWhackyForm

admin.site.register(Poll, PollAdmin)

