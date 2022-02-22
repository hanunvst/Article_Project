
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.http import HttpResponse
from django.contrib import messages

from users.models import Profile
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
        else:
            username = form.cleaned_data.get('username')
            messages.warning(request,f'Account not created for {username}.Try again!')
            return redirect('register')

    else:
        form = UserRegisterForm()
        context = {'form' : form}
        return render(request, 'users/register.html', context)


@login_required
def profile_view(request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            "u_form" : u_form,
            "p_form" : p_form
        }
        return render(request, 'users/profile.html', context)



