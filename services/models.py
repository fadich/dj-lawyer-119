from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)

class Service(models.Model):
    name = models.CharField(max_length=256)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='services')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = (
            ('name', 'domain'),
        )


# class Lawyer(models.Model):
#     name = models.CharField(max_length=256)
#     experience = models.CharField(max_length=256)
#     description = models.TextField()
#     location = models.CharField(max_length=256)
#     specialisation = models.CharField(max_length=256)
#     services = models.TextField()



