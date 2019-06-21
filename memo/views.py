from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MemoForm
from .models import Memo
from django.shortcuts import get_object_or_404
from django.forms import forms
#from DjangoUeditor.forms import UEditorField
# Create your views here.




def Memo_list(request):
    memo=Memo.objects.all()
    return render(request, 'memo_list.html', context={'memos':memo})


def Memo_detail(request,memo_id):
    detail_memos=get_object_or_404(Memo,pk=memo_id)

    return render(request,'memo_detail.html',context={'detail_memos':detail_memos})


def Memo_forms(request):
    memo = Memo.objects.all()
    if request.method == 'POST':
        form = MemoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/memo_list/')
    else:
        form = MemoForm()
    context = {
        'memos': memo,
        'form': form,
    }

    return render(request, 'memo_form.html', context=context)



def delmemos(request):
    id = request.GET.get("id")
    Memo.objects.filter(id=id).delete()

    return redirect('/memo_list/')