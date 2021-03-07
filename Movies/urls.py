from django.urls import path
from . import views

app_name = "Movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movies_id>", views.details, name="detail")
]