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

def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '      apiKey: "AIzaSyB0_O_U4BpawvEAtArvVY9z9q7W3tcEuAA",'\
         '       authDomain: "studify-5c4b8.firebaseapp.com",'\
         '       projectId: "studify-5c4b8",'\
         '       storageBucket: "studify-5c4b8.appspot.com",'\
         '       messagingSenderId: "543888714962",'\
         '       appId: "1:543888714962:web:e50b0e254920102146110b",'\
         '       measurementId: "G-VLVWZMEEWY"'\
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")