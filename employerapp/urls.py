from django.urls import path
from .views import *

urlpatterns = [
    path('employers', employers),
    path('showemployers', showemployers),
    path('', showemployers),
    path('deleteEmployers/<str:pk>', deleteEmployers),
    path('editEmployers/<str:pk>', editemployers), 
    path('updateEmployers/<str:pk>', updateEmployers), 
]
