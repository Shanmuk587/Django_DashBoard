from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
def panel_dashboard_view(request):
    return render(request, 'panel_dashboard.html')
def panel_chatbot(request):
    return render(request, 'panel_chatbot.html')
def chatbot(request):
    return render(request, 'chatbot.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Passwords are not matching')
            return redirect('register')           
                
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('chatbot')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'login_design2.html')