from django.forms import ModelForm
from services.models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            'datetime_start',
            'datetime_end',
            'service',
            'comment',
        ]

