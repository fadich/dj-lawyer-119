from django.contrib import admin

from services import models


@admin.register(models.Domain)
class DomainAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'domain',
        'price',
    )


class LawyerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
    )


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'service',
        'lawyer',
        'datetime_start',
        'datetime_end',
    )


admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Lawyer, LawyerAdmin)
admin.site.register(models.Booking, BookingAdmin)


