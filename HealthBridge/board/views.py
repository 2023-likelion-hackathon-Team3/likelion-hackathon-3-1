from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def board(request):
    question_list = Board.objects.all()
    return render(request, 'board.html', {'question_list':question_list})

def create(request):
    if request.method == 'POST':
        new_question = Board()
        new_question.title = request.POST.get('title')
        new_question.content = request.POST.get('content')
        new_question.save()
        return redirect('board:board-main')
    return render(request, 'create.html')

def detail(request, id):
    list = get_object_or_404(Board, pk=id)
    return render(request, 'detail.html', {'list':list})

def update(request, id):
    update_list = get_object_or_404(Board, pk=id)
    
    if update_list.answer.strip() == '': #전문가답변이 없을 때
        if request.method == 'POST':
            update_list.title = request.POST.get('title')
            update_list.content = request.POST.get('content')
            update_list.save()
            return redirect('board:board-detail', update_list.pk)
        return render(request, 'update.html', {'update_list': update_list})
    else: #전문가 답변이 존재할 때
        return redirect('board:board-detail', update_list.pk)
