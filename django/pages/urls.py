from django.urls import path

from .views import AboutPageView, HomePageView, ContactPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home')
]
