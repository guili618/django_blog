from django.conf.urls import url
from . import  views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    #url(r'^$', views.home,name='blog-home'),
    url(r'^$', PostListView.as_view(),name='blog-home'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(),name='post-detail'),
    url(r'post/add/$', PostCreateView.as_view(), name='post-add'),
    url(r'post/(?P<pk>[0-9]+)/update$', PostUpdateView.as_view(),\
                                                            name='post-update'),
    url(r'post/(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(),\
                                                            name='post-delete'),
    url(r'^about/', views.about,name='blog-about'),
]
'''
urlpatterns = [
    url(r'^$', PostListView.as_view(),name='blog-home'),
    url(r'^user/(?P<username>\w+)/$', UserPostListView.as_view(),name='user-posts'),
    
    
    #url(r'^$', views.home,name='blog-home'),
    url(r'^about/', views.about,name='blog-about'),
]



'''


# <app>/<model>_<view_type>.html