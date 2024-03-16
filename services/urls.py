from django.urls import path

from services.views import homepage


urlpatterns = [
    path('', homepage, name='homepage'),
]
