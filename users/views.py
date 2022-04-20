from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Register new user"""
    if request.method != 'POST':
        # display a blank form
        form = UserCreationForm()
    else:
        # process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:index')

    # display blank/invalid forms
    context = {'form': form}
    return render(request, 'registration/register.html', context)
