from datetime import date, datetime
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from lmsAdmin.models import Attendance, User, SchoolClass
from django.contrib.auth import authenticate, login, logout
from lmsAdmin.backends import EmailORIDAuthenticationBackend
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AssignTeacherForm, AssignStudentForm


# Create your views here.


# ******************** LOGIN *******************
def LoginView(request):
    return render(request, "lmsAuth/login.html")

def LoginBackendView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = EmailORIDAuthenticationBackend.authenticate(request,username=username,password=password)
    if user:
        if user.is_admin == 1:
            return redirect ("/dashboard/")
        if user.is_teacher == 1:
            return HttpResponse("teacher Dashboard")
        if user.is_teacher == 0:
            return HttpResponse("Student Dashboard")

    messages.error(request, "Invalid credentials Please try again!!")
    return redirect("/")

# ******************** Dashboard *******************

def AdminDashboardView(request):
    classes = SchoolClass.objects.all()
    context = {
        "classes": classes
    }
    return render(request,"admin/admindashboard.html", context)

# ******************** Student *******************
def StudentAddView(request):
    classes = SchoolClass.objects.all()
    context = {
        "classes": classes
    }
    return render(request,"lmsAuth/addstudent.html", context)

def StudentAddDetailView(request):
    # Auth Details
    studentId = request.POST['studentId']
    password = request.POST['password']

    # Further Details
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    gender = request.POST['gender']
    classNo = request.POST['classNo']
    religion = request.POST['religion']
    dob = request.POST['dob']
    phone = request.POST['phone']
    admissionNo = request.POST['admissionNo']
    section = request.POST['section']
    fatherName = request.POST['fatherName']
    fatherOccupation = request.POST['fatherOccupation']
    fatherMobile = request.POST['fatherMobile']
    motherName = request.POST['motherName']
    motherOccupation = request.POST['motherOccupation']
    motherMobile = request.POST['motherMobile']
    presentAddress = request.POST['presentAddress']
    permanentAddress = request.POST['permanentAddress']
    image = request.FILES['image']

    # user = User.objects.create_user(studentId=studentId,password=password)
    # user.is_teacher = False
    # user.save()

    student = User.objects.create_user(
        studentId=studentId,password=password,
        is_teacher = False,image=image,firstname=firstname,lastname=lastname,gender=gender,classNo=classNo,
        religion=religion,dob=dob,phone=phone,admissionNo=admissionNo,section=section,
        fatherName=fatherName,fatherOccupation=fatherOccupation,fatherMobile=fatherMobile,
        motherName=motherName,motherOccupation=motherOccupation,motherMobile=motherMobile,
        presentAddress=presentAddress,permanentAddress=permanentAddress
        )
    student.save()

    schoolclass = SchoolClass.objects.filter(pk=int(classNo)).first()
    schoolclass.students.add(student)


    print(request.FILES)  
    return redirect ("/studentlist/") 




def StudentListView(request):
    students = User.objects.filter(is_teacher=False)
    context = {
        "students" : students
    }
    return render(request, "admin/allstudents.html",context)

