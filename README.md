# swcms
School Website Content Management System
Author -Vijay Kumar

Create a Folder swcms

create Virtual Enviornment

    python -m venv venv

Activate virtual Enviornment
    
    source venv/Scripts/activate

Install Django

    pip install django
    

Create Django Project in Present Working Directory

    django-admin startproject school .
    

Test Server

    python manage.py runserver 


Apply Admin Migrations

    python manage.py migrate

Create Admin Login

    python manage.py createsuperuser

Create a django app

    python manage.py startapp cms

Now open the setting.py file in your project folder and add cms app to installed app section

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
    ]


Create a new file in cms folder and save it with name urls.py 

    from django.urls import path

    urlpatterns = [
    path('',views.index,name='index'),
    ]

Now route this file in urls.py file in school folder

    from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include("cms.urls")),
    ]

 now Create a view for this. Goto view file in cms folder

    from django.shortcuts import render
    from . import views

    def index (request):
    return render(request,"index.html",{})

Create a templates folder in cms app and create html files index.html

index.html

    <!DOCTYPE html>
    
        <head>

        </head>
        
        <body>
   
        Hello! I am Home Page
        
        </body>
        
    </html>

Install Package pillow for image field

    python -m pip install pillow
    
Add following model code to model file in cms folder

from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import AbstractUser

    #class User(AbstractUser):
    #        ('student', 'Student'),
    #        ('teacher', 'Teacher'),
    #        ('parent', 'Parent/Guardian'),
    #        ('administrator', 'Administrator'),
    #        ('staff', 'Staff/Non-Teaching Personnel'),
    #        ('guest', 'Guest/User with Limited Access'),
    #    )
    #    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    class School(models.Model):
        name = models.CharField(max_length=255)
        address = models.TextField(blank=True)
        website = models.URLField(blank=True)
        email = models.EmailField(blank=True)
        phone_number = models.CharField(max_length=15, blank=True)
        logo = models.ImageField(upload_to='logos/', blank=True)  # Specify upload directory
        accreditation = models.CharField(max_length=255, blank=True)
        mission_statement = models.TextField(blank=True)
        vision_statement = models.TextField(blank=True)
        motto = models.CharField(max_length=255, blank=True)
        established_date = models.DateField(blank=True)
        principal_name = models.CharField(max_length=255, blank=True)
        description = models.TextField(blank=True)

        # Location using GeoDjango (optional)
        #location = models.PointField(blank=True, null=True)  # Requires GeoDjango installation

        def __str__(self):
        return self.name
        
    class Department(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        head_of_department = models.OneToOneField('Staff', on_delete=models.SET_NULL, null=True,         related_name='department_head')
    
        def __str__(self):
            return self.name
    
    class Event(models.Model):
        title = models.CharField(max_length=255)
        description = models.TextField()
        location = models.CharField(max_length=255)
        start_date = models.DateTimeField()
        end_date = models.DateTimeField()
    
        def __str__(self):
            return self.title
        
    class Facility(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to='facility_images/', blank=True)
    
        def __str__(self):
        return self.name   

    #class ExtracurricularActivity(models.Model):
        #name = models.CharField(max_length=100)
        #description = models.TextField()
        #category = models.CharField(max_length=100, choices=[
        #    ('Sports', 'Sports'),
        #    ('Clubs', 'Clubs'),
        #    ('Arts', 'Arts'),
        #    ('Academic', 'Academic'),
        #    ('Community Service', 'Community Service'),
        #    ('Other', 'Other')
        #])
        #start_date = models.DateField()
        #end_date = models.DateField()
        #location = models.CharField(max_length=255, blank=True)
        #image = models.ImageField(upload_to='activity_images/', blank=True)
        #coordinator = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='coordinated_activities')
        #participants = models.ManyToManyField('Student', related_name='participated_activities', blank=True)
        #schedule = models.TextField(blank=True)
        #requirements = models.TextField(blank=True)
        #achievements = models.TextField(blank=True)
        #resources = models.ManyToManyField('Resource', related_name='linked_activities', blank=True)
        #cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
        #registration_deadline = models.DateField(blank=True, null=True)
        #registration_link = models.URLField(blank=True)
        #active = models.BooleanField(default=True)
        #capacity = models.PositiveIntegerField(blank=True, null=True)
        #feedback_form = models.URLField(blank=True)
    
        #def __str__(self):
        #    return self.name
        
    class Class(models.Model):
        name = models.CharField(max_length=50, unique=True)  # Ensure class name is unique
        school = models.ForeignKey(School, on_delete=models.CASCADE)  # Link to School
    
        def __str__(self):
            return self.name
        class Meta:
            verbose_name_plural = 'Class'
    
    class Course(models.Model):
        department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
        name = models.CharField(max_length=100)
        description = models.TextField()
        credits = models.PositiveIntegerField()
        prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)
    
        def __str__(self):
            return self.name
               
    class Student(models.Model):
        #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
        name = models.CharField(max_length=100)
        roll_number = models.CharField(max_length=20)
        email = models.EmailField()
        date_of_birth = models.DateField()
        address = models.TextField()
        courses = models.ManyToManyField(Course, related_name='students', blank=True)
        #extracurricular_activities = models.ManyToManyField(ExtracurricularActivity, related_name='participants', blank=True)
    
        def __str__(self):
            return self.name
    
    class Staff(models.Model):
        #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
        school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='staff')
        name = models.CharField(max_length=100)
        role = models.CharField(max_length=100)
        email = models.EmailField()
        phone_number = models.CharField(max_length=20)
        bio = models.TextField(blank=True)
        profile_picture = models.ImageField(upload_to='staff_profile/', blank=True)
    
        def __str__(self):
            return self.name
    
    class Section(models.Model):
        name = models.CharField(max_length=50)
        class_level = models.ForeignKey(Class, on_delete=models.CASCADE)  # Link to Class
    
        def __str__(self):
            return f"{self.class_level.name} - {self.name}"

    class Subject(models.Model):
        name = models.CharField(max_length=100, unique=True)  # Ensure subject name is unique
    
        def __str__(self):
            return self.name
        
    class TimetableSlot(models.Model):
        day = models.CharField(max_length=10, choices=[
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
        ])
        start_time = models.TimeField()
        end_time = models.TimeField()
    
        def __str__(self):
            return f"{self.day} - {self.start_time} - {self.end_time}"

    class Teacher(models.Model):
      #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      email = models.EmailField(unique=True)
      phone_number = models.CharField(max_length=15, blank=True)
      subject = models.CharField(max_length=50, blank=True)
      bio = models.TextField(blank=True)
      image = models.ImageField(upload_to='static/teachers/', blank=True)
      date_of_birth = models.DateField(blank=True, null=True)
      joining_date = models.DateField(blank=True, null=True)
      retirement_date = models.DateField(blank=True, null=True)
      GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        )
      gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
      CATEGORY_CHOICES = (
            ('GEN', 'General'),
            ('SC', 'Scheduled Caste'),
            ('ST', 'Scheduled Tribe'),
            ('OBC', 'Other Backward Class'),
            ('EWS', 'Economically Weaker Section'),
            ('OTHER', 'Other'),
        )
      category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, blank=True)
      father_name = models.CharField(max_length=255, blank=True)
      mother_name = models.CharField(max_length=255, blank=True)
      spouse_name = models.CharField(max_length=255, blank=True) 
    
      def __str__(self):
        return f"{self.first_name} {self.last_name}"
      
      class Meta:
        ordering = ['first_name','last_name']
    
    class TimetableEntry(models.Model):
        section = models.ForeignKey(Section, on_delete=models.CASCADE)
        subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
        teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
        slot = models.ForeignKey(TimetableSlot, on_delete=models.CASCADE)
        school = models.ForeignKey(School, on_delete=models.CASCADE)  # Link to School
    
        # Optional field for handling absent teachers
        #substitute_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    
        class Meta:
            unique_together = ('section', 'slot')  # Ensure no duplicate entries for section and slot
    
        def __str__(self):
            return f"{self.section.name} - {self.subject.name} - {self.teacher.name} ({self.slot})"
                            
    
    class SmcCommitteeMember(models.Model):
        name = models.CharField(max_length=100)
        designation = models.CharField(max_length=50)  
        email = models.EmailField(blank=True)
        phone_number = models.CharField(max_length=15, blank=True)
        image = models.ImageField(upload_to='smc_members/', blank=True)  # Optional image field
    
        def __str__(self):
            return self.name
    
        class Meta:
            ordering = ['designation', 'name']
    
    class Affiliation(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField()
        website = models.URLField(blank=True)  # Website URL
        logo = models.ImageField(upload_to='affiliations/', blank=True)  
    
        def __str__(self):
            return self.name  
              
    class Coordinator(models.Model):
        staff = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='coordinator')
        role = models.CharField(max_length=100)
        email = models.EmailField()
        phone_number = models.CharField(max_length=20)
        department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name='coordinators')
        bio = models.TextField(blank=True)
        profile_picture = models.ImageField(upload_to='coordinator_profiles/', blank=True)
        office_location = models.CharField(max_length=255, blank=True)
        social_media_links = models.TextField(blank=True)
        responsibilities = models.TextField(blank=True)
        office_hours = models.CharField(max_length=100, blank=True)
        additional_contact_info = models.TextField(blank=True)
        achievements = models.TextField(blank=True)
        qualifications = models.TextField(blank=True)
        professional_experience = models.TextField(blank=True)
        education_background = models.TextField(blank=True)
        languages = models.CharField(max_length=255, blank=True)
        skills = models.TextField(blank=True)
    
        def __str__(self):
            return self.staff.name if self.staff else ""
    
    class Committee(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField(blank=True)
        chairperson = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='chaired_committees')
        members = models.ManyToManyField('Staff', related_name='committee_members', blank=True)
        meeting_schedule = models.CharField(max_length=100, blank=True)
        agenda = models.TextField(blank=True)
        tasks = models.TextField(blank=True)
        start_date = models.DateField(blank=True, null=True)
        end_date = models.DateField(blank=True, null=True)
        objectives = models.TextField(blank=True)
        documents = models.ManyToManyField('Document', related_name='related_committees', blank=True)
        contact_person = models.CharField(max_length=100, blank=True)
        contact_email = models.EmailField(blank=True)
        contact_phone = models.CharField(max_length=20, blank=True)
        
    
        def __str__(self):
            return self.name
    
    class Document(models.Model):
        name = models.CharField(max_length=255)
        file = models.FileField(upload_to='documents/')
        uploaded_at = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return self.name 
              
    class News(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField()
        date_published = models.DateTimeField(default=timezone.now)
        author = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)  # Foreign key to Teacher model (optional)
        category = models.CharField(max_length=50, blank=True)  # News category (e.g., "Academics", "Events")
        image = models.ImageField(upload_to='news/', blank=True) 
        def __str__(self):
            return self.title
    
        class Meta:
            verbose_name_plural = 'News'
            ordering = ['-date_published']  # Order by most recent first    


    class Topper(models.Model):
        STUDENT_TYPE_CHOICES = (
        ('Topper', 'Topper'),
        ('Shining Star', 'Shining Star')
    )

        student = models.ForeignKey('Student', on_delete=models.CASCADE)
        subject = models.CharField(max_length=100)
        obtained_marks = models.FloatField()
        total_marks = models.FloatField()
        exam_date = models.DateField()
        position = models.PositiveIntegerField()
        reason = models.TextField(null=True, blank=True)
        date_awarded = models.DateField(null=True, blank=True)
        award_type = models.CharField(max_length=20, choices=STUDENT_TYPE_CHOICES)    

