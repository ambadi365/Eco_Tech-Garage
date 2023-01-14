from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexpage,name='indexpage'),
    path('service/',views.Services,name='service'),
    path('service/<int:serv_id>',views.Single_Service,name='single-service'),
    path('team/',views.Team,name='team'),
    path('about/',views.About,name='about'),
    path('booking/',views.Contact,name='contact'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('respond/',views.Respond,name='respond'),
    path('status/',views.status,name='status'),
    path('contact/',views.contact_us,name='contact_us'),
    
    
    
    
]
