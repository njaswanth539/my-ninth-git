from django.shortcuts import render

# Create your views here.
def jasu(request):
    d={'a':66123,'b':225,'c':2488}
    return render(request,'jasu.html',d)