from django.urls import path
from . import views

urlpatterns=[
    path('',views.Setsession),
    path('get/',views.Getsession,name='sdetail'),
    path("signup/",views.signup,name='signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('dashboard/',views.Dashboard,name='dashboard'),
    path('changepassword/',views.Changepassword,name="changepassword"),
    path('resetpassword/',views.Resetpassword,name="resetpassword"),
    path('delete/',views.Deletesession),
    
]