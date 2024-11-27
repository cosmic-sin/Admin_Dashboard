from django.urls import path
from . import views

urlpatterns = [
    # path('users/', views.UserListView.as_view(), name='user_list'),
    # path('users/add/', views.UserCreateView.as_view(), name='add_user'),
    # path('users/edit/<int:pk>/', views.UserUpdateView.as_view(), name='edit_user'),
    # path('users/delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete_user'),

    # path('roles/', views.RoleListView.as_view(), name='role_list'),
    # path('roles/add/', views.RoleCreateView.as_view(), name='add_role'),
    # path('roles/edit/<int:pk>/', views.RoleUpdateView.as_view(), name='edit_role'),
    # path('roles/delete/<int:pk>/', views.RoleDeleteView.as_view(), name='delete_role'),

    path('permissions/', views.permission_list, name='permission_list'),
    path('permissions/add/', views.add_permission, name='add_permission'),
]
