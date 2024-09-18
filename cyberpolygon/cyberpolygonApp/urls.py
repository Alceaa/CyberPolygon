<<<<<<< HEAD
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.init, name='init'),
    path('home/', views.home, name='home'),
    path("accounts/", include("allauth.urls")),
=======
from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.init, name='init'),

    path('api/user', views.UserListCreate.as_view()),
    re_path(r'^api/user/(?P<pk>[0-9]+)/$', views.UserRetrieveUpdateDestroy.as_view() ),

    path('api/roles/', views.RoleListCreate.as_view()),
    re_path(r'^api/roles/(?P<pk>[0-9]+)/$', views.RoleRetrieveUpdateDestroy.as_view() ),

    path('api/categories/', views.CategoryListCreate.as_view()),
    re_path(r'^api/categories/(?P<pk>[0-9]+)/$', views.CategoryRetrieveUpdateDestroy.as_view() ),

    path('api/tasks/', views.TaskListCreate.as_view()),
    re_path(r'^api/tasks/(?P<pk>[0-9]+)/$', views.TaskRetrieveUpdateDestroy.as_view() ),

    path('api/comments/', views.CommentsListCreate.as_view()),
    re_path(r'^api/comments/(?P<pk>[0-9]+)/$', views.CommentsRetrieveUpdateDestroy.as_view() ),

    path('api/avatars/', views.UserAvatarListCreate.as_view()),
    re_path(r'^api/avatars/(?P<pk>[0-9]+)/$', views.UserAvatarRetrieveUpdateDestroy.as_view() ),
>>>>>>> origin/qqewi
]
