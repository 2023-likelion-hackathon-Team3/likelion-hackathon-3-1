from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

@login_required
def index(request):
    return redirect("HBapp:index")
