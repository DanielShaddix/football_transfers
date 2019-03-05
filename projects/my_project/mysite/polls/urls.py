from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^my_1polls_url$', views.indexpolls, name='index3'),
    # url(r'^polls/', include('polls.urls')),
    # url(r'^adminpolls/', admin.site.urls),

    # # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]


