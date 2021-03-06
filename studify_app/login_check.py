from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

# login check middleware to avoid problems such as hardcoding urls and sql injection 
class LoginCheck(MiddlewareMixin):
    def processView(self,request,view_func,view_args,view_kwargs):
        modulename = view_func.__module__
        print(modulename)
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "studify_app.hod_views":
                    pass
                elif modulename == "studify_app.views" or modulename == "django.views.static":
                    pass
                elif modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "studify_app.staff_views" or modulename == "studify_app.Result":
                    pass
                elif modulename == "studify_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                if modulename == "studify_app.student_views" or modulename == "django.views.static":
                    pass
                elif modulename == "studify_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))

        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login") or modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites" or modulename=="studify_app.views":
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))