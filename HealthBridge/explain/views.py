from django.shortcuts import render

# Create your views here.

def explain(request):
    return render(request, "explain.html")