from django.contrib import admin
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cid', 'name', 'age', 'loan', 'years', 'email')  # Customize fields to display in admin list view
admin.site.register(Customer, CustomerAdmin)
