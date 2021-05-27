from django.contrib import admin

# Register your models here.
from .models import Contact


# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Mobile', 'Email','Message')
    list_filter = ("Name",)
    search_fields = ['email', 'content']
    # prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Contact, ContactAdmin)
