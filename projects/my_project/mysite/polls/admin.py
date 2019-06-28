from django.contrib import admin

from .models import Question, Choice, Addition,Transfers_List
from mysite import transfers


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date',)

class Transfers_ListAdmin(admin.ModelAdmin):
    list_display = ('id','last_names','names','age','club','price')


    # def players(self,obj):
    #     p = Transfers_List.objects.filter(players_id=obj.pk)
    #     return list(p)
#call_club = transfers.Clubs(money=100)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Addition)
admin.site.register(Transfers_List,Transfers_ListAdmin)

#admin.site.register(DictModelClubs)

# Register your models here.
