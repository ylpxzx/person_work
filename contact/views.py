from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm
from .models import Contact
from django.shortcuts import get_object_or_404
# Create your views here.
def Contact_list(request):

    contact=Contact.objects.all()
    return render(request, 'contact_list.html', context={'contacts':contact})



def delcontacts(request):

    id = request.GET.get("id")
    Contact.objects.filter(id=id).delete()
    return redirect('/contact_list/')

def Contact_forms(request):
    contact = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact_list/')
    else:
        form = ContactForm()
    context = {
        'contacts': contact,
        'form': form,
    }
    return render(request, 'contact_form.html', context=context)