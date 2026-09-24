from django.urls import path
from . import views
urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('students/',views.students,name='students'),
    path('students/add/',views.student_add,name='student_add'),
    path(
    'students/<int:pk>/edit/',
    views.student_edit,
    name='student_edit'
),
    path('students/<int:pk>/',views.student_detail,name='student_detail'),
    path('departments/',views.departments,name='departments'),
    path('departments/add/',views.department_add,name='department_add'),
    path('staff/add/',views.staff_add,name='staff_add'),
    path('subjects/',views.subjects,name='subjects'),
    path('subjects/add/',views.subject_add,name='subject_add'),
    path('marks/upload/',views.marks_upload,name='marks_upload'),
    path('marks/template/',views.marks_template,name='marks_template'),
    path('semester/add/',views.semester_add,name='semester_add'),
    path('activity/add/',views.activity_add,name='activity_add'),
    path('approvals/',views.approvals,name='approvals'),
    path('approve/<str:model>/<int:pk>/<str:decision>/',views.approve,name='approve'),
    path('reports/',views.reports,name='reports'),
]
