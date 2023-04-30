from django.urls import path
from .views import loginPage, dashboard, logoutPage, register


app_name = 'account'
urlpatterns=[
    path('', loginPage, name = 'login'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logoutPage, name='logout'),
    path('register', register, name='register')
]