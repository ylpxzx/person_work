from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from .forms import ImageForm
from .models import Image
from django.shortcuts import get_object_or_404

# Create your views here.
def Image_list(request):
    images=Image.objects.all()
    return render(request, 'image_list.html', context={'images':images})


def Image_forms(request):
    image = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/image_list/')
    else:
        form = ImageForm()
    context = {
        'memos': image,
        'form': form,
    }
    return render(request, 'image_form.html', context=context)


def delimages(request):
    id = request.GET.get("id")
    Image.objects.filter(id=id).delete()

    return redirect('/image_list/')
