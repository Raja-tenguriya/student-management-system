from django.urls import path
from .views import home, Add_student, delete_student, Edit_student

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('Add-student/', Add_student.as_view(), name ='add-student'),
    path('delete-student/', delete_student.as_view(), name="delete-student"),
    path('edit-student/<int:roll>/', Edit_student.as_view(), name="edit-student"),
]
