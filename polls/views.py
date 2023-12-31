from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import darcekform
from datetime import datetime  # Import datetime
from .models import Choice, Question, darcek

def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]

def IndexView(request):
    darceks = darcek.objects.all()[:12]
    return render(request,'polls/index.html',{'darceks':darceks})    

def AddView(request):
    if request.method == 'POST':
        form = darcekform(request.POST)
        if form.is_valid():
            darcek = form.save(commit=False)
            darcek.pub_date = datetime.now()  # Set pub_date to the current date and time
            darcek.save()
            return redirect('./')  # Redirect to a success page
    else:
        form = darcekform()

    return render(request, 'polls/add.html', {'form': form})

def delete_darcek(request, darcek_id):
    # Retrieve the Darcek object based on its primary key (id)
    darcek = get_object_or_404(Darcek, pk=darcek_id)

    if request.method == 'POST':
        # If the request is a POST request, delete the object and redirect
        darcek.delete()
        return redirect('success_page')  # Redirect to a success page or any desired URL

    return render(request, 'polls/delete.html', {'darcek': darcek})
# def AddView(request):
#     if request.method == 'POST':
#         form = darcekform(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to the snippets page after successful submission
#             return redirect('add')  
#     else:
#         form = darcekform()

#     return render(request, 'polls/add.html', {'form': form})


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
