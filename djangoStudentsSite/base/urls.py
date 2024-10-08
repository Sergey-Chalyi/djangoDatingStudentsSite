"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('startPage.urls')),
    path('look_for_job/', include('lookForJob.urls')),
    path('look_for_student/', include('lookForStudent.urls')),
    path('support/', include('support.urls')),
    path('__debug__/', include("debug_toolbar.urls")),
    # namespace - пространство имен для маршрутов в student.urls
    # для того, чтобы обращаться к маршрутам users:name
    path('users/', include('student.urls', namespace="users")),
]

# название страницы админ панели
admin.site.site_header = "ADMIN PANEL"
# заглавие главной страницы админ панели
admin.site.index_title = 'Main Admin Page'