from django.urls import path
from . import views 


urlpatterns = [
   path('mail_details/', views.api, name="Mail Details"),
]
