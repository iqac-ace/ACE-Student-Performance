from django import forms
from django.contrib.auth.models import User
from .models import Department, Student, Subject, SemesterResult, ActivityEvidence, Profile

class DepartmentForm(forms.ModelForm):
    class Meta: model=Department; fields=['code','name','active']
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'register_number',
            'name',
            'department',
            'batch',
            'current_semester',
            'email',
            'phone',
            'class12_board',
            'class12_total',
            'class12_max',
            'active',
        ]

        widgets = {
            'register_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Register Number'
                }
            ),

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Student Name'
                }
            ),

            'department': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'batch': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Example: 2025-2029'
                }
            ),

            'current_semester': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                    'max': 8
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Student Email'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone Number'
                }
            ),

            'class12_board': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '12th Board'
                }
            ),

            'class12_total': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'class12_max': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),
        }
class SubjectForm(forms.ModelForm):
    class Meta: model=Subject; fields='__all__'
class SemesterResultForm(forms.ModelForm):
    class Meta: model=SemesterResult; exclude=['uploaded_by','status']
class ActivityEvidenceForm(forms.ModelForm):
    class Meta: model=ActivityEvidence; exclude=['created_by','status']
class ExcelUploadForm(forms.Form):
    file=forms.FileField(help_text='Upload .xlsx file using the provided template')
class StaffCreateForm(forms.Form):
    username=forms.CharField(); password=forms.CharField(widget=forms.PasswordInput)
    first_name=forms.CharField(required=False); last_name=forms.CharField(required=False)
    email=forms.EmailField(required=False)
    role=forms.ChoiceField(choices=[('HOD','Head of Department'),('FACULTY','Faculty')])
    department=forms.ModelChoiceField(queryset=Department.objects.filter(active=True))
