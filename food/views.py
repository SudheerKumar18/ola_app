from django.shortcuts import render

# Create your views here.
def nonveg(request):
    return render(request,'food.html')