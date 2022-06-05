from django.urls import path, reverse_lazy
from .views import register, user_login, user_logout
#  profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name="logout"),
    
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html") , name="change-password"),
    
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset-password.html'), name='reset-password'),

    # path('profile/', profile, name='profile'),
]