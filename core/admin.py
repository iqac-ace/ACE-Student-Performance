from django.contrib import admin
from .models import *
for m in [Department,Profile,Student,Subject,SubjectMark,SemesterResult,FrameworkParameter,ActivityEvidence,AuditLog]:
    admin.site.register(m)
