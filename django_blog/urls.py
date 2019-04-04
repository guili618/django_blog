"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

from django_filters.views import FilterView

from users.filters import UserFilter


urlpatterns = [
    url(r'^$', FilterView.as_view(filterset_class=UserFilter, 
                                           template_name='users/users_list.html'), name='search'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^register/',user_views.register,name='users-register'),
    url(r'^profile/',user_views.profile,name='users-profile'),
    url(r'^login/',auth_views.LoginView.as_view(template_name='users/login.html'),
                                                         name='auth-login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),
                                                           name='auth-logout'),
    url(r'^updateprofile/',user_views.UserUpdateView.as_view(),name='users-UserUpdateView'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)