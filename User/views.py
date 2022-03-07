from django.shortcuts import render,redirect
from .models import Destinations,Profile

# Create your views here.

def index(request):
    city = Destinations.objects.all()
    return render(request, 'User/index.html',{'city': city})

def deleteProfile(request):
    Profile.objects.filter(user = request.user).delete()
    return redirect('/')

def CreateProfile(request):
    form = ProfileForm()
    message = ''
    if request.method == "POST":
        if form.is_valid():
            form.save()
            message = "Profile Create sucessfull"       
    return render(request, 'User/profile.html', {'form': form,'message': message})

def EditProfile(request):
    message = ''
    try:
        profile_form = ProfileForm(instance=request.user.profile)
    except:
        profile_form = ProfileForm()
    if request.method == "POST":
        if form.is_valid():
            form.save(commit=False)
            message = "Profile Update sucessfull"       
    return render(request, 'User/profile.html', {'form': profile_form,'message': message})

def UserProfileDetails(request):
    return
    