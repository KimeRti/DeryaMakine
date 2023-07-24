from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signin', views.signin, name='login'),
    path('signup', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path("activate/<uidb64>/<token>/", views.activate, name='activate'),
    path('logout', views.logout_request, name='logout'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_confirm'),
]