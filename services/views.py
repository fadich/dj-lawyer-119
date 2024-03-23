from typing import Iterable

# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Lawyer


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

