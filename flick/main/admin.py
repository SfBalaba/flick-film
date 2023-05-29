from django.contrib import admin

from django.contrib import admin
# from main.models import Reco

#
from .models import RecommendCos


class RecommendCosAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'recom_movie', 'imdb_id']

admin.site.register(RecommendCos, RecommendCosAdmin)

