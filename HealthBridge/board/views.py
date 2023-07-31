from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import *

# Create your views here.

def board(request):
    question_list = Board.objects.all()
    return render(request, 'board.html', {'question_list':question_list})

def write(request):
    if request.method == 'POST':
        now_user=request.user
        new_question = Board()
        new_question.title = request.POST.get('title')
        new_question.content = request.POST.get('content')
        new_question.hb_user = now_user
        new_question.save()
        
        return redirect('board:board-main')
    return render(request, 'write.html')

def detail(request, id):
    list = get_object_or_404(Board, pk=id)
    return render(request, 'detail.html', {'list':list})
