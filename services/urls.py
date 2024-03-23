from django.urls import path

from services.views import homepage, about_us


urlpatterns = [
    path('', homepage, name='homepage'),
    path('about-us', about_us, name='about_us')
]
