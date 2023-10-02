from django.shortcuts import render ,HttpResponseRedirect,HttpResponse
from .forms import Signup,CustomUserForm,CustomAdminForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User

def signup(req):
   if req.method=="POST":
      fm=Signup(req.POST)
      if fm.is_valid():
         messages.success(req,"Account Created Successfully !! ")
         fm.save()
   else:
        fm=Signup()
   return render(req,'signup.html',{'form':fm})   
      

def formdata(req):
    if req.method=='POST':
        form=Signup(req.POST)
        print(form)
        if form.is_valid():
            print("form validate")
            print("first name is : ",req.POST['fname'])
            print('Email is : ',form.cleaned_data['email'])
            print('Contact is : ',form.cleaned_data['contact'])
            print('Password is : ',form.cleaned_data['password'])
            # form.save()
            messages.success(req,'RECORD SUBMITTED')
            form=Signup()
    else:
        form=Signup()
    return render(req,'signup.html',{'form':form})            

def Login(req):
    if not req.user.is_authenticated:
    # if not user1:
        if req.method=="POST":
            fm=AuthenticationForm(request=req,data=req.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                passw=fm.cleaned_data['password']
                user=authenticate(username=uname,password=passw)
                if user is not None:
                    login(req,user)
                    messages.success(req,'Logged In Successfully !! ')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=AuthenticationForm()
        return render(req,'login.html',{'form':fm}) 
     
    else:
     return HttpResponseRedirect('/dashboard/')      

def Dashboard(req):
    if req.user.is_authenticated:
        if req.method=="POST":
            if req.user.is_superuser==True:
                fm=CustomAdminForm(req.POST,instance=req.user)
                users=User.objects.all()
            else:
              fm=CustomUserForm(req.POST,instance=req.user)
              users=None
            if fm.is_valid():
                messages.success(req,'Profile Updated !! ')
                fm.save()
        else: 
            if req.user.is_superuser==True:                
                fm=CustomAdminForm(instance=req.user)
                users=User.objects.all()
            else:    
                fm=CustomUserForm(instance=req.user)
                users=None
        return render(req,'dashboard.html',{'name':req.user.username,'form':fm,'users':users})
            
    else:
        return HttpResponseRedirect('/login/')


def Logout(req):
    logout(req)
    return HttpResponseRedirect('/login/')

def Changepassword(req):
    if req.user.is_authenticated:
        if req.method=="POST":
            fm=PasswordChangeForm(user=req.user,data=req.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(req,fm.user)
                messages.success(req,'Password Changed Successfully')
                return HttpResponseRedirect('/dashboard/')
        else:
            fm=PasswordChangeForm(user=req.user)
        return render(req,"passwordchange.html",{'form':fm})
    else:
        return HttpResponseRedirect('/login/') 


def Resetpassword(req):
    if req.user.is_authenticated:
        if req.method=="POST":
            fm=SetPasswordForm(user=req.user,data=req.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(req,fm.user)
                messages.success(req,'Password Changed Successfully')
                return HttpResponseRedirect('/dashboard/')
        else:
            fm=SetPasswordForm(user=req.user)
        return render(req,"resetpass.html",{'form':fm})
    else:
        return HttpResponseRedirect('/login/')     
    
def Setsession(req):
    req.session['name']='megha'
    return render(req,'setsession.html')
 
def Getsession(req):
    print(req.session.get_session_cookie_age())
    print(req.session.get_expiry_age())
    print(req.session.get_expiry_date())
    print(req.session.get_expire_at_browser_close())
    if 'name' in req.session:
        name=req.session['name']
        return render(req,'getsession.html',{'name':name})
    else:
        return HttpResponse("YOUR SESSION HAS BEEN EXPIRED")

def Deletesession(req):
    req.session.flush()
    req.session.clear_expired()
    return render(req,'delsession.html')