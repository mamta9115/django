from django.contrib import admin
from.models import Contact
@admin.register(Contact)

# Register your models here.
class ContactAdmin(admin.ModelAdmin):

    list_display = ['name','email','message']


