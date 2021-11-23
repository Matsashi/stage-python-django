from django.shortcuts import redirect, render
from django.db.models import Prefetch
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.http import HttpResponse


def quiz_index(request):
    #quiz = Quiz.objects.prefetch_related(Prefetch('quiz', queryset=Quiz.objects.order_by("-created_on")))
    #quiz = Quiz.objects.order_by("-created_on").prefetch_related("title")
    quiz = Quiz.objects.all().order_by("-created_on")
    context = {"quiz": quiz}
    return render(request, "quiz_index.html", context)


def quiz_category(request, category):
    quiz = Quiz.objects.filter(categories__name__contains=category).order_by("-created_on")
    context = {"category": category, "quiz": quiz}
    return render(request, "quiz_category.html", context)


def quiz_detail(request):
    if request.method == 'POST':
        print(request.POST)
        questions = Question.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = correct / total * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'result.html', context)
    else:
        questions = Question.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'index.html', context)


def addQuestion(request):
    if request.user.is_staff:
        form = AddQuestionForm()
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('quiz')
        context = {'form': form}
        return render(request, 'addQuestion.html', context)
    else:
        return redirect('quiz')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('quiz')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('quiz')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')
