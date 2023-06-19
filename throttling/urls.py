from django.urls import path
from . import views


app_name = "throttling"


urlpatterns = [
    path('', views.throttling_example),
]