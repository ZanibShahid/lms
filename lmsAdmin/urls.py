from django import views
from django.urls import path
from lmsAdmin.views import AdminDashboardView,LoginView, StudentAddView,StudentAddDetailView,LoginBackendView, \
 StudentListView, StudentEditView, StudentDeleteView, TeacherAddView,TeacherAddDetailView, \
  TeacherListView,TeacherEditView, TeacherProfile, assign_teacher, AddClassView, ClassDetailView, EditClassView,\
  assign_teacher_page,StudentProfile, attendance_list, edit_attendance, upload_attendance


urlpatterns = [

    # Login
    path('',LoginView,name="login"),
    path('loginbackend/',LoginBackendView,name="loginbacked"),


    path('dashboard/',AdminDashboardView,name="dashboard"),


    # Student
    path('addstudent/',StudentAddView,name="addstudent"),
    path('addstudentdetail/',StudentAddDetailView,name="addstudentdetail"),
    path('studentlist/',StudentListView,name="studentlist"),
    path('studentedit/<int:id>',StudentEditView,name="studentedit"),
    path('studentdelete/<int:id>',StudentDeleteView,name="studentdelete"),
    

    # Teacher
    path('addteacher/',TeacherAddView,name="addteacher"),
    path('addteacherdetail/',TeacherAddDetailView,name="addteacherdetail"),
    path('teacherlist/',TeacherListView,name="teacherlist"),
    path('teacheredit/<int:id>',TeacherEditView,name="teacheredit"),


    # class 
    path('addclass/',AddClassView,name="addclass"),
    path('editclass/<int:id>',EditClassView,name="editclass"),
    path('assign-teacher-page/<int:id>', assign_teacher_page, name="assignteacherpage"),
    path('assign-teacher/', assign_teacher, name="assignteacher"),
    path('classdetail/<int:id>', ClassDetailView, name="classdetail"),



    # Profile
    path('stdprofile/<int:id>',StudentProfile,name="stdprofile"),
    path('teacherprofile/<int:id>',TeacherProfile,name="teacherprofile"),
    
    
    path('attendance-upload/<int:id>', upload_attendance, name='attendance-upload'),
    path('attendance-edit/<attendance_id>/', edit_attendance, name='attendance-edit'),
    path('attendance-list/', attendance_list, name='attendance-list'),

]