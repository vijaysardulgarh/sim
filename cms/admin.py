from django.contrib import admin
#from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import DateWidget, BooleanWidget
import datetime
#from import_export.widgets import DateWidget
#from .models import User
from .models import School
from .models import Affiliation
from .models import Facility
from .models import Nodal
from .models import Event
from .models import Document
from .models import News
from .models import ExtracurricularActivity
from .models import Committee
from .models import CommitteeMember
from .models import CommitteeMeeting    
from .models import Department
from .models import Stream
from .models import Class
from .models import Section
from .models import Subject
from .models import Staff
from .models import Classroom
from .models import ClassIncharge
from .models import Timetable
from .models import Day
from .models import TimetableSlot
from .models import TimetableEntry
from .models import Student
from .models import Topper
from .models import Book
import logging

 
admin.site.site_header="Admin Panel PM SHRI GSSS NAGPUR" 
admin.site.site_title="hi"
admin.site.index_title="welcome"
class StaffResource(resources.ModelResource):
    employee_id = fields.Field(attribute='employee_id',column_name='Employee ID')
    name = fields.Field(attribute='name',column_name='Employee Name [ID]')
    father_name = fields.Field(attribute='father_name',column_name="Father's Name")
    mother_name = fields.Field(attribute='mother_name',column_name="Mother's Name")
    spouse_name = fields.Field(attribute='spouse_name',column_name='Spouse Name')
    gender = fields.Field(attribute='gender',column_name='Gender')
    aadhar_number = fields.Field(attribute='aadhar_number',column_name='Aadhar No')
    designation = fields.Field(attribute='designation',column_name='Designation')
    category = fields.Field(attribute='category',column_name='Category')
    date_of_birth = fields.Field(attribute='date_of_birth',column_name='Date of Birth')
    joining_date = fields.Field(attribute='joining_date',column_name='Date of Joining School/Office')
    current__joining_date = fields.Field(attribute='current_joining_date',column_name='Date of Joining School/Office')
    retirement_date = fields.Field(attribute='retirement_date',column_name='Retirement Date')
    subject = fields.Field(attribute='subject',column_name='Subject')
    email = fields.Field(attribute='email',column_name='Email ID')
    mobile_number = fields.Field(attribute='phone_number',column_name='Mobile Number')
    teaching_subject_1 = fields.Field(attribute='teaching_subject_1',column_name='Teaching Subject 1')
    teaching_subject_2 = fields.Field(attribute='teaching_subject_1',column_name='Teaching Subject 2')
    staff_role = fields.Field(attribute='staff_role',column_name='Staff Role')
    employment_type = fields.Field(attribute='employment_type',column_name='Employment Type')
    designation = fields.Field(attribute='designation',column_name='Designation')

    class Meta:
        model = Staff
        fields=('id',"employee_id","name","father_name","mother_name","spouse_name","gender","aadhar_number","category","date_of_birth","joining_date","retirement_date","teaching_subject_1","teaching_subject_2","email","mobile_number","subject","staff_role","employment_type","designation")

    def before_import_row(self, row, **kwargs):
        try:
            if 'Date of Birth' in row and row['Date of Birth']:
                row['Date of Birth'] = self.reformat_date(row['Date of Birth'])
            if 'Date of Joining School/Office' in row and row['Date of Joining School/Office']:
                row['Date of Joining School/Office'] = self.reformat_date(row['Date of Joining School/Office'])
        except ValueError as e:
            logging.error(f"Error converting date: {e}. Row: {row}")

    def reformat_date(self, date_str):
        try:
            original_format = "%Y-%m-%d"  # Adjust format for date with time
            date_obj = datetime.datetime.strptime(date_str, original_format)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Error parsing date '{date_str}': {e}")
            return None  # Or provide a default value
        
class StaffAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display =("employee_id","name","father_name","mother_name","spouse_name","gender","aadhar_number","category","date_of_birth","joining_date","retirement_date","email","mobile_number","teaching_subject_1","staff_role","employment_type","designation")
    resource_class=StaffResource
