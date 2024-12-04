from django.contrib import admin
from .models import Category, ChatHistory,Customer,Product,Order

from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'GLIMMER'
    site_title = 'Custom Admin Site'
    index_title = 'Welcome to Glimmer Dashboard'

admin.site = CustomAdminSite()



admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ChatHistory)
