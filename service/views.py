from django.contrib import auth
from django.contrib.messages.api import info
from django.db.models.fields import related
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Profile,Client
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def orderpromotion(request):
    return render(request,'hero_order.html')

def workerlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found!')
            return redirect('/login')
        
        profile_obj = Profile.objects.filter(user = user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Incorrect username or password')
            return redirect('/login')
        
        else:
            login(request , user)
            return redirect('/dashboard')
        
    return render(request,'login.html')
                
# champ connect here
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Condition to check if user already exist
        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username already taken!')
                return redirect('/reg')
        
            if User.objects.filter(email = email).first():
                messages.success(request, 'Email already taken!')
                return redirect('/reg')
        
            user_obj = User.objects.create(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_verification_email(email , auth_token)
            return redirect('/token')
        
        except Exception as e:
            print(e)
        
    return render(request,'register.html')

def deliver_token(request):
    return render(request,'send_token.html')

def token_success(request):
    return render(request,'success.html')

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')


def packages(request):
    return render(request,'package.html')

def error(request):
    return render(request,'error.html')

@login_required(login_url='/login')
def user_profile(request):
    return render(request,'dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    
def user_tasks(request):
    return render(request,'user_task.html')

def send_verification_email(email , token):
    subject = 'Growy - Account Verification'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from , recipient_list )
    
# client connnect here
def client_connect(request):
    if request.method == 'POST':
        client_email = request.POST.get('email')
        client_password = request.POST.get('password')
        try:
            # check if email exists
            if Client.objects.filter(client_email = client_email).first():
                messages.success(request, 'Email already exist!')
                return redirect('/connect')
            
            client_obj = Client(client_email = client_email, client_password = client_password)
            client_obj.save()
        
            return render(request,'order-promo.html')
                
        except Exception as e:
            print(e)
       
    return render(request,'client_reg.html')

def client_login(request):
    if request.method == 'POST':
        client_email = request.POST.get('email')
        client_password = request.POST.get('password')
        client = auth.authenticate(client_email = client_email , client_password = client_password)
        
        client_obj = Client.objects.filter(client_email = client_email).first()
        if client_obj is None:
            messages.success(request,'Hero not found!')
            return redirect('/herologin')
       
        if client is None:
            messages.success(request, 'Incorrect username or password')
            return redirect('/herologin')
        
        else:
            auth.login(request, client)
            return redirect('/order')
            
    return render(request,'client_login.html')

def hero_panel(request):
    return render(request,'hero_panel.html')
    
    