from django.contrib import admin
from .models import Customer,Lead,Opportunity,Interaction,Product,Sale,Contact

# Register your models here.
admin.site.register(Customer)
admin.site.register(Lead)
admin.site.register(Opportunity)
admin.site.register(Interaction)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Contact)
