from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('dashboard/<str:username>/',views.dashboard,name='dashboard'),
    path('deposit/<str:username>/',views.deposit,name='deposit'),
    path('withdraw/<str:username>/',views.withdraw,name='withdraw'),
    path('change_upi_pin/<str:username>/',views.change_upi_pin,name='change_upi_pin'),

]