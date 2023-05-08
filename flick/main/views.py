
from django.shortcuts import render, redirect
import requests

from main.service import get_trailers,  get_trailers1


def index(request):
    # template = loader.get_template("index.html")
    context = {
    }


    return render(request, 'main/index.html')


def bio(request, id):



    API_KEY = "B17W2SC-N124J5X-MNF6E8N-0XZBT5T"

    URL = f'https://api.kinopoisk.dev/v1.3/movie/{id}'
    response = requests.get(URL,  headers={
        'Content-Type': "application/json",
      "X-API-KEY": "B17W2SC-N124J5X-MNF6E8N-0XZBT5T"
    })
    data = response.json()
    print(data)
    # print(data['videos']['trailers'][0]['url'])

    context = {
        'obj' : id,
        'response': data,
         'id': data['id'],
        'name': data['name'],
        'description': data['description'],
        'posterPreviewUrl': data['poster']['previewUrl'],
        'trailerUrl': get_trailers1(data),
        "genres": data['genres'],
        'persons': data["persons"],

    }
    print(context['persons'])
    return render(request, 'main/movie_base.html', context)