
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from .models import CustomUser
# from django.urls import reverse_lazy
# from django.template import loader
# from .models import Roles
# Create your views here.

# from django.contrib.auth import authenticate,login as auth_login
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get['username']
#         password = request.POST.get['password']

#         user = authenticate(request, username=username,password=password)
#         if user is not None:
#             if user.is_superuser:

#                 auth_login(request, user)
#                 return redirect('/ad_dash')
#             else:
#                 return render(request,'login.html',{'error':'Invalid user'})
#         else:
#             return render(request,'login.html',{'error':'Invalid credentials'})
#     return render(request,'login.html')

# def ad_dash(request):
#     if not request.user.is_superuser:
#         return redirect('login')
#     return render(request, 'base.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Permission
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Fixed from 'Username' to 'username'
        password = request.POST.get('password')
        stay_logged_in = request.POST.get('stay-logged-in')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                auth_login(request, user)
                if stay_logged_in:
                    request.session.set_expiry(0)
                return redirect('/admin/')
            else:
                return render(request, 'login.html', {'error': 'Invalid user (not a superuser)'})
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def ad_dash(request):
    if not request.user.is_superuser:
        return redirect('login')
    return render(request, 'base.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# def permission_list(request):
#     permissions = Permission.objects.all()
#     return render(request,'permissions/list.html',{'permissions': permissions})


# def add_permission(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         code = request.POST.get('code')
#         if name and code:
#             Permission.objects.create(name=name , code=code)
#             messages.success(request,"Permission add Sucessfully")
#             return redirect('permission_list')
#         else:
#             messages.error(request,"Both fields Requried")
#     return render(request,'permissions/add.html')



# class UserListView(ListView):
#     model = CustomUser
#     template_name = 'dashboard/user_list.html'
#     context_object_name = 'users'

# class UserCreateView(CreateView):
#     model = CustomUser
#     fields = ['username','email', 'role', 'is_active']
#     template_name = 'dashboard/user_form.html'
#     success_url = reverse_lazy('user_list')

# class UserUpdateView(UpdateView):
#     model = CustomUser
#     fields = ['username', 'email', 'role', 'is_active']
#     template_name = 'dashboard/user_form.html'
#     success_url = reverse_lazy('user_list')

# class UserDeleteView(DeleteView):
#     model = CustomUser
#     template_name = 'dashboard/user_confirm_delete.html'
#     success_url = reverse_lazy('user_list')

# #Role based Views

# class RoleListView(ListView):
#     model = Roles
#     template_name = 'dashboard/role_list.html'
#     context_object_name = 'roles'

# class RoleCreateView(CreateView):
#     model = Roles
#     fields = ['name', 'description', 'permissions']
#     template_name = 'dashboard/role_form.html'
#     success_url = reverse_lazy('role_list')

# class RoleUpdateView(UpdateView):
#     model = Roles
#     fields = ['name', 'description', 'permissions']
#     template_name = 'dashboard/role_form.html'
#     success_url = reverse_lazy('role_list')

# class RoleDeleteView(DeleteView):
#     model = Roles
#     template_name = 'dashboard/role_confirm_delete.html'
#     success_url = reverse_lazy('role_list')
