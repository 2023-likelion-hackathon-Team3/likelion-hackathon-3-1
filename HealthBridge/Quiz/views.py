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
    return render(request, 'quiz.html', context)

def answer(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    return render(request, 'answer.html', {'quiz':quiz})

def searchView(request):
    search = request.GET.get('search', '')
    
    search_nouns = extract_nouns_from_query(search)
    
    query = Q()
    for noun in search_nouns:
        query &= Q(question__icontains=noun)
    
    search_temps = Quiz.objects.filter(query)
    
    return render(request, 'quiz.html', {'temps': search_temps, 'search_nouns' : search_nouns})

def extract_nouns_from_query(search_query):
    okt = Okt()
    nouns = [word for word, pos in okt.pos(search_query) if pos == 'Noun']
    return nouns