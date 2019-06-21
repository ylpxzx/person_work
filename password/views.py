from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PasswordForm
from memo.models import Memo
from .models import Password
from image.models import Image
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    password = Password.objects.all()
    passwords=password[0:2]

    memo = Memo.objects.all()
    memos = memo[0:2]

    image=Image.objects.all()
    images = image[0:6]
    return render(request,'index.html',context={'passwords': passwords,'memos':memos,'images':images})


def Password_list(request):
    password=Password.objects.all()
    return render(request, 'password.html', context={'passwords':password})


def Password_detail(request,password_id):
    detail_passwords=get_object_or_404(Password,pk=password_id)
    return render(request,'password_detail.html',context={'detail_passwords':detail_passwords})


def Password_forms(request):
    password = Password.objects.all()
    if request.method == 'POST':
        form = PasswordForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/password/')
    else:
        form = PasswordForm()
    context = {
        'passwords': password,
        'form': form,
    }
    return render(request, 'password_form.html', context=context)


def delpasswords(request):
    id = request.GET.get("id")
    Password.objects.filter(id=id).delete()

    return redirect('/password/')