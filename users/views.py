from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import  get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .models import Profile
from .forms import UserProfileForm

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('explorer:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    """Display User Profile"""
    profile = request.user.profile
    return render(request, 'users/user_profile.html', {
        'profile': profile
    })

@login_required
def edit_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated the Profile Successfully!")
            return HttpResponseRedirect(reverse('users:profile'))

    return render(request, 'users/edit_profile.html', {
        'form': form
    })
