from typing import Iterable
from django.http import HttpResponse
from django.shortcuts import render
from .models import Lawyer


def homepage(request):
    lawyers: Iterable[Lawyer] = Lawyer.objects.all()  # QuerySet

    return render(
        request=request,
        template_name='homepage.html',
        context={
            "lawyers": lawyers,
        },
    )

    # return HttpResponse(b'Hello Gandalf!!!')


def about_us(request):
    return render(
        request=request,
        template_name='about_us.html',
    )
