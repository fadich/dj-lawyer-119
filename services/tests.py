from django.test import TestCase
from services.models import Domain, Service, Lawyer, Booking
from datetime import datetime


class BookingTestCase(TestCase):
    def setUp(self):
        self.domain = Domain.objects.create(name='Dark Magic')
        self.service = Service.objects.create(name='Revival', domain=self.domain, price=3000)
        self.lawyer = Lawyer.objects.create(name='Sauron', experience=10)
        self.lawyer.services.add(self.service)

    def tearDown(self):
        self.lawyer.delete()
        self.service.delete()
        self.domain.delete()

    def test_booking_creation(self):
        booking = Booking.objects.create(
            service=self.service,
            lawyer=self.lawyer,
            datetime_start=datetime.now(),
            datetime_end=datetime.now(),
        )

        self.assertIsNone(booking.comment)
        booking.delete()
