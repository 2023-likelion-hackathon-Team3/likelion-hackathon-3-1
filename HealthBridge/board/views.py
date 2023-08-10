from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import *

# Create your views here.


def board(request):
    question_list = Board.objects.all()
    return render(request, "board.html", {"question_list": question_list})


def write(request):
    if request.method == "POST":
        now_user = request.user
        new_question = Board()
        new_question.title = request.POST.get("title")
        new_question.content = request.POST.get("content")
        new_question.hb_user = now_user
        new_question.save()

        return redirect("board:board-main")
    return render(request, "write.html")


def detail(request, id):
    list = get_object_or_404(Board, pk=id)
    if request.method == "POST":
        new_answer = DoctorAnswer()
        new_answer.doctor = Doctor.objects.get(doctor_user=request.user)
        new_answer.answer = request.POST.get("answer")
        new_answer.board = list
        new_answer.save()
        list.answer = True
        list.save()
        print(new_answer)

        return redirect("board:board-detail", id=list.id)

    if request.method == "GET":
        if list.answer == False:
            print(list.answer)
            return render(request, "detail.html", {"list": list})

        else:
            answer = DoctorAnswer.objects.get(board=list)
            return render(request, "detail.html", {"list": list, "answer": answer})

    return render(request, "detail.html", {"list": list, "answer": new_answer})


def updateAnswer(request, id, ansid):
    board = Board.objects.get(pk=id)
    doctor = Doctor.objects.get(doctor_user=request.user)
    answer = DoctorAnswer.objects.get(pk=ansid)

    print(answer)

    if request.method == "POST":
        answer.answer = request.POST.get("answer")
        answer.save()
        return redirect("board:board-detail", id=id)
    return render(request, "update.html", {"answer": answer, "list": board})


def deleteAnswer(request, id, ansid):
    board = Board.objects.get(id=id)
    answer = DoctorAnswer.objects.get(pk=ansid)
    answer.delete()
    board.answer = False
    board.save()
    return redirect("board:board-detail", id=id)
