from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from django.db import IntegrityError


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # اعتبارسنجی داده‌های ورودی
        if len(username) < 3:
            messages.error(request, 'نام کاربری باید حداقل ۳ حرف باشد')
            return redirect('accounts:signup')

        if len(password) < 6:
            messages.error(request, 'رمز عبور باید حداقل ۶ کاراکتر باشد')
            return redirect('accounts:signup')

        if password != confirm_password:
            messages.error(request, 'رمز عبور و تکرار آن مطابقت ندارند')
            return redirect('accounts:signup')

        try:
            # ایجاد کاربر جدید
            user = User.objects.create_user(
                username=username,
                password=password
            )

            # ورود خودکار کاربر
            login(request, user)

            messages.success(request, 'ثبت نام با موفقیت انجام شد!')
            return redirect('home:home')  # یا هر مسیر دیگری که می‌خواهید

        except IntegrityError:
            messages.error(request, 'این نام کاربری قبلاً ثبت شده است')
            return redirect('home:home')

    return render(request, 'account/signup.html')


def logout_view(request):
    logout(request)
    return redirect("home:home")
