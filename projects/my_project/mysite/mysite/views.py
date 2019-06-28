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

# def get_player(request):
#     player = request.GET.get('id')
#     id = Transfers_List.objects.get(id=player)
#     obj={
#         'last name':id.last_names,
#         'name':id.names,
#         'age':id.age,
#         'price':id.price,
#         'club':id.club,
#     }
#     return JsonResponse(obj)

def get_player(request):
    player = request.GET.get('id')
    try:
        id = Transfers_List.objects.get(id=player)
        obj={
            'last name':id.last_names,
            'name':id.names,
            'age':id.age,
            'price':id.price,
            'club':id.club,
        }
    except Transfers_List.DoesNotExist:
        raise Http404('ID does not exist')
    return JsonResponse(obj)
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         print('-'*80)
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


# def get_player(request,players_id):
#     players = get_object_or_404(Transfers_List,pk=players_id)
#     context={
#         'players':players
#     }
#     return render(request,'mysite/transfer_index.html',context)


    # def vote(request, question_id):
    #     question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/detail.html', {'question': question})

    # return render(request.GET)


    # def cribdetail(request):
    #     post = Meekme.objects.get(id='id')
    #     return render_to_response('postdetail.html', {'post': post, 'Meekme': Meekme},
    #                               context_instance=RequestContext(request))
# def users(request):
#     id = request.GET.get("id", 1)
#     name = request.GET.get("name", "Tom")
#     output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
#     return HttpResponse(output)

# def index(request):
#     person = Person()
#     person.name = 'Alex'
#     person.email = 'Alex@gmail.com'
#     return render_to_response('person.html', {'p': person})

# def transfer_list_id(request):
#     player_id = Transfers_List.objects.all()
#     context = {
#         'player_id': player_id,
#     }
#     return render(request, 'mysite/transfer_index.html', context)
        #raise Exception("Not found")
# def transfer_list_id(request):
#     return HttpResponse("Hello, world. You're at the polls index. qweqwe <br> <b>qweqwe</b>")
    #         context={
    #             'player_id': player_id
    #         }
    # return render(request,'mysite/transfer_index.html',context)

# def transfer_list_id(request,player_id):
#     return HttpResponse( 'player' % player_id)


# def transfer_list_id(request):
#     all_last_names = Transfers_List.objects.all()
#     context ={
#         'all_last_names': all_last_names,
#      }
#     return render(request, 'mysite/transfer_index.html', context)



    # import gc
    #
    # def objects_by_id(id_):
    #     for obj in gc.get_objects():
    #         if id(obj) == id_:
    #             return obj
    #     raise Exception("No found")

# def upload_file(request):
#     call_club = Clubs(money=100)
#     if request.method == 'POST':
#         form = call_club(request.POST)
#         if form.is_valid():
#            (request.FILES[transfers])
#     return render_to_response('mysite/transfer_index.html')

# def transfer_site20(request):
#     call_club = Clubs(money=100)
#     file = open('mysite/transfers','w')
#     for player in file.players:


# def handle_uploaded_file(f):
#     destination = open('some/file/name.txt', 'wb+')
#     for chunk in f.chunks():
#         destination.write(chunk)
#     destination.close()

# def site(request):
#     call_club = Clubs(money=100)
#     context = {
#        'transfer': HttpResponse(call_club.show_players_rma(),call_club)
#
#     }
#     return render(request,'mysite/transfer.index', context)





# html
# json
# sql