def StudentEditView(request,id):
    classes = SchoolClass.objects.all()
    student = User.objects.filter(pk=id).first()
    if request.method == "POST":
        studentId = request.POST['studentId']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        classNo = request.POST['classNo']
        religion = request.POST['religion']
        dob = request.POST['dob']
        phone = request.POST['phone']
        admissionNo = request.POST['admissionNo']
        section = request.POST['section']
        fatherName = request.POST['fatherName']
        fatherOccupation = request.POST['fatherOccupation']
        fatherMobile = request.POST['fatherMobile']
        motherName = request.POST['motherName']
        motherOccupation = request.POST['motherOccupation']
        motherMobile = request.POST['motherMobile']
        presentAddress = request.POST['presentAddress']
        permanentAddress = request.POST['permanentAddress']

        # Updating Data
        student.studentId = studentId
        student.set_password(password)
        student.firstname = firstname
        student.lastname = lastname
        student.gender = gender
        student.classNo = classNo
        student.religion = religion
        student.dob = dob
        student.phone = phone
        student.admissionNo = admissionNo
        student.section = section
        student.fatherName = fatherName
        student.fatherOccupation = fatherOccupation
        student.fatherMobile = fatherMobile
        student.motherName = motherName
        student.motherOccupation = motherOccupation
        student.motherMobile = motherMobile
        student.presentAddress = presentAddress
        student.permanentAddress = permanentAddress
        student.save()

        try:
            class_obj = SchoolClass.objects.get(students=student)
            class_obj.students.remove(student)
            class_obj.save()
        except: 
            print("update errors")
        schoolclass = SchoolClass.objects.filter(name=str(classNo)).first()
        if schoolclass:
            schoolclass.students.add(student)
        else:
    # Handle the case when no SchoolClass object with the specified name is found
           print("SchoolClass not found for the specified name:", classNo)
        messages.success(request,"Student Record Edited Successfully")
        return redirect('/studentlist/')
    else:        
        context = {
            "student": student,
            "classes": classes
        }
        return render(request, "admin/editstudent.html",context)
    
def StudentDeleteView(request,id):
    student = User.objects.filter(pk=id).first()
    student.delete()
    messages.error(request,"Student Record Deleted!!")
    return redirect('/studentlist/')




# # ******************** Teacher *******************

def TeacherAddView(request):
    return render(request,"lmsAuth/addteacher.html")
    
def TeacherAddDetailView(request):
    # Auth Details
    teacherId = request.POST['teacherId']
    email = request.POST['email']
    password = request.POST['password']

    # Further Details
    name = request.POST['name']
    gender = request.POST['gender']
    dob = request.POST['dob']
    phone = request.POST['phone']
    qualification = request.POST['qualification']
    experience = request.POST['experience']
    department = request.POST['department']
    education = request.POST['education']
    certificate = request.POST['certificate']
    skills = request.POST['skills']
    presentAddress = request.POST['presentAddress']
    permanentAddress = request.POST['permanentAddress']
    image = request.FILES['image']


    teacher = User(
        teacherId=teacherId,email=email,password=password,is_teacher = True,
        image=image,firstname=name,gender=gender,experience=experience,dob=dob,phone=phone,
        qualification=qualification,department=department,education=education,certificate=certificate,
        skills=skills,presentAddress=presentAddress,permanentAddress=permanentAddress
        )
    teacher.save()
 
    return redirect ("/teacherlist/") 


def TeacherListView(request):
    teachers = User.objects.filter(is_teacher=True,is_admin=False)
    classes = SchoolClass.objects.all()
    context = {
        "teachers" : teachers,
        "classes": classes
    }
    return render(request, "admin/allteacher.html",context)



def TeacherEditView(request,id):
    teacher = User.objects.filter(pk=id).first()
    if request.method == "POST":
        teacherId = request.POST['teacherId']
        password = request.POST['password']
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        phone = request.POST['phone']
        qualification = request.POST['qualification']
        experience = request.POST['experience']
        education = request.POST['education']
        certificate = request.POST['certificate']
        skills = request.POST['skills']
        email = request.POST['email']
        presentAddress = request.POST['presentAddress']
        permanentAddress = request.POST['permanentAddress']

        # Updating Data
        teacher.teacherId = teacherId
        teacher.email = email
        teacher.set_password(password)
        teacher.firstname = name
        teacher.gender = gender
        teacher.dob = dob
        teacher.phone = phone
        teacher.qualification = qualification
        teacher.experience = experience
        teacher.education = education
        teacher.certificate = certificate
        teacher.skills = skills
        teacher.presentAddress = presentAddress
        teacher.permanentAddress = permanentAddress
        teacher.save()

        messages.success(request,"teacher Record Edited Successfully")
        return redirect('/teacherlist/')
    else:        
        context = {
            "teacher": teacher
        }
        return render(request, "admin/editteacher.html",context)


def TeacherDeleteView(request,id):
    teacher = User.objects.filter(pk=id).first()
    teacher.delete()
    messages.error(request,"Teacher Record Deleted!!")
    return redirect('/teacherlist/')


