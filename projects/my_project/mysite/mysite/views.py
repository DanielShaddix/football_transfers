from django.http import HttpResponse, JsonResponse
from mysite import transfers
from mysite.transfers import Clubs
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.shortcuts import render
from polls.models import Question,Transfers_List
from django.shortcuts import get_object_or_404, render,Http404
import gc
from urllib import request
import json

def index0(request):
    return HttpResponse("Hello, world. You're at the polls index. qweqwe <br> <b>qweqwe</b>")


def index_json(request):
    obj = {
        'product': {
            'name': 'samsung',
            'color': 'red',
        }
    }
    return JsonResponse(obj)



def transfer_site(request):
    call_club = Clubs(money=100)
    return HttpResponse(call_club.show_players_rma(),call_club)

def transfer_site2old(request):
    template = loader.get_template('mysite/transfer_index.html')
    context = RequestContext(request, {
        'call': '000000',
        'transfer2': 'HttpResponse(Clubs(money=100).show_players_rma(),call_club)'
        # 'call': transfer_site(request),
    })
    return HttpResponse(template.render(context))

#'transfer':'HttpResponse(Clubs(money=100).show_players_rma(),call_club)',


#
# def transfer_site2(request):
#     call_club = Clubs(money=100)
#     context = {'a': '12312123','transfer2':(request.transfers)}
#     return render(request, 'mysite/transfer_index.html', context)


# def transfer_site2(request):
#     call_club = Clubs(money=100)
#     strng = ''
#     for player in call_club.show_players_rma():
#         strng += str(player) +'\n'
#     context = {'a': '12312123', 'rma': strng}
#     return render(request, 'mysite/transfer_index.html', context)

# def transfer_site2(request):
#     context = {'a': '12312123', 'rma': Clubs(money=100).show_players_rma2()}
#     return render(request, 'mysite/transfer_index.html', context)

def transfer_site2(request):
    context = {'rma2':Clubs(money=100).show_players_rma4()}
    return render(request, 'mysite/transfer_index.html', context)

def transfer_site5(request):
    call_club = Clubs(money=100)
    return HttpResponse(call_club.show_players_rma(),call_club)

def transfer_list(request):
    all_last_names = Transfers_List.objects.all()
    context ={
        'all_last_names': all_last_names,
     }
    return render(request, 'mysite/transfer_index.html', context)


# def transfer_list_id(request,id_):
#     for Transfers_List.objects in gc.get_objects():
#         if id(Transfers_List) == id_:
#             return Transfers_List
#         raise Exception("Not found")
def transfer_list_id(request):
    player = Transfers_List.objects.get(id='id')
    context={
        'player':player
    }
    return render(request,'mysite/transfer_index.html',context)

def get_player(request):
    player = request.GET.get('id_player')
    try:
        id_player = Transfers_List.objects.get(id=player)
        obj={
            'last name':id_player.last_names,
            'name':id_player.names,
            'age':id_player.age,
            'price':id_player.price,
            'club':id_player.club,
        }
    except Transfers_List.DoesNotExist:
        raise Http404('ID does not exist')
    return JsonResponse(obj)

def players(request):
    people=Transfers_List.objects.all()
    players = []
    for id_player in people:
        obj={
            'last name': id_player.last_names,
            'name': id_player.names,
            'age': id_player.age,
            'price': id_player.price,
            'club': id_player.club,
        }
        players.append(obj)
    return JsonResponse(players,safe=False)

def try_p(request):
    list_to_json = [{"title": '1', "link": '2', "date": 3}, {'title_2':'1'}]
    return JsonResponse(list_to_json, safe=False)

# def playrs_and_get_player(request):
#     players = []
#     people = Transfers_List.objects.all()
#     for id_player in people:
#         player = request.GET.get('id_player')
#         try:
#             id_player = people.get(id=player)
#             obj = {
#             'last name': id_player.last_names,
#             'name': id_player.names,
#             'age': id_player.age,
#             'price': id_player.price,
#             'club': id_player.club,
#             }
#             players.append(obj)
#         except Transfers_List.DoesNotExist:
#             raise Http404('ID does not exist')
#     return JsonResponse(players,safe=False)







# html
# json
# sql
obj = {
            'last name': 'value_l_n',
            'name': 'value_n',
            'age': 'value_a',
            'price': 'value_p',
            'club': 'value_c',
        }

def player_get(request):
    player = request.GET.get('id_player')
    try:
        id_player = Transfers_List.objects.get(id=player)
        obj.update((k,id_player.last_names) for k,v in obj.items()if v=='value_l_n')
        obj.update((k, id_player.names) for k, v in obj.items() if v == 'value_n')
        obj.update((k, id_player.age) for k, v in obj.items() if v == 'value_a')
        obj.update((k, id_player.price) for k, v in obj.items() if v == 'value_p')
        obj.update((k, id_player.club) for k, v in obj.items() if v == 'value_c')
    except Transfers_List.DoesNotExist:
        raise Http404('ID does not exist')
    return JsonResponse(obj)

def get_players(request):
    people = Transfers_List.objects.all()
    players = []
    for id_player in people:
        obj.update((k, id_player.last_names) for k, v in obj.items() if v == 'value_l_n')
        obj.update((k, id_player.names) for k, v in obj.items() if v == 'value_n')
        obj.update((k, id_player.age) for k, v in obj.items() if v == 'value_a')
        obj.update((k, id_player.price) for k, v in obj.items() if v == 'value_p')
        obj.update((k, id_player.club) for k, v in obj.items() if v == 'value_c')
        players.append(obj)
    return JsonResponse(players, safe=False)

def table_data(id_players):
    obj = {
        'last name': id_players.last_names,
        'name': id_players.names,
        'age': id_players.age,
        'price': id_players.price,
        'club': id_players.club
    }
    return (obj)

def get_players_table(request):
    id_players = Transfers_List.objects.all()
    players = []
    for id_player in id_players:
        players_list = table_data(id_player)
        players.append(players_list)
    return JsonResponse(players, safe=False)

def get_player_table_by_id(request):
    player = request.GET.get('id_player')
    try:
        id_player = Transfers_List.objects.get(id=player)
        players_list = table_data(id_player)
    except Transfers_List.DoesNotExist:
        raise Http404('ID does not exist')
    return JsonResponse(players_list)


def get_player_table_by_id_2(request,id_player):
    try:
        id_player = Transfers_List.objects.get(id=id_player)
        players_list = table_data(id_player)
    except Transfers_List.DoesNotExist:
        raise Http404('ID does not exist')
    return JsonResponse(players_list)



# def users(request, id, name):
#     output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
#     return HttpResponse(output)


#  deff get_player(request):
#     player = request.GET.get('id_player')
#     try:
#         id_player = Transfers_List.objects.get(id=player)
#         obj={
#             'last name':id_player.last_names,
#             'name':id_player.names,
#             'age':id_player.age,
#             'price':id_player.price,
#             'club':id_player.club,
#         }
#     except Transfers_List.DoesNotExist:
#         raise Http404('ID does not exist')
#     return JsonResponse(obj)




# def get_players_table(request):
#     # players_list = table_data()
#     # players = []
#     # for id_player in players_list:
#     #     players.append(id_player)
#     return JsonResponse([], safe=False)

# def get_player_table(request):
#     player_list = table_data()
#     player = request.GET.get('id_player')
#     try:
#         id_player = Transfers_List.objects.get(id=player)
#     except Transfers_List.DoesNotExist:
#         raise Http404('ID does not exist')
#     return JsonResponse(obj)
