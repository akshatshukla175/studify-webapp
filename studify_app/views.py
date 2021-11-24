from django.contrib.auth import login,logout
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls.base import reverse


from studify_app.email_backend import EmailBackend
from studify_app.models import Courses, CustomUser, SessionYearModel

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

def signupAdmin(request):
    return render(request,"signup_admin_page.html")

def signupStudent(request):
    courses=Courses.objects.all()
    session_years=SessionYearModel.object.all()
    return render(request,"signup_student_page.html",{"courses":courses,"session_years":session_years})

def signupStaff(request):
    return render(request,"signup_staff_page.html")

def doAdminSignup(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")

    try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=1)
        user.save()
        messages.success(request,"Successfully Created Admin")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"Failed to Create Admin")
        return HttpResponseRedirect(reverse("show_login"))

def doStaffSignup(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    address=request.POST.get("address")

    try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=2)
        user.staffs.address=address
        user.save()
        messages.success(request,"Successfully Created Faculty Account")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"Failed to Create Staff")
        return HttpResponseRedirect(reverse("show_login"))

def doSignupStudent(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    address = request.POST.get("address")
    session_year_id = request.POST.get("session_year")
    course_id = request.POST.get("course")
    sex = request.POST.get("sex")

    profile_pic = request.FILES['profile_pic']
    fs = FileSystemStorage()
    filename = fs.save(profile_pic.name, profile_pic)
    profile_pic_url = fs.url(filename)

    try:
        user = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                            first_name=first_name, user_type=3)
        user.students.address = address
        course_obj = Courses.objects.get(id=course_id)
        user.students.course_id = course_obj
        session_year = SessionYearModel.object.get(id=session_year_id)
        user.students.session_year_id = session_year
        user.students.gender = sex
        user.students.profile_pic = profile_pic_url
        user.save()
        messages.success(request, "Successfully Created Student Account")
        return HttpResponseRedirect(reverse("show_login"))
    except:
       messages.error(request, "Failed to Add Student")
       return HttpResponseRedirect(reverse("show_login"))