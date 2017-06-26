from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator

from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm
from qa.models import Question

# Create your views here.

def test(request):
    return HttpResponse("test")

@require_GET
def index(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1

    questions = Question.objects.new()
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'index.html', {
        'paginator': paginator,
        'questions': page.object_list,
        'page': page,
        'user': request.user,
        'session': request.session, })

@require_GET
def popular(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    except TypeError:
        page = 1

    questions = Question.objects.popular()
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'popular.html', {
        'paginator': paginator,
        'questions': page.object_list,
        'page': page, })

def question(request, id):
    try:
        q = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            _ = form.save()
            # url = q.get_url()
            url = _.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
        # form = AnswerForm(initial={'question': q.id })

    return render(request, 'question.html', {
        'question': q,
        'form' : form,
        'user': request.user,
        'session': request.session, })

def ask_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        return render(request, 'ask_add_form.html', {
            'form' : form,
            'user': request.user,
            'session': request.session, })

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data["username"]
            password = form.raw_password
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form,
        'user': request.user,
        'session': request.session, })

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username, password)
            user = authenticate(username=username, password=password)
            print(type(user))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
        'user': request.user,
        'session': request.session, })
