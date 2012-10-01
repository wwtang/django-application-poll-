# Create your views here.


from django.http import HttpResponse
from polls.models import Poll, Choice
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse



def index(request):
    #data retrived from model|queryset|mysql
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #get template
    #tmplt = loader.get_template('polls/index.html')
    #create Context dict for data
    #cntxt = Context({
    #    "latest_p_list":latest_poll_list,
    #    })
    #output= ", ".join([p.question for p in latest_poll_list])
    #
    return render_to_response('polls/index.html',{"latest_p_list":latest_poll_list})


def detail(request, poll_id):
    #try:
    #    p = Poll.objects.get(pk=poll_id)
    #except Poll.DoesNotExist:
    #    raise Http404
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html',{"poll": p},context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)

    return render_to_response('polls/result.html',{'poll':p})

def vote(request, poll_id):

    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):

        return render_to_response("polls/detail.html",{
            'poll':p,
            'error_message': "You did not selsect a choice.",
            }, context_instance=RequestContext(request))
    else:
        selected_choice.votes +=1
        selected_choice.save()
    
        return HttpResponseRedirect(reverse('poll_result',args=(p.id,)))
