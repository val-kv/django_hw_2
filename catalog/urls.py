from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('admin/', admin.site.urls),
]