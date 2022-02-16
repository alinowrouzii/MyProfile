from django.contrib import admin

from profileInfo.models import Education, Profile, Portfolio

# Register your models here.


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # list_display = ['id', 'title']
    list_display = ["full_name"]

    def full_name(self, obj):
        return obj.first_name + " " + obj.last_name


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
