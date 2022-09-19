from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import store
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def index(request):
    stores = store.objects.all().values("st_name", "st_location", "st_Address","st_status" ,"seller", 
   "seller__sell_name", "seller__sell_gender" ,"image")
    
    return render(request, "index.html", {"store": stores})


def search(request):
    return render(request, "search.html")

def search_action(request):
    search_item = request.GET.get("search_item")
    stores = list(store.objects.all().values("st_name", "st_location", "st_Address","st_status" ,"seller", 
   "seller__sell_name", "seller__sell_gender"))
    #return render(request, "index.html", {"store": stores})
    return JsonResponse({"store_result": stores})

def signup(request):
    return render(request, "signup.html")

def signup_action(request):
    username = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    user = User.objects.create_user(username=username, password=password, first_name = name)
    auth.login(request, user=user)
    return redirect('index')

def signin_action(request):
    username = request.POST.get("email")
    password = request.POST.get("password")
    print(username,password)
    user = auth.authenticate(request,username=username, password=password)
    auth.login(request, user=user)
    return redirect('index')

def signin(request):
    return render(request, "signin.html")


'''
def Ram(request):
    #return HttpResponse("<h1>Hello Ram</>")   
    return HttpResponse("<h5>DataEngineering</>")

'''
