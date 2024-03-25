from datetime import datetime
from typing import Iterable

from django.db.models import Q
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .forms import BookingForm
from .models import Lawyer, Booking


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lawyers'] = Lawyer.objects.all()
        return context


# def homepage(request):
#     lawyers: Iterable[Lawyer] = Lawyer.objects.all()  # QuerySet
#
#     return render(
#         request=request,
#         template_name='homepage.html',
#         context={
#             "lawyers": lawyers,
#         },
#     )

    # return HttpResponse(b'Hello Gandalf!!!')


def about_us(request):
    return render(
        request=request,
        template_name='about_us.html',
    )


class LawyerDetailView(DetailView):
    model = Lawyer
    template_name = 'lawyer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Booking.objects \
            .filter(
                Q(lawyer=self.object) &
                Q(datetime_end__gte=datetime.now())
            ) \
            .order_by('datetime_start') \
            .all()
        context['booking_form'] = BookingForm()  # TODO: implement booking form logic

        # print(context['bookings'].query)
        return context



