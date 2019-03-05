from django.http import HttpResponse, JsonResponse
from mysite import transfers
from mysite.transfers import Clubs
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.shortcuts import render


def index(request):
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
