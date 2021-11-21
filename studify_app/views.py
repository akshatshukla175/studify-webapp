from django.contrib.auth import login,logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls.base import reverse


from studify_app.email_backend import EmailBackend

# Create your views here.
def showDemoPage(request):
    return render(request, "demo.html")

def showLoginPage(request):
    return render(request, "login_page.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user = EmailBackend.authenticate(request, username = request.POST.get("email"), password = request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
            
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")

def getUserDetails(request):
    if request.user != None:
        return HttpResponse("User : "+request.user.email+"usertype : "+request.user.user_type)
    else:
        return HttpResponse("Please login first")