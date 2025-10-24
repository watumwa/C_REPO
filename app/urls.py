from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('attendance-report/', views.attendance_report, name='attendance_report'),
]
