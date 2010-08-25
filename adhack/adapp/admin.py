from django.contrib import admin

from adhack.adapp import models

class PollOptionInlineAdmin(admin.TabularInline):
    model = models.PollOption

class PollAdmin(admin.ModelAdmin):
    inlines = [PollOptionInlineAdmin]

admin.site.register(models.Poll, PollAdmin)

