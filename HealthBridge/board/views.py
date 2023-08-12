from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import *
from doctor.models import *

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
        try:
            new_question.image = request.FILES["image"]
        except:
            new_question.image = None
        new_question.hb_user = now_user
        new_question.save()

        return redirect("board:board-main")
    return render(request, "write.html")


def detail(request, id):
    list = get_object_or_404(Board, pk=id)
    myuser = MyUser.objects.get(user=request.user)
    answer = DoctorAnswer.objects.filter(board_list=list)

    # if request.method == "GET":
    #     if list.has_answer == False:
    #         return render(request, "detail.html", {"list": list, "myuser": myuser})

    #     else:
    #         answer = DoctorAnswer.objects.filter(board_list=list)
    #         return render(
    #             request,
    #             "detail.html",
    #             {"list": list, "answer": answer, "myuser": myuser},
    #         )
    return render(
        request, "detail.html", {"list": list, "myuser": myuser, "answer":answer}
    )


# def updateAnswer(request, id, ansid):
#     board = Board.objects.get(pk=id)
#     doctor = Doctor.objects.get(doctor_user=request.user)
#     answer = DoctorAnswer.objects.get(pk=ansid)

#     print(answer)

#     if request.method == "POST":
#         answer.answer = request.POST.get("answer")
#         answer.save()
#         return redirect("board:board-detail", id=id)
#     return render(request, "update.html", {"answer": answer, "list": board})


# def deleteAnswer(request, id, ansid):
#     board = Board.objects.get(id=id)
#     answer = DoctorAnswer.objects.get(pk=ansid)
#     answer.delete()
#     board.answer = False
#     board.save()
#     return redirect("board:board-detail", id=id)
