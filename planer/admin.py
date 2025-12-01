from django.contrib import admin
from planer.models import PersonalUser

@admin.register(PersonalUser)
class PersonalUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'create_date', 'status', 'description')