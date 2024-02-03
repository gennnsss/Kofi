from django.contrib import admin
from .models import Customer, Product, Order, Group, Return, Review, Payment

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Group)
admin.site.register(Return)
admin.site.register(Review)
admin.site.register(Payment)