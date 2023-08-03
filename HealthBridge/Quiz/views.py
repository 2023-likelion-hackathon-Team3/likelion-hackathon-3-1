from django.shortcuts import render
from .models import Quiz
from django.db.models import Q

# Create your views here.

def quiz(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes}
    return render(request, 'quiz.html', context)

def answer(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    return render(request, 'answer.html', {'quiz':quiz})

def searchView(request):
    search=request.GET.get('search','')
    search_temps=Quiz.objects.filter(
    Q(question__icontains = search)
    )
    return render(request,'quiz.html',{'temps':search_temps})