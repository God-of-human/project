from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'myapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'myapp/results.html'

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id) #获取对象，出现错误时抛出404异常，保证松散的耦合性，
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'myapp/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('myapp:results',args=(question_id,)))
