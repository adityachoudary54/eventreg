from django.urls import path
from .views import (
    index,
    loginEventReg,
    display,
    details
)

urlpatterns=[
    path('',index,name='index'),
    path('login/',loginEventReg,name='login'),
    path('display/',display,name='display'),
    path('details/<int:id>/',details,name='details'),
]