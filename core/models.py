from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

ROLE_CHOICES=[('IQAC','IQAC Coordinator'),('HOD','Head of Department'),('FACULTY','Faculty'),('STUDENT','Student')]
STATUS=[('PENDING','Pending'),('HOD_APPROVED','HOD Approved'),('IQAC_APPROVED','IQAC Approved'),('REJECTED','Rejected')]

class Department(models.Model):
    code=models.CharField(max_length=20, unique=True)
    name=models.CharField(max_length=120, unique=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.code} - {self.name}'

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=10,choices=ROLE_CHOICES,default='FACULTY')
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self): return f'{self.user.username} ({self.role})'

class Student(models.Model):
    register_number=models.CharField(max_length=30,unique=True)
    name=models.CharField(max_length=120)
    department=models.ForeignKey(Department,on_delete=models.PROTECT)
    batch=models.CharField(max_length=20,help_text='Example: 2025-2029')
    current_semester=models.PositiveSmallIntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(8)])
    email=models.EmailField(blank=True); phone=models.CharField(max_length=15,blank=True)
    class12_board=models.CharField(max_length=50,blank=True)
    class12_total=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    class12_max=models.DecimalField(max_digits=6,decimal_places=2,default=600)
    class12_percentage=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    active=models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if self.class12_total is not None and self.class12_max:
            self.class12_percentage = round(
                float(self.class12_total) /
                float(self.class12_max) * 100,
                2
            )

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.register_number} - {self.name}"

class Subject(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    semester=models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(8)])
    code=models.CharField(max_length=20); name=models.CharField(max_length=120)
    credits=models.DecimalField(max_digits=3,decimal_places=1,default=3)
    max_internal=models.DecimalField(max_digits=6,decimal_places=2,default=40)
    max_external=models.DecimalField(max_digits=6,decimal_places=2,default=60)
    class Meta: unique_together=('department','semester','code')
    def __str__(self): return f'{self.code} - {self.name}'

class SubjectMark(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='subject_marks')
    subject=models.ForeignKey(Subject,on_delete=models.PROTECT)
    internal=models.DecimalField(max_digits=6,decimal_places=2,default=0)
    external=models.DecimalField(max_digits=6,decimal_places=2,default=0)
    total=models.DecimalField(max_digits=6,decimal_places=2,default=0)
    status=models.CharField(max_length=15,choices=STATUS,default='PENDING')
    uploaded_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='uploaded_marks')
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: unique_together=('student','subject')
    def save(self,*args,**kwargs):
        self.total=float(self.internal)+float(self.external)
        super().save(*args,**kwargs)

class SemesterResult(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='semester_results')
    semester=models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(8)])
    sgpa=models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    cgpa=models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    credits_registered=models.DecimalField(max_digits=5,decimal_places=1,default=0)
    credits_earned=models.DecimalField(max_digits=5,decimal_places=1,default=0)
    arrears=models.PositiveSmallIntegerField(default=0)
    result=models.CharField(max_length=20,default='PASS')
    status=models.CharField(max_length=15,choices=STATUS,default='PENDING')
    uploaded_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    class Meta: unique_together=('student','semester')

class FrameworkParameter(models.Model):
    category_code=models.CharField(max_length=2)
    category_name=models.CharField(max_length=120)
    category_max=models.PositiveIntegerField()
    name=models.CharField(max_length=150)
    max_points=models.PositiveIntegerField()
    def __str__(self): return f'{self.category_code}. {self.name}'

class ActivityEvidence(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='activities')
    parameter=models.ForeignKey(FrameworkParameter,on_delete=models.PROTECT)
    title=models.CharField(max_length=180)
    activity_date=models.DateField()
    level=models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(4)])
    points=models.DecimalField(max_digits=6,decimal_places=2,default=0)
    evidence=models.FileField(upload_to='evidence/',blank=True,null=True)
    remarks=models.TextField(blank=True)
    status=models.CharField(max_length=15,choices=STATUS,default='PENDING')
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class AuditLog(models.Model):
    actor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    action=models.CharField(max_length=120)
    entity=models.CharField(max_length=80)
    entity_id=models.CharField(max_length=50,blank=True)
    details=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
