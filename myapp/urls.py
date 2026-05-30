from django.urls import path 
from myapp import views

urlpatterns = [
    path('showemployees/',views.showemployees,name='emps'),
    path('',views.add,name='employees'),
    path('findemployee/<int:id>/',views.findemployee,name='findemployee'),
    path('editemployee/<int:id>/',views.editemployee,name='editemployee'),
    path('deleteemployee/<int:id>/',views.deleteemployee,name='deleteemployee'),
]