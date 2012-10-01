from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from polls.models import Poll


urlpatterns = patterns('polls.views',


        #url(r'^$',"index", name="index_url"),

        url(r'^$',
            ListView.as_view(
                queryset=Poll.objects.order_by("-pub_date")[:5],
                context_object_name="latest_poll_list",
                template_name="polls/index.html"),
            name='poll_index'),

        #url(r'^(?P<poll_id>\d+)/$','detail',name="detail_url"),
        url(r'^(?P<pk>\d+)/$',
            DetailView.as_view(
                model=Poll,
                template_name='polls/detail.html'),
            name='poll_detail'),
        
        #url(r'^(?P<pk>\d+)/results/$','results',name="results_url"),
        url(r'^(?P<pk>\d+)/results/$',
            DetailView.as_view(
                model=Poll,
                template_name='polls/result.html'),
            name='poll_result'),
         

        url(r'^(?P<poll_id>\d+)/vote/$','vote',name="vote_url"),
)
