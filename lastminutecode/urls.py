from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mathieu/', views.mathieu, name="mathieu"),
    path('mathieu/cv', views.cv_mathieu, name="cv_mathieu"),
]
