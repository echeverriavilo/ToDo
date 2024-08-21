from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from ..forms import ProfileForm
from ..models import UserProfile



class UserRegistrationView(View):
    def get(self, request, *args, **kwargs):
        user_form = UserCreationForm()
        profile_form = ProfileForm()
        return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})
    
    def post(self, request, *args, **kwargs):
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print("User Form Data:", user_form.data)
        print("Profile Form Data:", profile_form.data)
        
        if user_form.is_valid():
            print("User Form Valid")
        else:
            print("User Form Errors:", user_form.errors)
        
        if profile_form.is_valid():
            print("Profile Form Valid")
        else:
            print("Profile Form Errors:", profile_form.errors)
            
            
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
        return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile_detail.html'

    def get_object(self, queryset=None):
        return self.request.user.profile
    
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileForm
    template_name = 'profile_form.html'
    success_url = reverse_lazy('profile_detail')
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    
