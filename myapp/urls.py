from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', cgpa_calculator, name='cgpa_calculator'),
    path('edit/<int:subject_id>/', edit_subject, name='edit_subject'),
    path('delete/<int:subject_id>/', delete_subject, name='delete_subject'),
    path('result/', result, name='result'),

    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
]