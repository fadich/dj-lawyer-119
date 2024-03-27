from datetime import datetime
from typing import Iterable

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
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


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup_form'] = UserCreationForm()
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, user=form.instance)
            return HttpResponseRedirect(reverse("homepage"))
        context = self.get_context_data()
        context['signup_form'] = form
        return self.render_to_response(context=context)


class SignOutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request=request)
        return HttpResponseRedirect(reverse("homepage"))


class SignInView(TemplateView):
    template_name = 'signin.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("homepage"))
        context = self.get_context_data()
        context['error'] = 'Invalid Credentials!'
        context['username'] = username
        return self.render_to_response(context=context)
