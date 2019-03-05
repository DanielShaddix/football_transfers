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

    def show_players(self):
        return (self.rma, self.juv, self.tm)

    def show_players_rma(self):
        data=[]
        for player in self.rma:
            data += (player + '\n')
        return data

    def show_players_rma2(self):
        return self.rma

    def show_players_rma3(self):
        for key,value in self.rma.items():
            self.rma[key] = value
        return self.rma

    def show_players_rma4(self):
        return self.rma.items()

    # def show_players_rma3(self):
    #     club_rma = {}
    #     for key, value in self.rma.items():
    #         club_rma[key] = value
    #     return club_rma

    # def show_players_juv(self):
    #     data1 = []
    #     for player in self.juv:
    #         data1 += (player + '\n')
    #     return data1

    def add_to_team_real(self, player):
        if not player in self.tm:
            return ('I dont know this name - ')
        if player in self.tm:
            price = self.tm[player]
            if price > self.money:
                return ('U dont have enjoy money - ')
            if self.money > price:
                self.money -= price
                self.rma[player] = price
                del self.tm[player]
                return ('Successful')

        if not player in self.juv:
            return ('I dont know this name - ')
        if player in self.juv:
            price = self.juv[player]
            if price > self.money:
                return ('U dont have enjoy money - ')
            if self.money > price:
                self.money -= price
                self.rma[player] = price
                del self.juv[player]
            return ('Successful')







