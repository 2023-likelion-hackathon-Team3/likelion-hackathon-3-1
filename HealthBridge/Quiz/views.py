from django.shortcuts import render
from .models import Quiz
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models import Q
from konlpy.tag import Okt
from collections import Counter
import os

# Create your views here.

def quiz(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes}
    if 'search_nouns' in request.GET:
        search_nouns = request.GET.getlist('search_nouns')
        request.session['previous_nouns'] = search_nouns
    return render(request, 'quiz.html', context)

def answer(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    search_nouns = request.session.get('search_nouns', []) #이거 아직 안됨
    return render(request, 'answer.html', {'quiz':quiz, 'search_nouns':search_nouns})

def searchView(request):
    search = request.GET.get('search', '')
    
    search_nouns = extract_nouns_from_query(search)
    
    request.session['previous_nouns'] = search_nouns
    
    query = Q()
    for noun in search_nouns:
        query &= Q(question__icontains=noun)
    
    search_temps = Quiz.objects.filter(query)
    
    return render(request, 'quiz.html', {'temps': search_temps, 'search_nouns' : search_nouns})

def extract_nouns_from_query(search_query):
    okt = Okt()
    nouns = [word for word, pos in okt.pos(search_query) if pos == 'Noun']
    return nouns