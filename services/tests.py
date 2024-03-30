from django.test import TestCase
from services.models import Domain, Service, Lawyer, Booking
from datetime import datetime
from django.urls import reverse


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

    def test_booking_creation_default_comment_is_none(self):
        booking = Booking.objects.create(
            service=self.service,
            lawyer=self.lawyer,
            datetime_start=datetime.now(),
            datetime_end=datetime.now(),
        )

        self.assertIsNone(booking.comment)
        booking.delete()

    def test_lawyer_page_status_200_OK(self):
        url = reverse('lawyer_detailed', kwargs={'pk': self.lawyer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_lawyer_page_status_404_Not_Found(self):
        url = reverse('lawyer_detailed', kwargs={'pk': self.lawyer.pk + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
