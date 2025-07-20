from unittest import result
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from importlib import import_module

# Create your models here.
class Class(models.Model):
    level = models.CharField(max_length=250)
    section = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.level + ' - ' + self.section)

class Subject(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    classI = models.ForeignKey(Class, on_delete= models.CASCADE)
    student_id = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank= True, null=True)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=20, choices=(('Male','Male'),('Female','Female')), default = 1)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.student_id + " - " + self.first_name + " " + (str(self.middle_name + " " + self.last_name)  if self.middle_name != '' else self.last_name ))

    def get_name(self):
        return str(self.first_name + " " + (str(self.middle_name + " " + self.last_name)  if self.middle_name != '' else self.last_name ))

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.CharField(max_length=250,blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.semester}"

    def countSubjects(self):
        try:
            resultCount = Student_Subject_Result.objects.filter(result = self).count()
        except:
            resultCount = 0
        return resultCount

    def average(self):
        try:
            resultCount = Student_Subject_Result.objects.filter(result = self).count()
            results = Student_Subject_Result.objects.filter(result = self).aggregate(Sum('grade'))['grade__sum']
            if not results is None:
                average = results / resultCount
        except Exception as err:
            print(err)
            average = 0
        return average

class Student_Subject_Result(models.Model):
    result = models.ForeignKey(Result, on_delete= models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    grade = models.FloatField(default=0)

    def __str__(self):
        return f"{self.result} - {self.subject}"

 
class user(models.Model):
    ENROLLMENT_NO = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    SEAT_NO = models.IntegerField(max_length=10)
    BRANCH=models.CharField(max_length=50)
    EVS= models.CharField(max_length=300)
    OS= models.CharField(max_length=10)
    OS_P = models.CharField(max_length=10)
    AJP = models.CharField(max_length=10)
    AJP_P = models.CharField(max_length=10)
    ST = models.CharField(max_length=10)
    ST_P = models.CharField(max_length=10) 
    CSSL = models.CharField(max_length=10) 
    CSSL_P = models.CharField(max_length=10) 
    IT = models.CharField(max_length=10) 
    CPP = models.CharField(max_length=10) 
    PERCENTAGE = models.FloatField(max_length=50)
    TOTAL = models.IntegerField(max_length=4)
    DIST = models.CharField(max_length=50)
    class Meta:
        db_table="COSEM3"

class user1(models.Model):
    ENROLLMENT_NO = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    SEAT_NO = models.IntegerField(max_length=10)
    BRANCH=models.CharField(max_length=50)
    OOP= models.CharField(max_length=300)
    OOP_P= models.CharField(max_length=10)
    DSU = models.CharField(max_length=10)
    DSU_P = models.CharField(max_length=10)
    CG = models.CharField(max_length=10)
    CG_P = models.CharField(max_length=10)
    DMS = models.CharField(max_length=10) 
    DMS_P = models.CharField(max_length=10) 
    DT = models.CharField(max_length=10) 
    DT_P = models.CharField(max_length=10) 
    PERCENTAGE = models.FloatField(max_length=50)
    TOTAL = models.IntegerField(max_length=4)
    DIST = models.CharField(max_length=50)
    class Meta:
        db_table="COSEM2"      
class user12(models.Model):
    ENROLLMENT_NO = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    SEAT_NO = models.IntegerField(max_length=10)
    BRANCH=models.CharField(max_length=50)
    ENGLISH= models.CharField(max_length=300)
    ENG_P= models.CharField(max_length=10)
    BASIC_SCIENCE = models.CharField(max_length=10)
    BS_P = models.CharField(max_length=10)
    BASIC_MATHEMATICS = models.CharField(max_length=10)
    ICT = models.CharField(max_length=10)
    EG = models.CharField(max_length=10) 
    WP = models.CharField(max_length=10) 
    PERCENTAGE = models.FloatField(max_length=50)
    TOTAL = models.IntegerField(max_length=4)
    DIST = models.CharField(max_length=50)
    class Meta:
        db_table="COSEM1"             
class MESEM3(models.Model):
    ENROLLMENT_NO = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    SEAT_NO = models.IntegerField(max_length=10)
    BRANCH=models.CharField(max_length=50)
    MANAGEMENT= models.CharField(max_length=300)
    PER= models.CharField(max_length=10)
    PER_P = models.CharField(max_length=10)
    AMP = models.CharField(max_length=10)
    AMP_P = models.CharField(max_length=10)
    EMD = models.CharField(max_length=10)
    EMD_P = models.CharField(max_length=10) 
    PPE = models.CharField(max_length=10) 
    PPE_P = models.CharField(max_length=10) 
    SMAM = models.CharField(max_length=10) 
    IT = models.CharField(max_length=10) 
    CPP = models.CharField(max_length=10) 
    PERCENTAGE = models.FloatField(max_length=50)
    TOTAL = models.IntegerField(max_length=4)
    DIST = models.CharField(max_length=50)
    class Meta:
        db_table="MESEM3"   

class ELSEM3(models.Model):
    ENROLLMENT_NO = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    SEAT_NO = models.IntegerField(max_length=10)
    BRANCH=models.CharField(max_length=50)
    MANAGEMENT= models.CharField(max_length=300)
    IAM= models.CharField(max_length=10)
    IAM_P = models.CharField(max_length=10)
    SP = models.CharField(max_length=10)
    SP_P = models.CharField(max_length=10)
    ECA = models.CharField(max_length=10)
    ECA_P = models.CharField(max_length=10) 
    EIA = models.CharField(max_length=10) 
    EIA_P = models.CharField(max_length=10) 
    ED = models.CharField(max_length=10) 
    IT = models.CharField(max_length=10) 
    CPP = models.CharField(max_length=10) 
    PERCENTAGE = models.FloatField(max_length=50)
    TOTAL = models.IntegerField(max_length=4)
    DIST = models.CharField(max_length=50)
    class Meta:
        db_table="ELSEM3"             


class ELSEM2(models.Model):
    ENROLLMENT_NO = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    SEAT_NO = models.IntegerField(max_length=10)
    BRANCH=models.CharField(max_length=50)
    EC= models.CharField(max_length=300)
    EC_P= models.CharField(max_length=10)
    EEM = models.CharField(max_length=10)
    EEM_P = models.CharField(max_length=10)
    FPE = models.CharField(max_length=10)
    FPE_P = models.CharField(max_length=10)
    EPG = models.CharField(max_length=10) 
    EPG_P = models.CharField(max_length=10) 
    EMWP = models.CharField(max_length=10) 
    EMWP_P = models.CharField(max_length=10) 
    PERCENTAGE = models.FloatField(max_length=50)
    TOTAL = models.IntegerField(max_length=4)
    DIST = models.CharField(max_length=50)
    class Meta:
        db_table="ELSEM2" 

class myuploadfile(models.Model):
    f_name = models.CharField(max_length=255)
    myfiles = models.FileField(upload_to="ele")

    def __str__(self):
        return self.f_name
        
class myuploadfile1(models.Model):
    f_name = models.CharField(max_length=255)
    myfiles = models.FileField(upload_to="com")

    def __str__(self):
        return self.f_name
class myuploadfile2(models.Model):
    f_name = models.CharField(max_length=255)
    myfiles = models.FileField(upload_to="civ")

    def __str__(self):
        return self.f_name
class myuploadfile3(models.Model):
    f_name = models.CharField(max_length=255)
    myfiles = models.FileField(upload_to="mec")

    def __str__(self):
        return self.f_name




