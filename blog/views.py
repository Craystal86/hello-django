from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def hello_times(request, times):
    message = "안녕하세요" * times
    return HttpResponse(message)

