import json

from django.shortcuts import render
from django.http import HttpResponse
import movie_rate_system.sparkClient.moviesHandler as moviesHandler


# Create your views here.
class resultTemplate:
    def __init__(self, result, messgae, data):
        self.result = result
        self.data = data
        self.message = messgae

    result = "false"
    message = "未知错误"
    data = []


def queryMovies(request):
    movies = moviesHandler.queryMovies()
    result = json.dumps({"result": "true", "message": "返回成功", "data": movies})
    return HttpResponse(result, content_type="application/json")


def getIndexHtml(request):
    return render(request, "index.html", content_type="text/html")

def getMoviesTag(request):
    result = json.dumps(
        {"result": "true", "message": "返回成功", "data": moviesHandler.getMovieTags(request.GET["movieId"])})
    return HttpResponse(result, content_type="application/json")

def getMovies(request):
    result = json.dumps(
        {"result": "true", "message": "返回成功", "data": moviesHandler.queryMoviesByTitle(request.GET["title"])})
    return HttpResponse(result, content_type="application/json")


def getMovieRate(request):
    result = json.dumps(
        {"result": "true", "message": "返回成功", "data": moviesHandler.averageRate(request.GET["movieId"])})
    return HttpResponse(result, content_type="application/json")