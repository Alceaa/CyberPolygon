from django.shortcuts import render
from django.http import HttpResponse

def init(request):
    return render(
            request,
            'empty.html'
        )
