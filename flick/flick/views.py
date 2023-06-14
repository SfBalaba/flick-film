
from django.shortcuts import render, redirect

def index(request):
    # template = loader.get_template("index.html")
    context = {
    }
    return render(request, 'main/../main/templates/index.html')
