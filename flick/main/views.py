
from django.shortcuts import render, redirect

def index(request):
    # template = loader.get_template("index.html")
    context = {
    }
    return render(request, 'main/index.html')


def bio(request, id):
    # template = loader.get_template("index.html")
    context = {
        'obj' : id,
    }
    return render(request, 'main/movie_base.html', context)