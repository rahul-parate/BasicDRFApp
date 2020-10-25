from django.contrib import admin

# Register your models here.
from .models import Profile, ActivityPeriods


class ProfileModelAdmin(admin.ModelAdmin):
    pass


class ActivityPeriodsModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileModelAdmin)

admin.site.register(ActivityPeriods, ActivityPeriodsModelAdmin)