# ************ Classes ************
def assign_teacher_page(request,id):
    teacher= User.objects.filter(pk=id).first()
    classes = SchoolClass.objects.all()
    context = {
        "teacher" : teacher,
        "classes" : classes
    }
    return render(request,'admin/assignteacher.html',context)

def assign_teacher(request):
    if request.method == 'POST':
        classid = request.POST["teacherclass"]
        teacherid = request.POST["teacher"]
        classs = SchoolClass.objects.get(pk=int(classid))
        teacher = User.objects.get(pk=int(teacherid))
        classs.teachers.add(teacher)

        messages.success(request, 'Teacher assigned to class.')
        return redirect("/teacherlist/")
    return redirect("/teacherlist/")


def AddClassView(request):
    if request.method == "POST":
        name = request.POST["classname"]
        schoolclass = SchoolClass(name=name)
        schoolclass.save()
        messages.success(request, 'Class Added Successfully')
        return redirect('/dashboard/')
    return redirect('/dashboard/')


def ClassDetailView(request, id):
    classes = SchoolClass.objects.filter(pk=id).first()
    students = classes.students.all()
    teachers = classes.teachers.all()

    context = {
        "clas": classes,
        "students": students,
        "teachers": teachers
    }
    return render(request, 'admin/class.html', context)


def EditClassView(request,id):
    if request.method == "POST":
        name = request.POST["classname"]
        schoolclass = SchoolClass.objects.filter(pk=id).first()
        schoolclass.name = name
        schoolclass.save()
        messages.success(request, f'{schoolclass.name} Updated Succesfully Successfully')
        return redirect('/admin/')
    return redirect('/admin/')


# ************ Profiles ************
def StudentProfile(request,id):
    student = User.objects.filter(pk=id,is_teacher=False)
    context = {'student' : student}
    return render(request,'lmsAuth/stdprofile.html',context)

def TeacherProfile(request,id):
    teacher = User.objects.filter(pk=id)
    context = {'teacher' : teacher}
    return render(request,'lmsAuth/teacherprofile.html',context)

def upload_attendance(request, id):
    classes = SchoolClass.objects.filter(pk=id).first()
    students = classes.students.all().values('studentId','firstname','image')
    attendance_date = date.today()
    attendance_time = datetime.now().strftime('%I:%M %p')

    if request.method == 'POST':
        attendance_date = request.POST.get('attendance_date')
        attendance_time = request.POST.get('attendance_time')
        classes = request.POST.get('clas')
        for student in students:
            stdid = student['studentId']
            stdname = student['firstname']
            for key, value in request.POST.items():
                if key.startswith('status_'):
                    if key.endswith(str(stdid)):
                        status = value
                        
                        attendance_data = Attendance(
                            attendance_date=attendance_date,
                            attendance_time=attendance_time,
                            classes=classes,
                            student_id=stdid,
                            student_name=stdname,
                            status=status
                            )
                        attendance_data.save()
        return redirect('attendance-list')

    context = {
        'clas': classes,
        'students':students,
        'attendance_date': attendance_date,
        'attendance_time': attendance_time,
    }
    return render(request, 'lmsAuth/upload-attendance.html', context)



def edit_attendance(request,attendance_id):
    if request.method == 'POST':
        attendance_id = request.POST.get('attendance_id')
        new_status = request.POST.get('status')
        attendance = get_object_or_404(Attendance, id=attendance_id)
        attendance.status = new_status
        attendance.save()
        messages.success(request, 'Attendance updated successfully.')
        return redirect('attendance-list')
    else:
        attendance = Attendance.objects.get(id=attendance_id)
        context = {'attendance': attendance}
        return render(request, 'lmsAuth/edit-attendance.html', context)




def attendance_list(request):
    attendance_list = Attendance.objects.all()
    unique_dates = set(attendance.attendance_date for attendance in attendance_list)
    context = {
        'attendance_list': attendance_list,
        'unique_dates': unique_dates
    }
    return render(request, 'lmsAuth/attendance_list.html', context)
