from django.urls import path
from . import views 

urlpatterns = [
    path('list-student/',views.listStudent,name='liststudent'),
    path('add-student/',views.addStudent, name='addstudent'),
]