Register all above model in admin.py in school folder

    from django.contrib import admin

    from . models import School
    from . models import Department
    from . models import Event
    from . models import Facility
    #from . models import ExtracurricularActivity
    from . models import Class
    from . models import Course
    from . models import Staff
    from . models import Student
    from . models import Section
    from . models import Subject
    from . models import Teacher
    from . models import TimetableSlot
    from . models import TimetableEntry
    from . models import SmcCommitteeMember
    from . models import Affiliation
    from . models import News
    from . models import Coordinator
    from . models import Committee
    from . models import Document
    class TeacherAdmin(admin.ModelAdmin):
        list_display =("first_name","last_name","father_name","mother_name","spouse_name","gender","category","date_of_birth","joining_date","retirement_date","subject","image","email","phone_number")
        
    
    admin.site.register(School)
    admin.site.register(Department)
    admin.site.register(Event)
    admin.site.register(Facility)
    #admin.site.register(ExtracurricularActivity)
    admin.site.register(Class)
    admin.site.register(Course)
    admin.site.register(Staff)
    admin.site.register(Student)
    admin.site.register(Section)
    admin.site.register(Subject)
    admin.site.register(Teacher,TeacherAdmin)
    admin.site.register(TimetableSlot)
    admin.site.register(TimetableEntry)
    admin.site.register(SmcCommitteeMember)
    admin.site.register(Affiliation)
    admin.site.register(News)
    admin.site.register(Coordinator)
    admin.site.register(Committee)
    admin.site.register(Document)

        
