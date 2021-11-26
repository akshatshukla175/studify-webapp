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
    
    # demo page path
    path('demo', views.showDemoPage),

    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    
    # Sign up paths
    path('signup_admin',views.signupAdmin,name="signup_admin"),
    path('signup_student',views.signupStudent,name="signup_student"),
    path('signup_staff',views.signupStaff,name="signup_staff"),
    path('do_admin_signup',views.doAdminSignup,name="do_admin_signup"),
    path('do_staff_signup',views.doStaffSignup,name="do_staff_signup"),
    path('do_signup_student',views.doSignupStudent,name="do_signup_student"),

    # User paths
    path('get_user_details', views.getUserDetails),
    path('do_login',views.doLogin,name="do_login"),
    path('logout_user', views.logoutUser, name="logout"),
    path('',views.showLoginPage, name="show_login"),

    # Admin/HOD URL Paths
    path('admin_home', hod_views.adminHome, name = "admin_home"),
    path('add_staff',hod_views.addStaff,name="add_staff"),
    path('add_staff_save',hod_views.addStaffSave,name="add_staff_save"),
    path('add_course', hod_views.addCourse,name="add_course"),
    path('add_course_save', hod_views.addCourseSave,name="add_course_save"),
    path('add_student', hod_views.addStudent,name="add_student"),
    path('add_student_save', hod_views.addStudentSave,name="add_student_save"),
    path('add_subject', hod_views.addSubject,name="add_subject"),
    path('add_subject_save', hod_views.addSubjectSave,name="add_subject_save"),
    path('manage_staff', hod_views.manageStaff,name="manage_staff"),
    path('manage_student', hod_views.manageStudent,name="manage_student"),
    path('manage_course', hod_views.manageCourse,name="manage_course"),
    path('manage_subject', hod_views.manageSubject,name="manage_subject"),
    path('edit_staff/<str:staff_id>', hod_views.editStaff,name="edit_staff"),
    path('edit_staff_save', hod_views.editStaffSave,name="edit_staff_save"),
    path('edit_student/<str:student_id>', hod_views.editStudent,name="edit_student"),
    path('edit_student_save', hod_views.editStudentSave,name="edit_student_save"),
    path('edit_subject/<str:subject_id>', hod_views.editSubject,name="edit_subject"),
    path('edit_subject_save', hod_views.editSubjectSave,name="edit_subject_save"),
    path('edit_course/<str:course_id>', hod_views.editCourse,name="edit_course"),
    path('edit_course_save', hod_views.editCourseSave,name="edit_course_save"),
    path('manage_session', hod_views.manageSession,name="manage_session"),
    path('add_session_save', hod_views.addSessionSave,name="add_session_save"),
    path('student_feedback_message', hod_views.studentFeedbackMessage,name="student_feedback_message"),
    path('student_feedback_message_replied', hod_views.studentFeedbackMessageReplied,name="student_feedback_message_replied"),
    path('staff_feedback_message', hod_views.staffFeedbackMessage,name="staff_feedback_message"),
    path('staff_feedback_message_replied', hod_views.staffFeedbackMessageReplied,name="staff_feedback_message_replied"),
    path('student_leave_view', hod_views.studentLeaveView,name="student_leave_view"),
    path('staff_leave_view', hod_views.staffLeaveView,name="staff_leave_view"),
    path('student_approve_leave/<str:leave_id>', hod_views.studentApproveLeave,name="student_approve_leave"),
    path('student_disapprove_leave/<str:leave_id>', hod_views.studentDisapproveLeave,name="student_disapprove_leave"),
    path('staff_disapprove_leave/<str:leave_id>', hod_views.staffDisapproveLeave,name="staff_disapprove_leave"),
    path('staff_approve_leave/<str:leave_id>', hod_views.staffApproveLeave,name="staff_approve_leave"),
    path('admin_view_attendance', hod_views.adminViewAttendance,name="admin_view_attendance"),
    path('admin_get_attendance_dates', hod_views.adminGetAttendanceDates,name="admin_get_attendance_dates"),
    path('admin_get_attendance_student', hod_views.adminGetAttendanceStudent,name="admin_get_attendance_student"),
    path('admin_profile', hod_views.adminProfile,name="admin_profile"),
    path('admin_profile_save', hod_views.adminProfileSave,name="admin_profile_save"),
    path('check_email_exist', hod_views.checkEmailExist,name="check_email_exist"),
    path('check_username_exist', hod_views.checkUsernameExist,name="check_username_exist"),
    path('admin_send_notification_staff', hod_views.adminSendNotificationStaff,name="admin_send_notification_staff"),
    path('admin_send_notification_student', hod_views.adminSendNotificationStudent,name="admin_send_notification_student"),
    path('send_student_notification', hod_views.sendStudentNotification,name="send_student_notification"),
    path('send_staff_notification', hod_views.sendStaffNotification,name="send_staff_notification"),
    

    # Faculty URL Paths
    path('staff_home', staff_views.staffHome, name="staff_home"),
    path('staff_take_attendance', staff_views.staffTakeAttendance, name="staff_take_attendance"),
    path('staff_update_attendance', staff_views.staffUpdateAttendance, name="staff_update_attendance"),
    path('get_students', staff_views.getStudents, name="get_students"),
    path('get_attendance_dates', staff_views.getAttendanceDates, name="get_attendance_dates"),
    path('get_attendance_student', staff_views.getAttendanceStudent, name="get_attendance_student"),
    path('save_attendance_data', staff_views.saveAttendanceData, name="save_attendance_data"),
    path('save_updateattendance_data', staff_views.saveUpdateAttendanceData, name="save_updateattendance_data"), 
    path('staff_apply_leave', staff_views.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save', staff_views.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback', staff_views.staffFeedback, name="staff_feedback"),
    path('staff_feedback_save', staff_views.staffFeedbackSave, name="staff_feedback_save"),
    path('staff_profile', staff_views.staffProfile, name="staff_profile"),
    path('staff_profile_save', staff_views.staffProfileSave, name="staff_profile_save"),
    path('staff_fcmtoken_save', staff_views.staffFcmtokenSave, name="staff_fcmtoken_save"),
    path('staff_all_notification', staff_views.staffAllNotification, name="staff_all_notification"),
    path('staff_add_result', staff_views.staffAddResult, name="staff_add_result"),
    path('save_student_result', staff_views.saveStudentResult, name="save_student_result"),
    path('edit_student_result',Result.Result.as_view(), name="edit_student_result"),
    path('fetch_result_student',staff_views.fetchResultStudent, name="fetch_result_student"),
    
    # Student URL Paths
    path('student_home', student_views.studentHome, name="student_home"),
    path('save_attendance_data', staff_views.saveAttendanceData, name="save_attendance_data"),
    path('student_view_attendance', student_views.studentViewAttendance, name="student_view_attendance"),
    path('student_view_attendance_post', student_views.studentViewAttendancePost, name="student_view_attendance_post"),
    path('student_apply_leave', student_views.studentApplyLeave, name="student_apply_leave"),
    path('student_apply_leave_save', student_views.studentApplyLeaveSave, name="student_apply_leave_save"),
    path('student_feedback', student_views.studentFeedback, name="student_feedback"),
    path('student_feedback_save', student_views.studentFeedbackSave, name="student_feedback_save"),
    path('student_profile', student_views.studentProfile, name="student_profile"),
    path('student_profile_save', student_views.studentProfileSave, name="student_profile_save"),
    path('student_fcmtoken_save', student_views.studentFcmtokenSave, name="student_fcmtoken_save"),
    path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js"),
    path('student_all_notification',student_views.studentAllNotification,name="student_all_notification"),
    path('student_view_result',student_views.studentViewResult,name="student_view_result"),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
