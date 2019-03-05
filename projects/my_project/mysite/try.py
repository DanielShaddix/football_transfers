rma_team = {'Bale':70, 'Benzema': 40, 'Modric': 25, 'Ramos': 30, 'Kroos': 75}
juv_team = {'Ronaldo': 90, 'Dybala': 100, 'Pjanic': 65, 'Bonucci': 35, 'Mandzukic': 25}
transfer_markt = {'Kane': 135, 'Mbape': 180, 'Neymar': 165, 'Piatek': 15, 'Ericson': 75}
money = 100


class Clubs(object):
    def __init__(self, money):
        self.rma = rma_team
        self.juv = juv_team
        self.tm = transfer_markt
        self.money = money

    def show_players_rma(self):
        data=[]
        for player in self.rma:
            data += (player + '\n')
        return data

call_club = Clubs(money=100)
print(call_club.show_players_rma())