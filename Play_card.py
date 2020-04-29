import random

class Cards():
    def __init__(self):
        # Колода карт. Обозначение мастей В - буби, С -червы, Т - трефы, Р - пики.
        # J - валет, Q - дама, K - король, А - туз.
        self.koloda = ['6B', '6T', '6C', '6P', '7B', '7T', '7C', '7P', '8B', '8T', '8C', '8P', '9B', '9T', '9C', '9P',
                       '10B', '10T', '10C', '10P', 'JB', 'JT', 'JC', 'JP', 'QB', 'QT', 'QC', 'QP', 'KB', 'KT', 'KC', 'KP',
                       'AB', 'AT', 'AC', 'AP']
        # Игральная колода карт
        self.koloda_play = ['' for i in range(36)]
        self.cards_player1 = []
        self.cards_player2 = []
        self.kozyr=[]
        self.pole_plr_1 = []
        self.pole_plr_2 = []

    # Перемешивание колоды карт.
    def mix_koloda(self):
        i = 0

        while i < 36:
            tmp = random.randint(0,35)
            if self.koloda_play[tmp] == '':
                self.koloda_play[tmp] = self.koloda[i]
                i+=1
        print('Перемешанная колода', self.koloda_play)

    # Раздаем карты игрокам
    def give_cards(self):
       i = 0
       self.kozyr.append(self.koloda_play[35])
       while i<12:
            self.cards_player1.append(self.koloda_play[i])
            self.cards_player2.append(self.koloda_play[i+1])
            i+=2
       # Удаляем выданные карты из списка
       for i in range(12):
           self.koloda_play.pop(0)
       print('Остаток колоды', self.koloda_play)
       print('Козырь ', self.kozyr)
       print('карты 1', self.cards_player1)
       print('карты 2', self.cards_player2)

    def hod_plr_1(self):
        tmp = random.randint(0, 5)
        self.pole_plr_1 = self.cards_player1.pop(tmp)
        print('игрок 1 сходил ', self.pole_plr_1)
        print('карты 1', self.cards_player1)

    def hod_plr_2(self):
        tmp = random.randint(0, 5)
        self.pole_plr_2 = self.cards_player2.pop(tmp)
        print('игрок 2 сходил ', self.pole_plr_2)
        print('карты 2', self.cards_player2)

    def otbil_plr_1(self):
        pass
    def otbil_plr_1(self):
        pass
if __name__ == '__main__':
    card_game = Cards()
    card_game.mix_koloda()
    card_game.give_cards()
    card_game.hod_plr_1()
    card_game.hod_plr_2()