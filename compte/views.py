from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Account
from . import forms

# Create your views here.

class SignUpFormView(UserPassesTestMixin, View):
    template_name = 'accounts/signup.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.user_type == 'ADMIN'
    

    def get(self, request, *args, **kwargs):
        form = forms.SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            user     = Account.objects.create_user(username=username, password=password, user_type=user_type)
            login(request,  user)
        else:
            return render(request, self.template_name, {'form': form})

        return redirect('list-user')

class SignInFormView(View):
    template_name = 'accounts/signin.html'

    def get(self, request, *args, **kwargs):
        form = forms.SignInForm()
        return render(request, self.template_name, {'form': form})

    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile-detail', user.pk)
        else:
            form = forms.SignInForm(request.POST)
            return render(request, self.template_name, {'form': form})

class ProfileFormView(LoginRequiredMixin, View):
    
    template_name= 'accounts/profile.html'


    def get(self, request, *args, **kwargs):
        form = forms.ProfileForm(instance=request.user)
        ctx = {'form': form, 'title': request.user.username}

        return render(request, self.template_name, ctx)
    
    def post(self, request, *args, **kwargs):
        form = forms.ProfileForm(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('users')
       
        return render(request, self.template_name, {'form': form})

class UserListView(LoginRequiredMixin, View):
    template_name = 'accounts/list.html'

    def get(self, request, *args, **kwargs):
        action = request.GET.get('action', False)
        pk = request.GET.get('pk', False)
    
        try:
            user = Account.objects.get(pk=pk)
            if action == 'delete':
                user.delete()
                return redirect('users')
        except Account.DoesNotExist:
            queryset = Account.objects.all()
            ctx = {
                'queryset': queryset
            }

            return render(request, self.template_name, ctx)



    

def logout_user(request):
    logout(request)
    return redirect('login')   

