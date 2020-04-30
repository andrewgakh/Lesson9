import random

class Cards():
    def __init__(self):
        # Колода карт. Обозначение мастей В - буби, С -червы, Т - трефы, Р - пики.
        # J - валет, Q - дама, K - король, А - туз.
        self.koloda = [['6','B', 6], ['6', 'C', 6], ['6', 'T', 6], ['6', 'P', 6],
                       ['7', 'B', 7], ['7', 'C', 7], ['7', 'T', 7], ['7', 'P', 7],
                       ['8', 'B', 8], ['8', 'C', 8], ['8', 'T', 8], ['8', 'P', 8],
                       ['9', 'B', 9], ['9', 'C', 9], ['7', 'T', 9], ['9', 'P', 9],
                       ['10', 'B', 10], ['10', 'C', 10], ['10', 'T', 10], ['10', 'P', 10],
                       ['J', 'B', 11], ['J', 'C', 11], ['J', 'T', 11], ['J', 'P', 11],
                       ['Q', 'B', 12], ['Q', 'C', 12], ['Q', 'T', 12], ['Q', 'P', 12],
                       ['K', 'B', 13], ['K', 'C', 13], ['K', 'T', 13], ['K', 'P', 13],
                       ['A', 'B', 14], ['A', 'C', 14], ['A', 'T', 14], ['A', 'P', 14]]
        #self.dict_ves_card = {'6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        # Игральная колода карт
        self.koloda_play = ['' for i in range(36)]
        self.cards_player1 = []
        self.cards_player2 = []
        self.kozyr=[]
        self.pole_plr_1 = []
        self.pole_plr_2 = []
        self.win_plr_1 = 0
        self.win_plr_2 = 0

        self.min_koz=[]

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
       self.kozyr = self.koloda_play[35]
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
        print()
        print('Ход игрока 2 ', self.pole_plr_2)
        print('карты 2', self.cards_player2)
        print()

    def min_koz_card(self, x):
        tmp_list = ''
        for i in range(len(x)):
            tmp = x[i]
            if  tmp[1] == self.kozyr[1]:
                tmp_list.append(tmp) # лист с козырными картами

        min = 14
        for i in range(len(tmp_list)):
            tmp = tmp_list[i]
            self.ves_card(tmp[0])
            if self.ves_crd < min:
                min = self.ves_crd
                self.min_koz = tmp


        #tmp_koz_card



    def otbil_plr_1(self):
        crd_tmp_list = self.cards_player1
        koz_flag = 0    # Указывает наличие козыря
        num = 0
        mast = self.kozyr[1]
        # Определяем наличие карты, которая имеет больший вес той же масти
        for i in range(len(crd_tmp_list)):
            crd_tmp = crd_tmp_list[i]
            if  crd_tmp[2] > self.pole_plr_2[2] and crd_tmp[1] == self.pole_plr_2[1]:
                self.pole_plr_1 = self.cards_player1.pop(i)
                self.win_plr_1 = 1
                break
        #  Определяем мин. козырь
        min = self.kozyr[2]
        crd_tmp_list = self.cards_player1
        for i in range(len(crd_tmp_list)):
            crd_tmp = crd_tmp_list[i]
            if  crd_tmp[2] < min and crd_tmp[1] == self.kozyr[1]:
                min = crd_tmp[2]
                self.min_koz = crd_tmp
                koz_flag = 1
                n = i
        if koz_flag == 1:
            self.pole_plr_1 = self.cards_player1.pop(num)
            self.win_plr_1 = 1

        #print('Минимальный козырь', self.min_koz)

        if self.win_plr_1  == 1:
            # Берем по карте из колоды
            self.cards_player2.append(self.koloda_play.pop(0))
            self.cards_player1.append(self.koloda_play.pop(0))
            print('Карта игрока 2 БИТА ', self.pole_plr_1 )
            print('карты 1', self.cards_player1)
        else:
            self.win_plr_2 = 1
            # Берет карту из колоды игрок 2
            self.cards_player2.append(self.koloda_play.pop(0))
            self.cards_player1.append(self.pole_plr_2)
            print('Карта игрока 2 НЕ БИТА ', self.pole_plr_1)
            print('карты 1', self.cards_player1)
            print('карты 2', self.cards_player2)

    def otbil_plr_2(self):
        pass
if __name__ == '__main__':
    card_game = Cards()
    card_game.mix_koloda()
    card_game.give_cards()
    #card_game.hod_plr_1()
    card_game.hod_plr_2()
    card_game.otbil_plr_1()