from django.shortcuts import render
from .models import Game

def new_game(request):
    return render(request, 'blackjack/index.html')

def play(request):
    return render(request, 'blackjack/play.html')

def leaderboard(request):
    return render(request, 'blackjack/leaderboard.html')



