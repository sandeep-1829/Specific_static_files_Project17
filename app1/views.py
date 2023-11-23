from django.shortcuts import render

# Create your views here.

def specific_staticfiles(request):
    return render(request,'specific_staticfiles.html')