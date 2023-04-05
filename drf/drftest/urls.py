from django.urls import path
from . import views
urlpatterns=[
    path('test/',views.defListView.as_view(),name='drf-list'),
    path('test/<int:pk>/',views.drfDetail.as_view(),name='drf-detail'),
    path('users/',views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/',views.UserDetail.as_view()),
    path('',views.api_root)
]