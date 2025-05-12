from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form':form})

@login_required
def home_view(request):
    return render(request, 'accounts/home.html')

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})


User = get_user_model()

# @login_required
# def profile_edit_view(request):
#     if request.method == 'POST':
#         user = request.user
#         user.username = request.POST['username']
#         user.email = request.POST['email']
#         user.save()
#         messages.success(request, 'Profile updated successfully.')
#         return redirect('edit_profile')

#     return render(request, 'accounts/edit_profile.html')


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('edit_profile')
        
    else:
            form = CustomUserChangeForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})