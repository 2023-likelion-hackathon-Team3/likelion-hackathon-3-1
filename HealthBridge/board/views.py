from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import *
from doctor.models import *

# Create your views here.


def board(request):
    question_list = Board.objects.all().order_by("-pk")
    return render(request, "board.html", {"question_list": question_list})


def write(request):
    if request.method == "POST":
        now_user = request.user
        new_question = Board()
        new_question.title = request.POST.get("title")
        new_question.content = request.POST.get("content")
        try:
            new_question.image = request.FILES["image"]
        except:
            new_question.image = None
        new_question.hb_user = now_user
        new_question.save()

        return redirect("board:board-main")
    return render(request, "board_write.html")


def detail(request, id):
    list = get_object_or_404(Board, pk=id)
    myuser = MyUser.objects.get(user=request.user)
    if request.method == "POST":
        answer = DoctorAnswer()
        answer.answer = request.POST.get("answer")
        answer.doctor = Doctor.objects.get(doctor_user=request.user)
        answer.board_list = list
        answer.save()
        list.answer = True
        list.save()
        return redirect("board:board-detail", list.id, {"answer": answer})

    if request.method == "GET":
        if list.answer == False:
            return render(
                request, "board_result.html", {"list": list, "myuser": myuser}
            )

        else:
            answer = DoctorAnswer.objects.get(board_list=list)
            doctor = User.objects.get(username=answer.doctor.doctor_user)
            return render(
                request,
                "board_result.html",
                {"list": list, "answer": answer, "myuser": myuser, "doctor": doctor},
            )
    return render(
        request, "board_result.html", {"list": list, "myuser": myuser, "answer": answer}
    )


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
    board.answer = False
    board.save()
    answer.delete()

    return redirect("board:board-detail", id=id)
