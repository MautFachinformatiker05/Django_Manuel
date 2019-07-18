from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from blog.models import Post



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Your Account created has been created !Congrats {username}! Please login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    context = { 'posts': Post.objects.all() }
    return render(request, 'users/profile.html',context)




