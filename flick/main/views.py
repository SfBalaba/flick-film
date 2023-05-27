import sys
from django.shortcuts import render, redirect
import requests
from main.service import get_trailers1

API_KEY = "YJKWE1C-8WSMSY3-PB0XDGX-2JN8N8N"
#API_KEY = '61556GR-YSY47YS-JBK7JE0-M9FJ4EA'

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
    poster = 'https://www.kinopoisk.ru/Da170N130/9bc82cW_E9C/W3BsR2ELvD0lNsDBzUdPKCOp3fGMM4AjB49RMHvJ81N-ftTh3nUtPZn4th1s_JbFV5cDaSBTvX93KxB-lngKg1xibNekijsr4XDCwd-Gza4xbE2xyjRCbwxE2zw20X5dtHcaZVgx7X-YeHaarK2WwoRWhGY8QfW-7emUPhK0QMhfYP5e5Ynxcucxi0IayUpp-uNJaEd1Cu7Bjx-x91Z2Xvi902HVeH801Ls412ck2QNaF4Wv-pLztyAv0LmSvc4Mm65z1i-JMTvo_4AI2gZH7n7hjCvNfQ2uQgeWNXlb-d73PNfgHb21dRnycZYpbljAExLLYHgQP_Zgatg8UvsPDJUl_d_nCTq2IXrORB1Gzqw75UAjzfULbIdOlvi6kTDatrdf4Bcxe_kZeTvf5CvfyJHbDaR7ETpyL2KQNN-5z0ec5_aeJ4E4O-m_TgVbhAIhOutFJE98j-BIQhkyuhdzlTy10WvcdXP3Gzsx2uMmUsRVHoyvuhS3Pujl3XjftMOCUur9GiFKu3Xj8IOHF03HbXThiKaGMo8rwsfZdXgYNtI79JVj1ne3_ZR5dl_t5JABkZBAYT-VtXsi5hp83jzCDdrofp-hCHExYP7OyN8BSqR-IQgkTLwDYAqCmHbz0TlZ-fnTZN7yPfAZv34Y5a6TTdoRi6txHHI07CxQ8NWzj8OcZTQcJoExdab3TosWRo-v9aaHp42yCOZIRBb5etMx3DBx1aoeP3O42vX3lWJqGMZdk8crv9M8OO5s1_Xd-MZHl-C7FSZH-TOsdUZDXEXIIfYkhCAPvEppSUrRN_Dc9598_9fo37e2e9Dwvt1mqZaJVxEFYDMYNb1qqpAwnDfMCxXts93uSjkzZHeEg9oED-TyLYUsT3qH6gqBFzLzV7cWd_8YZN9_u3CTeXvW5eyeDhYQDG940_g07GUadN-yxo9RJDYY58e69GY6xAdcyk-vMiZDqAy8BSHJCdd3tJOzF3C7FOEXsrX50_50GKfkVAEW0IIsfdi4si_vVDkXfIYH3O171CXJdfxvN48KmMVI5jOljegL-MhgAY-a-LPadFd3sB2kFXh6fpQ5_Foso1xG1JvJoXIbODVor5r8VrQLDRZr917ijvaw4beIAJWJRab0YAnmhbFPrIiK1X46lLla9TWXqZO_vPXWf7bfqiabg9ZYjSq6HbV0pCYVsxj5hsAf5z9c601xcSn4xsiWCEwsPSwKL0p6SqPIiBo_uVJ7EXD0UORcv_a91zW3nOIu0YUR34KpOxW-t68vljEevEOIGSu2nC3IPH3reYMCnQ7NoLSrjOEGc4khyARX8H3Q_xd--1RkV3o0-dg2NxflLVCIHx9MoX-T9vOsZFD03HrPg5NiOdEvhr5zIznIydMOjS865ksvQHfFqwFN1zWzV3Ted_gRadP_fH5cM7FeaWPWyZUYCyT9n38yaq3Q-RB8BkSV4rXZoQWz_Wl4ykCbCchmdSHFYwQ8CmsLyhI5vxZxUbY50ihdMjY3kLJzXaTkkEvV0c9j89k4tGatkvsXe0hD3OJy0CUAPrUl-sNNXQXMbnTsgWbA-0vujgefOPSY8F9_eNGk2Tm9vhx9uVYqLxOK3lgFZ7NcfLvt7Jr7XrROyFJt_xwqj7K1KPWLQFrAhS52LU3oR_pOIYCEGPl1GnYUN70bqNc5-r-feDic6W3Zxt8Xj2m-ErM1oGeafRG9wI1ea39Vbgd9-i54QwHejcupM6xF7Mo9j-OOTRq-td50WrS5WSgQdHB_Vv32WObh0EHRnAnqMlM7fadtlngf8MkKnK-zGeJHOD5n90wI1w9IbL2rDOwC90NiAsGd-fSY9tc-dFtqk7ByfBt5_5JtKVGEHdlEYrKbcrdnIZlwH3EPA5wmNRZsxnV773iLgJVIhCYy7YRqiHmCKE2J0jx01DpaP36b61F-9blYv3gXaWqSwdcbia3_ETW6rSkftlr1x0LcZHZe58gz9SgzQsxXjUfvcaWPJEd6BSLCid42PFG31T8x266Xdfcz0XD3U-2lEMkUkUjrMFizsq1s2HafdYHAGqV0kO0Oevwv8EJEE4dG7PIniiQAfAojhwzavncRM1-5_trhlbWzcRC7tF1n5RtG3JDDLHdVOzShrlAw1zPARJdsNR3kx334ZPlMg1ZHDuS24c3oAHjPIkvE2bhxkzTUMXbU7Fx8_3sY-DZS56TRwlKUDek51Tf7r2PceFF4D06T5DoRLEI7OSNwTkJTwQYu9WcDL8KwTmBCStM38pb-VHV93OlT_jN_HzJ7UyUjFEZeU4Kv-hpyOCHsmvnacssKHKD91yMH9T6l_s_MlI2L7vSrCikIc0PjBoqQsHyS99O0vxUh1LG6thB5PRYmolZI21CBoDkftT8tLpY4GnsJjRxnfl4hB3yy73HGBF3PCGh0JkXrRjGGZkII3jxx1nxaP7kSKZH_OHtXvzabL6pXzh3cAqhxGTvypq7Ys9x7zkQXZnzcJ8k5-2z4gkqcDsjuvalNrgN0huXLwZb_fdb3Ef59EKqeOn8xn7g3mCHvnIDfnINgMRK-sm_pHb5WfMvEWyq8X-_Ddbmk-AFJnYXM5rloAGoF94IpQUoXvjgZfJ99P1spHrj1Ptc4sZLlrxjB1dxJan4bM_Mv5Je_UTABzBOlNNniiHx0YT4CSdrAD6-yJ09jhThPYE6P0XD1VPgdvXtRJZAxPLycc3cU76LRw9efCmrzFHI65uoS_Bl1B4BcprqS5A-wvqUxCshchk3ku2mHpsQ7x-qKgR7_fVIzlPS8GOxYPLow3rM0GmuvH8xa2kDkslv-tK9sGLEd9MeF3q61miEI8rYhMIIKFAfLoHLlwmxFOQBmQkhT93FW-hw4th0jHvnwfx7w_R3vJtBEUtpIIzHYMvxqbhgw1ffLDRun9RfnCvT973LHw5aIzuezaQeoQvAJLUeAWrE6n3dbPjTVa1uxc_ER8jzd7iHbRJbTAC2zUP-yZs'
    if data["poster"] is not None and data["poster"]["previewUrl"] is not None:
        poster = data["poster"]["previewUrl"]
    persons = list(map(lambda x: fixNames(x), data["persons"]))
    context = {
        'obj': id,
        'response': data,
        'id': data['id'],
        'name': data['names'][0]['name'],
        'description': data['description'],
        'posterPreviewUrl': poster,
        'trailerUrl': get_trailers1(data),
        "genres": data['genres'],
        'persons': persons,
        'sequelsAndPrequels': data['sequelsAndPrequels'],
    }
    return render(request, 'main/movie_base.html', context)

def fixNames(person):
    if person["name"] is None:
        person["name"] = person["enName"]
    return person