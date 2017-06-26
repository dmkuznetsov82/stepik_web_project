from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator

from qa.forms import AskForm, AnswerForm
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
        'page': page, })

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
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
        # form = AnswerForm(initial={'question': q.id })

    return render(request, 'question.html', {
        'question': q,
        'form' : form })

def ask_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        return render(request, 'ask_add_form.html',
                      { 'form' : form })
