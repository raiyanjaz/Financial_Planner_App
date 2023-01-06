from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages, auth
from login.models import Account

# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'html/landingPage.html')
    
class signUp(View):
    def get(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            
            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'It looks like the email is already in use with MYRAY')
                    return redirect('signUp/')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'It looks like the username is already in use with MYRAY')
                    return redirect('registration/login/registration/signUp/')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    
                    user_model = User.objects.get(username=username)
                    new_profile = Account.objects.create(user=user_model, id_user=user_model.id)
                    new_profile.save()
                    return redirect('registration/login/')
            else:
                messages.info(request, 'Passwords do not match.')
                return redirect('registration/login/')
        else: 
            return render(request, 'html/signUp.html')