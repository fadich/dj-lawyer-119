from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(
        request=request,
        template_name='homepage.html',
        context={
            "name": "Gandalf",
            "lawyers": ["Tanya", "Frodo", "Gandalf"],
        },
    )

    # return HttpResponse(b'Hello Gandalf!!!')
