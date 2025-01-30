
from django.contrib import admin
from django.urls import path
from FirstApp import views
from MultiViewsApp import views as v1
from App1 import views as v11
from App2 import views as v22
from django.urls import re_path
from App1.views import f11
from App2.views import f22


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome',views.display),
    path('welcome2',views.show),
    path('hello',views.hello),
    path('dtime/',views.senddatetime),

    path('mrng/',v1.f1),
    path('aftr/',v1.f2),
    path('evng/',v1.f3),

    path('hello2/',v11.f11),
    path('datetime2/',v22.f22),

    path('hello3/',f11),
    path('datetime3/',f22),
 
    path('firstdemo/',views.demo),
    path('seconddemo/',views.demo),
    path('thirddemo/',views.demo),

    re_path("^.*$",views.homepage),

]
