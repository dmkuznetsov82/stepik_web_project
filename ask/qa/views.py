from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

#from django.http import HttpResponse
from django.core.paginator import Paginator

from qa.models import Question

# Create your views here.

# def test(request, *args, **kwargs):
#     return HttpResponse('OK')

def question_list_new(request):
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page' , 1)

    questions = Question.objects.new(page)

    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'new.html', {
        'posts' : page.object_list,
        'paginator' : paginator,
        'page' : page,
    })

# def question_list_new(request):
#     page = request.GET.get('page')
#     questions = Question.objects.new(page)
#     return render(request, 'qa/question_list_main.html', {
#         'questions' : questions,
#         'page' : questions.id,
#     })

@require_GET
def question_details(request, id):
    question = get_object_or_404(Post, id=id)
    return render(request, 'details.html', {
        'question': question,
    })