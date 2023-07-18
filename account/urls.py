from django.urls import path
from . import views


urlpatterns = [
    path('signin', views.signin, name='login'),
    path('signup', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('forgot', views.forgot, name='forgot'),
    path("activate/<uidb64>/<token>/", views.activate, name='activate'),
    path('logout', views.logout_request, name='logout')
]