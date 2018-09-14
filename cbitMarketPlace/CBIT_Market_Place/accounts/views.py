from __future__ import unicode_literals

from django.shortcuts import render,redirect
from accounts.forms import (
	RegistrationForm,
	EditProfileForm,
	)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .forms import EditProfileForm,ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request,'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            form.save()
            return redirect('accounts:login')
    else:
        form = RegistrationForm()


    return render(request,'accounts/reg_form.html',{'form':form})

def profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)


# def edit_profile(request):
#     if request.method=='POST':
#         form=EditProfileForm(request.POST,request.FILES,instance=request.user)
#         form1 = ProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
#         if form.is_valid() and form1.is_valid():
#             u=form.save()
#             p=form1.save(commit=False)
#             p.user=request.user
#             if 'pic' in request.FILES:
#                 p.pic=request.FILES['pic']
#
#                 p.save()
#                 u.save()
#                 return redirect('/accounts/profile')
#
#     else:
#         form=EditProfileForm(instance=request.user)
#         form1=ProfileForm(instance=request.user.userprofile)
#
#     return render(request,'accounts/update_profile.html',{'form':form,'form1':form1})

def edit_profile(request):
	if request.method=='POST':
		form=EditProfileForm(request.POST,request.FILES,instance=request.user)
		form1 = ProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
		if form.is_valid() and form1.is_valid():
			u=form.save()
			p=form1.save(commit=False)
			p.user=request.user
			if 'pic' in request.FILES:
				p.pic=request.FILES['pic']

			p.save()
			u.save()
			return redirect('/accounts/profile')

	else:
		form=EditProfileForm(instance=request.user)
		form1=ProfileForm(instance=request.user.userprofile)

		return render(request,'accounts/update_profile.html',{'form':form,'form1':form1})
