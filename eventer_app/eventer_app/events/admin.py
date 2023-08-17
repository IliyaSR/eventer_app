from django.contrib import admin
from eventer_app.events.models import EventModels


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(EventModels, EventAdmin)
