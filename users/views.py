from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.views  import View
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username},您的账户已创建，现在可以登录！')
            return redirect('auth-login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request,f'{username},您的个人信息已修改！')            
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)



class UserUpdateView(View):


    @method_decorator(login_required)
    def get(self,request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
        'u_form':u_form,
        'p_form':p_form
    }
        return render(request,'users/profile.html',context)

    
    @method_decorator(login_required)
    def post(self,request):
            u_form = UserUpdateForm(request.POST,instance=request.user)
            p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                username = u_form.cleaned_data.get('username')
                messages.success(request,f'{username},您的个人信息已修改！')            
                return redirect('users-profile')            
