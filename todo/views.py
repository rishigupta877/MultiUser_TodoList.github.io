from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from todo.forms import TODOForm
from todo.models import Todo

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        form=TODOForm()
        todos=Todo.objects.filter(user=user).order_by('priority')

        return render(request,'todo/home.html',{'form':form,'todos':todos})


def login(request):

    if request.method=='GET':
        form=AuthenticationForm()


        return render(request,'todo/login.html',{"form":form})
    
    else:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                loginUser(request,user)
                return redirect('home')
            

        else:
            return render(request,'todo/login.html',{"form":form})
            



def signup(request):
    if request.method=="POST":
        print(request.POST)
        form=UserCreationForm(request.POST)
        context={
           "form":form

        }
        if form.is_valid():
            user=form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
           return render(request,'todo/signup.html',context=context) 

    else:
      form=UserCreationForm()
      context={
           "form":form

       }
      return render(request,'todo/signup.html' ,context=context)



@login_required(login_url='login')
def add_todo(request):

    if request.user.is_authenticated:
        user=request.user
        form=TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo=form.save(commit=False)
            todo.user=user
            todo.save()
            return redirect('home')
        else:
            return render(request,'todo/home.html',{'form':form})

@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('login')


def delete_todo(request,id):
    print(id)
    Todo.objects.get(pk=id).delete()

    return redirect('home')
    

def change_todo(request,id,status):
    #print(id)
    todo=Todo.objects.get(pk=id)
    todo.status=status
    todo.save()

    return redirect('home')