from django.contrib import admin

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'country', 'city')
    search_fields = ('name', 'email', 'message')