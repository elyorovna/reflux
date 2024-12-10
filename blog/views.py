from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import ContactForm


# Create your views here.
def index(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponse("qabul qilindi")
      else:
         return HttpResponse("qabul qilinmadi")
   else:
      form = 0

   context = {
      'form': form
   }
   return render(request, 'index.html', context=context)







