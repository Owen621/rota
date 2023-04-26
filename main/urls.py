from django.urls import path
from . import views
from .views import editView, updateInfo

urlpatterns = [
    path("", views.empty, name="empty"),
    path("welcome/", views.welcome, name="welcome"),
    path("info/", views.info, name="info"),
    path("home/", views.home, name="home"),
    path("generate/", views.generateRota, name="generateRota"),
    path("custom/", views.customRota, name="customRota"),
    path("edit/<int:pk>", editView.as_view(), name="editRota"),
    path("update/<int:pk>", updateInfo.as_view(), name="updateInfo"),
    path("delete/<int:pk>", views.deleteEmp, name="deleteEmp"),
    path("pdfrota/", views.pdf_rota, name="pdfrota"),
    path("rota/", views.rota, name="rota"),
    ]
