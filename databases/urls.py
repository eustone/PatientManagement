from django.urls import path
from . import views
app_name = 'databases'
urlpatterns = [
    path('', views.ListCreatePatientRecord.as_view(), name='database_list'),
]
