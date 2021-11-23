"""studify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from studify import settings
from studify_app import hod_views, Result,staff_views,student_views
from studify_app import views

urlpatterns = [
    path('demo', views.showDemoPage),
    path('signup_admin',views.signup_admin,name="signup_admin"),
    path('signup_student',views.signup_student,name="signup_student"),
    path('signup_staff',views.signup_staff,name="signup_staff"),
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('do_staff_signup',views.do_staff_signup,name="do_staff_signup"),
    path('do_signup_student',views.do_signup_student,name="do_signup_student"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.showLoginPage, name="show_login"),
    path('get_user_details', views.getUserDetails),
    path('do_login',views.doLogin,name="do_login"),
    path('logout_user', views.logoutUser, name="logout"),
    path('admin_home', hod_views.adminHome, name = "admin_home"),
    path('add_staff',hod_views.addStaff,name="add_staff"),
    path('add_staff_save',hod_views.addStaffSave,name="add_staff_save"),
    path('add_course', hod_views.addCourse,name="add_course"),
    path('add_course_save', hod_views.addCourseSave,name="add_course_save"),
    path('add_student', hod_views.add_student,name="add_student"),
    path('add_student_save', hod_views.add_student_save,name="add_student_save"),
    path('add_subject', hod_views.add_subject,name="add_subject"),
    path('add_subject_save', hod_views.add_subject_save,name="add_subject_save"),
    path('manage_staff', hod_views.manage_staff,name="manage_staff"),
    path('manage_student', hod_views.manage_student,name="manage_student"),
    path('manage_course', hod_views.manage_course,name="manage_course"),
    path('manage_subject', hod_views.manage_subject,name="manage_subject"),
    path('edit_staff/<str:staff_id>', hod_views.edit_staff,name="edit_staff"),
    path('edit_staff_save', hod_views.edit_staff_save,name="edit_staff_save"),
    path('edit_student/<str:student_id>', hod_views.edit_student,name="edit_student"),
    path('edit_student_save', hod_views.edit_student_save,name="edit_student_save"),
    path('edit_subject/<str:subject_id>', hod_views.edit_subject,name="edit_subject"),
    path('edit_subject_save', hod_views.edit_subject_save,name="edit_subject_save"),
    path('edit_course/<str:course_id>', hod_views.edit_course,name="edit_course"),
    path('edit_course_save', hod_views.edit_course_save,name="edit_course_save"),
    path('manage_session', hod_views.manage_session,name="manage_session"),
    path('add_session_save', hod_views.add_session_save,name="add_session_save"),
    path('student_feedback_message', hod_views.student_feedback_message,name="student_feedback_message"),
    path('student_feedback_message_replied', hod_views.student_feedback_message_replied,name="student_feedback_message_replied"),
    path('staff_feedback_message', hod_views.staff_feedback_message,name="staff_feedback_message"),
    path('staff_feedback_message_replied', hod_views.staff_feedback_message_replied,name="staff_feedback_message_replied"),
    path('student_leave_view', hod_views.student_leave_view,name="student_leave_view"),
    path('staff_leave_view', hod_views.staff_leave_view,name="staff_leave_view"),
    path('student_approve_leave/<str:leave_id>', hod_views.student_approve_leave,name="student_approve_leave"),
    path('student_disapprove_leave/<str:leave_id>', hod_views.student_disapprove_leave,name="student_disapprove_leave"),
    path('staff_disapprove_leave/<str:leave_id>', hod_views.staff_disapprove_leave,name="staff_disapprove_leave"),
    path('staff_approve_leave/<str:leave_id>', hod_views.staff_approve_leave,name="staff_approve_leave"),
    path('admin_view_attendance', hod_views.admin_view_attendance,name="admin_view_attendance"),
    path('admin_get_attendance_dates', hod_views.admin_get_attendance_dates,name="admin_get_attendance_dates"),
    path('admin_get_attendance_student', hod_views.admin_get_attendance_student,name="admin_get_attendance_student"),
    path('admin_profile', hod_views.admin_profile,name="admin_profile"),
    path('admin_profile_save', hod_views.admin_profile_save,name="admin_profile_save"),
    path('check_email_exist', hod_views.check_email_exist,name="check_email_exist"),
    path('check_username_exist', hod_views.check_username_exist,name="check_username_exist"),
    path('admin_send_notification_staff', hod_views.admin_send_notification_staff,name="admin_send_notification_staff"),
    path('admin_send_notification_student', hod_views.admin_send_notification_student,name="admin_send_notification_student"),
    path('send_student_notification', hod_views.send_student_notification,name="send_student_notification"),
    path('send_staff_notification', hod_views.send_staff_notification,name="send_staff_notification"),
    

    # Faculty URL Paths

    path('staff_home', staff_views.staffHome, name="staff_home"),
    path('staff_take_attendance', staff_views.staff_take_attendance, name="staff_take_attendance"),
    path('staff_update_attendance', staff_views.staff_update_attendance, name="staff_update_attendance"),
    path('get_students', staff_views.get_students, name="get_students"),
    path('get_attendance_dates', staff_views.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student', staff_views.get_attendance_student, name="get_attendance_student"),
    path('save_attendance_data', staff_views.save_attendance_data, name="save_attendance_data"),
    path('save_updateattendance_data', staff_views.save_updateattendance_data, name="save_updateattendance_data"), 
    path('staff_apply_leave', staff_views.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save', staff_views.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback', staff_views.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save', staff_views.staff_feedback_save, name="staff_feedback_save"),
    path('staff_profile', staff_views.staff_profile, name="staff_profile"),
    path('staff_profile_save', staff_views.staff_profile_save, name="staff_profile_save"),
    path('staff_fcmtoken_save', staff_views.staff_fcmtoken_save, name="staff_fcmtoken_save"),
    path('staff_all_notification', staff_views.staff_all_notification, name="staff_all_notification"),
    path('staff_add_result', staff_views.staff_add_result, name="staff_add_result"),
    path('save_student_result', staff_views.save_student_result, name="save_student_result"),
    path('edit_student_result',Result.Result.as_view(), name="edit_student_result"),
    path('fetch_result_student',staff_views.fetch_result_student, name="fetch_result_student"),
    
    # Student URL Paths

    path('student_home', student_views.studentHome, name="student_home"),
    path('save_attendance_data', staff_views.save_attendance_data, name="save_attendance_data"),
    path('student_view_attendance', student_views.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post', student_views.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave', student_views.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', student_views.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback', student_views.student_feedback, name="student_feedback"),
    path('student_feedback_save', student_views.student_feedback_save, name="student_feedback_save"),
    path('student_profile', student_views.student_profile, name="student_profile"),
    path('student_profile_save', student_views.student_profile_save, name="student_profile_save"),
    path('student_fcmtoken_save', student_views.student_fcmtoken_save, name="student_fcmtoken_save"),
    path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js"),
    path('student_all_notification',student_views.student_all_notification,name="student_all_notification"),
    path('student_view_result',student_views.student_view_result,name="student_view_result"),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
