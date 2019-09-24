"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls import url, include

from polls import views
from mysite import views
from mysite.views import index0, index_json, transfer_site, transfer_site2,transfer_list,get_player,players,try_p,player_get,get_players,transfer_list_id,get_players_table,get_player_table_by_id, get_player_table_by_id_2
#from  polls.views import index,detail,vote,results

#from mysite import views
#from  mysite.views import get_player_table_by_id_2

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^my_1_url$', index0, name='index'),
    url(r'^my_2_url$', index_json, name='index2'),
    url(r'^', include('polls.urls')),
    url(r'^transfetransfer_site_urlr_site_url$', transfer_site, name= 'transfer_url'),
    url(r'^transfer_site2_url$',transfer_site2, name= 'transfer_url2'),
    url(r'^transfer_list$',transfer_list,name='transfer_list'),
    url(r'^get_player$',get_player,name='get_player'),# ВЫЗОВ МЕТОДА "get_player"
    url(r'^players$',players, name='players'),
    url(r'^try_p$',try_p, name='try_p'),
    url(r'^player_get',player_get,name='player_get'),
    url(r'^get_players$',get_players, name='get_players'),
    url(r'^get_players_table$',get_players_table, name='get_players_table'),
    url(r'^get_player_table_by_id$',get_player_table_by_id,name='get_player_table_by_id'),
    #url(r'^get_player_table_by_id_2/(?P<id_player>[0-4]+)/$',get_player_table_by_id_2,name='get_player_table_by_id_2'),
    #url(r'^get_player_table_by_id_2/id_player$', views.get_player_table_by_id_2, name='get_player_table_by_id_2'),
    url(r'^get_player_table_by_id_2/(?P<id_player>[0-9])/$', get_player_table_by_id_2, name='get_player_table_by_id_2'),
    #url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),

    #url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
    #re_path(r'^get_player_table_by_id_2/(?P<id>\d+)/(?P<name>\D+)/', get_player_table_by_id_2),
    #url(r'^(?P<players_id>[0-4]+)/$', get_player, name='get_player'),
    #url(r'^transfer_list_id$',transfer_list_id,name='transfer_list_id'),
    #url(r'^(?P<player_id>[0-1]+)/transfer_list_id/$', transfer_list_id, name='transfer_list_id'),
    #url(r'^transfer_list_id$',transfer_list_id==1,name='transfer_list_id'),

    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    #url(r'^polls/latest\.html$', views.index),
]
