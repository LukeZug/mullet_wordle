from django.shortcuts import render, redirect


def index(request):
    return redirect('/wordle/')


def wordle(request):
    return render(request, 'wordle/index.html')
