from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=256)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='services')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = (
            ('name', 'domain'),
        )

    def __str__(self):
        return self.name


class Lawyer(models.Model):
    name = models.CharField(max_length=256)
    experience = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    specialisation = models.CharField(max_length=256, null=True, blank=True)
    services = models.ManyToManyField(to=Service, related_name='lawyers', blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='bookings')
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.datetime_start} - {self.lawyer}'
