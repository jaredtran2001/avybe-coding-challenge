from django.shortcuts import render
from .models import Post


def createpost(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('inputFile'):
                post=Post()
                post.name= request.POST.get('name')
                post.inputFile = request.POST.get('inputFile')
                post.save()
                return render(request, 'Index.html')

        else:
                return render(request, 'Index.html')












#def home(request):
#  return render(request, 'Index.html')
