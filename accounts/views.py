from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form, UserCreationForm, UpdateUserForm
from django.contrib.auth import  authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def doctors_list(request):
    doctors = User.objects.all() # Query set

    return render(request, 'user/doctors_list.html', {'doctors': doctors })


def doctors_detail(request, slug):
    doctors_detail = Profile.objects.get(slug = slug) # Query set

    return render(request, 'user/doctors_detail.html', {'doctors_detail': doctors_detail })



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('accounts:doctors_list')

    else:
        form = Login_Form()

    return render(request, 'user/login.html', {'form': form })

def signup(request):
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
            username = form.clean_data.get('username')
            password = form.clean_data.get('password')
            user = authenticate(request, username = username, password = password)
            login(request,user)
            return redirect('accounts:doctors_list')
    else:
        form = UserCreationForm()

    return render(request, 'user/signup.html', {'form': form })


@login_required()
def myprofile(request):

    user_form = UpdateUserForm(instance= request.user)
    return render(request, 'user/update_profile.html', {'user_form':user_form})




def update_profile(request):

    user_form = UpdateUserForm(instance=request.user)

    if request.method == "POST":
            user_form = UpdateUserForm(request.POST,instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('accounts:doctors_list')


    return render(request, 'user/update_profile.html', {'user_form':user_form})
