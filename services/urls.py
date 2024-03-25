from django.urls import path

from services.views import HomepageView, about_us, LawyerDetailView, SignUpView


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('about-us', about_us, name='about_us'),
    path('lawyers/<int:pk>', LawyerDetailView.as_view(), name='lawyer_detailed'),
    path('signup', SignUpView.as_view(), name='signup')
]
