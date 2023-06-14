from django.contrib import admin
from main.models import Main
# Register your models here.
class MainAdmin(admin.ModelAdmin):
    # pass
    list_display = ['title']

admin.site.register(Main)
# class GenomeScoresAdmin(admin.ModelAdmin):
#     # pass
#     list_display = ['movieId', 'tagId', 'relevance']
#
# admin.site.register(GenomeScores)