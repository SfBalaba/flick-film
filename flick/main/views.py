from django.shortcuts import render, redirect
import requests
from main.service import get_trailers1

API_KEY = "YJKWE1C-8WSMSY3-PB0XDGX-2JN8N8N"

headers = {
    'Content-Type': "application/json",
    "X-API-KEY": API_KEY,
}


def index(request):
    context = {
    }
    return render(request, 'main/index.html')


def compilation(request):
    global API_KEY, headers
    URL = 'https://api.kinopoisk.dev/v1/movie/possible-values-by-field?field=genres.name'
    response = requests.get(URL, headers=headers)
    data = response.json()
    context = {
        'genres': data,
    }
    return render(request, 'main/compilation.html', context=context)


def genres(request, genre_name):
    URL = f'https://api.kinopoisk.dev/v1.3/movie?page=1&limit=10&genres.name={genre_name}'
    response = requests.get(URL, headers=headers)
    data = response.json()
    context = {
        # 'list': data.docs,
        'list': data,
        'genre': genre_name,
        'description': 'хз какое описание :/ мб базу надо будет создать отдельно. Пока так.',
    }
    return render(request, 'main/genres_base.html', context=context)


def bio(request, id):
    URL = f'https://api.kinopoisk.dev/v1.3/movie/{id}'
    response = requests.get(URL, headers=headers)
    data = response.json()
    context = {
        'obj': id,
        'response': data,
        'id': data['id'],
        'name': data['name'],
        'description': data['description'],
        'posterPreviewUrl': data['poster']['previewUrl'],
        'trailerUrl': get_trailers1(data),
        "genres": data['genres'],
        'persons': data["persons"],
        'sequelsAndPrequels': data['sequelsAndPrequels'],
    }
    return render(request, 'main/movie_base.html', context)
