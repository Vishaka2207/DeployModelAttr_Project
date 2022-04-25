from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('Attrition/',views.Attrition,name="Attrition"),
    path('Churnform/',views.Churnform,name="Churnform"),
    path('home/',views.home,name="home"),
    path('result/',views.result,name="result")
]


urlpatterns += staticfiles_urlpatterns()
