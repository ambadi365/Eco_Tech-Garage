from django.contrib import admin
from .models import Service,registerDB,ServiceBooking,Teams,ServiceStatusDetail,Contact
# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceBooking)
admin.site.register(registerDB)
admin.site.register(Teams)
admin.site.register(ServiceStatusDetail)
admin.site.register(Contact)
