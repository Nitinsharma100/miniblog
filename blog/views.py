from django.shortcuts import render,HttpResponseRedirect
from .forms import signupform,loginform,Postform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
# Create your views here.
from django.contrib.auth.models import Group
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')

def deshboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        fullname=user.get_full_name()
        gps=user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'fullname':fullname,"groups":gps})
    else:
        return HttpResponseRedirect('/login/')
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations!! You have become an Author")
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form=signupform()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=loginform(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'logged in Successfully!!')
                    return HttpResponseRedirect('/deshboard/')
        else:
            form=loginform()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/deshboard/')


def addpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=Postform(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
                form=Postform()
        else:
            form=Postform()
        
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login')
        
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=Postform(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=Postform(instance=pi)
        return render(request,'blog/update.html',{'form':form})
    else:
        return HttpResponseRedirect('/login')
        
        
def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/deshboard')
    else:
        return HttpResponseRedirect('/login')
        