from django.contrib import admin
from eventer_app.profiles.models import ProfileModel


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProfileModel, ProfileAdmin)
