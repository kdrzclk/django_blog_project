from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate

from .forms import UserForm, UserProfileForm
# UpdateUserForm, UpdateProfileForm, 
from django.contrib.auth.forms import AuthenticationForm

from .models import UserProfile
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.



def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == "POST":
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            messages.success(request, 'Register Succesfully')
            return redirect('home')

    context = {
        'form_user': form_user,
        'form_profile': form_profile
    }
    return render(request, 'registration/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():

        user = form.get_user()

        if user:
            messages.success(request, "Login Succesfully")
            login(request, user)
            return redirect("home")

    return render(request, 'registration/user_login.html', {'form': form})

def user_logout(request):
    messages.success(request, 'You Logged Out')
    logout(request)
    return render(request, 'registration/user_logout.html')

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='users-profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'registration/profile.html', {'user_form': user_form,'profile_form': profile_form })