class StudentResource(resources.ModelResource):
    
    srn = fields.Field(attribute='srn',column_name='SRN')
    studentclass = fields.Field(attribute='studentclass',column_name='Class')
    section = fields.Field(attribute='section',column_name='Section')
    roll_number = fields.Field(attribute='roll_number',column_name='Roll Number')
    full_name_aadhar = fields.Field(attribute='full_name_aadhar',column_name='FullName as on Aadhar Card')
    father_full_name_aadhar = fields.Field(attribute='father_full_name_aadhar',column_name="Father's Full Name aso on Aadhar Card")
    mother_full_name_aadhar = fields.Field(attribute='mother_full_name_aadhar',column_name="Mother's Full Name as on Aadhaar")
    
    date_of_birth = fields.Field(attribute='date_of_birth',column_name='Date of Birth')
    gender = fields.Field(attribute='gender',column_name='Gender')
    aadhaar_number = fields.Field(attribute='aadhaar_number',column_name='Aadhaar Number (If any)')
    category = fields.Field(attribute='category', column_name='Category Name')
    admission_number = fields.Field(attribute='admission_number',column_name='Admission Number')
    admission_date = fields.Field(attribute='admission_date',column_name='Admission Date')
    father_mobile = fields.Field(attribute='father_mobile',column_name="Father's Mobile No")
    mother_mobile = fields.Field(attribute='mother_mobile', column_name="Mother's Mobile No")
    bank_name = fields.Field(attribute='bank_name', column_name='Bank Name')
    ifsc = fields.Field(attribute='ifsc', column_name='IFSC')
    account_number = fields.Field(attribute='account_number', column_name='Account Number')
    disability = fields.Field(attribute='disability', column_name='Disability')
    disorder = fields.Field(attribute='disorder', column_name='Disorder Name')
    subjects_opted = fields.Field(attribute='subjects_opted', column_name='Subjects opted by student')
    stream = fields.Field(attribute='stream',column_name='Stream')
    school_code = fields.Field(attribute='school_code',column_name='SchoolCode')
    school_name = fields.Field(attribute='school_name',column_name='SchoolName')
  
    
    domicile_of_haryana = fields.Field(attribute='domicile_of_haryana',column_name='Domicile Of Haryana?')
    father_aadhaar_number = fields.Field(attribute='father_aadhaar_number',column_name="Father's Aadhaar Number")
    mother_aadhaar_number = fields.Field(attribute='mother_aadhaar_number',column_name="Mother's Aadhaar Number")
    guardian_full_name_aadhar = fields.Field(attribute='guardian_full_name_aadhar',column_name="Guardian's Full Name as on Aadhar Card")
    guardian_aadhaar_number = fields.Field(attribute='guardian_aadhaar_number',column_name="Guardian's Aadhar Nummber")
    family_annual_income = fields.Field(attribute='family_annual_income',column_name='Family Annual Income')
    state = fields.Field(attribute='state',column_name='State')
    district = fields.Field(attribute='district',column_name='District')
    block = fields.Field(attribute='block',column_name='CD Block')
    sub_district = fields.Field(attribute='sub_district',column_name='Sub-district/Tehsil')
    city_village_town = fields.Field(attribute='city_village_town',column_name='City/Village/Town')
    address = fields.Field(attribute='address',column_name='Adress Line 1')
    postal_code = fields.Field(attribute='postal_code',column_name='Postalcode')
    guardian_mobile = fields.Field(attribute='mother_mobile', column_name="Guardian's Mobile No")
    caste = fields.Field(attribute='caste_name', column_name='Caste Name')
    
    class Meta:
        model = Student
        #exclude = ('id',)
        fields = ('srn', 'school_code', 'school_name', 'admission_date', 'class', 'stream', 'section', 'roll_number', 'admission_number','admission_date','title', 'excel_full_name_aadhar', 'name_in_local_language', 'date_of_birth', 'gender', 'aadhaar_number', 'eid_number', 'domicile_of_haryana', 'nationality', 'excel_birth_country', 'birth_state', 'birth_district', 'birth_sub_district', 'birth_city_village_town',) 
        import_id_fields = ['srn']
        export_order = ('srn','studentclass','section','roll_number','full_name_aadhar','father_full_name_aadhar','mother_full_name_aadhar','date_of_birth','gender','aadhaar_number','category','admission_number','father_mobile')
        #widgets = {
        #    'admission_date': {'format': '%d/%m/%Y'},  # Format for date fields
        #    'date_of_birth': {'format': '%d/%m/%Y'},  # Format for date fields
        #    'bpl_certificate_issued_date': {'format': '%d/%m/%Y'},  # Format for date fields
        #    'sibling_date_of_birth': {'format': '%d/%m/%Y'},  # Format for date fields
        #    # Widgets for boolean fields
       
        #}       
    
    def before_import_row(self, row, **kwargs):
        try:
            if 'Date of Birth' in row and row['Date of Birth']:
                row['Date of Birth'] = self.reformat_date(row['Date of Birth'])
            if 'Admission Date' in row and row['Admission Date']:
                row['Admission Date'] = self.reformat_date(row['Admission Date'])
        except ValueError as e:
            logging.error(f"Error converting date: {e}. Row: {row}")

    def reformat_date(self, date_str):
        try:
            original_format = "%m/%d/%Y %H:%M:%S"  # Adjust format for date with time
            date_obj = datetime.datetime.strptime(date_str, original_format)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError as e:
            logging.error(f"Error parsing date '{date_str}': {e}")
            return None  # Or provide a default value
        
class StudentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    
    resource_class=StudentResource
    list_display=('srn','studentclass','section','roll_number','full_name_aadhar','father_full_name_aadhar','mother_full_name_aadhar','date_of_birth','gender','aadhaar_number','category','admission_number','father_mobile')

    
    
class TimetableSlotResource(resources.ModelResource):
    season = fields.Field(attribute='season',column_name='Season')
    day = fields.Field(attribute='day',column_name='Day')
    period = fields.Field(attribute='period',column_name='Period Count')
    start_time = fields.Field(attribute='start_time',column_name='Start Time')
    end_time = fields.Field(attribute='end_time',column_name='End Time')

    class Meta:
        model = TimetableSlot
        fields=('season','day','period','start_time','end_time')
        #use_id=False

class TimetableSlotAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('season','day','period','start_time','end_time')
    resource_class=TimetableSlotResource

class TimetableEntryResource(resources.ModelResource):
    section = fields.Field(attribute='section',column_name='Section')
    subject = fields.Field(attribute='subject',column_name='Subject')
    teacher = fields.Field(attribute='teacher',column_name='Teacher')
    slot = fields.Field(attribute='slot',column_name='Slot')

    class Meta:
        model = TimetableEntry
        fields=('section','subject','teacher','slot')
        #use_id=False

class TimetableEntryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('section','subject','teacher','slot')
    resource_class=TimetableEntryResource    


class TimetableResource(resources.ModelResource):
    class_name = fields.Field(attribute='class_name',column_name='Class')
    section = fields.Field(attribute='section',column_name='Section')
    subject = fields.Field(attribute='subject',column_name='Subject')
    day = fields.Field(attribute='day',column_name='Subject')
    period=fields.Field(attribute="period",column_name="Period")
    start_time = fields.Field(attribute='start_time',column_name='Subject')
    end_time = fields.Field(attribute='end_time',column_name='Subject')
    class_name = fields.Field(attribute='class_name',column_name='Class')
    section = fields.Field(attribute='section',column_name='Section')
    #classrooms = fields.Field(attribute='classrooms',column_name='Subject')
    teachers = fields.Field(attribute='teachers',column_name='Teachers' )
    #slot = fields.Field(attribute='slot',column_name='Slot')

    class Meta:
        model = Timetable
        fields=('day','period','start_time','end_time','class_name','section','subject','teachers')
        #use_id=False

class TimetableAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('day','period','start_time','end_time','class_name','section','subject','teacher_name')

    def teacher_name(self, obj):
        return obj.teachers.name
    
    resource_class=TimetableResource        
    
#admin.site.register(User)  
admin.site.register(School)
admin.site.register(Affiliation)
admin.site.register(Facility)
admin.site.register(Nodal)
admin.site.register(Event)
admin.site.register(Document)
admin.site.register(News)
admin.site.register(ExtracurricularActivity)
admin.site.register(Committee)
admin.site.register(CommitteeMember)
admin.site.register(CommitteeMeeting)
admin.site.register(Department)
admin.site.register(Stream)
admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Classroom)
admin.site.register(ClassIncharge)
admin.site.register(Timetable,TimetableAdmin)
admin.site.register(TimetableSlot,TimetableSlotAdmin)
admin.site.register(TimetableEntry,TimetableEntryAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Topper)
admin.site.register(Book)



