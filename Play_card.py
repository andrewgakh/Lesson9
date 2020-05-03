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
        self.koloda_play = ['' for i in range(36)]      # Игральная колода карт
        self.cards_player2= []                          # Карты игрока 1
        self.cards_player1 = []                         # Карты игрока 2
        self.kozyr=[]                                   # Козырная карта
        self.pole_plr_2 = []                            # Ход игрока 1
        self.pole_plr_1 = []                            # Ход игрока 2
        self.win_plr_1 = 0                              # Игрок 1 отбил ход игрока 2
        self.win_plr_2 = 0                              # Игрок 2 отбил ход игрока 1
        self.min_koz=[]                                 # Минимальный козырь в картах игрока

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
       print()
       print('карты 1', self.cards_player1)
       print('карты 2', self.cards_player2)

    # Ход Игрока 1.
    def hod_plr_1(self):
        tmp = random.randint(0, 5)
        self.pole_plr_1 = self.cards_player1.pop(tmp)
        print()
        print('Ход игрока 1 ', self.pole_plr_1)
        #print('карты 1', self.cards_player1)
        print()

    # Ход Игрока 2.
    def hod_plr_2(self):
        tmp = random.randint(0, 5)
        self.pole_plr_2 = self.cards_player2.pop(tmp)
        print()
        print('Ход игрока 2 ', self.pole_plr_2)
        #print('карты 2', self.cards_player2)
        print()

    # Ответный ход Игрока 1. Ищет карту старше по масти, если нет ищет минимальную козырную карту. Иначе забирает карту.
    # Если карта бита берут по карте из колоды Игрок 2 затем Игрок 1. Если карта не бита карту берет только Игрок 2.
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
        if self.win_plr_1 == 0:
            # min = self.kozyr[2]
            min = 14
            crd_tmp_list = self.cards_player1
            for i in range(len(crd_tmp_list)):
                crd_tmp = crd_tmp_list[i]
                if  crd_tmp[2] < min and crd_tmp[1] == self.kozyr[1]:
                    min = crd_tmp[2]
                    self.min_koz = crd_tmp
                    koz_flag = 1
                    n = i
            if koz_flag == 1:
                self.pole_plr_1 = self.cards_player1.pop(n)
                self.win_plr_1 = 1

        if self.win_plr_1  == 1:
            # Берем по карте из колоды
            if len(self.cards_player2) < 7:
                    self.cards_player2.append(self.koloda_play.pop(0))
            if len(self.cards_player1) < 7:
                    self.cards_player1.append(self.koloda_play.pop(0))
            print('Игрок 1. Карта игрока 2 БИТА ', self.pole_plr_1 )
            print('карты 1', self.cards_player1)
            print('карты 2', self.cards_player2)
        else:
            self.win_plr_2 = 1
            # Берет карту из колоды игрок 2
            if len(self.cards_player2) < 7:
                self.cards_player2.append(self.koloda_play.pop(0))
            self.cards_player1.append(self.pole_plr_2)
            print('Игрок 1. Карта игрока 2 НЕ БИТА. Принимаю карту ', self.pole_plr_2)
            print('карты 1', self.cards_player1)
            print('карты 2', self.cards_player2)
        self.pole_plr_1.clear()
        self.pole_plr_2.clear()
        self.min_koz.clear()
        koz_flag = 0

    # Ответный ход Игрока 2. Ищет карту старше по масти, если нет ищет минимальную козырную карту. Иначе забирает карту.
    # Если карта бита берут по карте из колоды Игрок 1 затем Игрок 2. Если карта не бита карту берет только Игрок 1.
    def otbil_plr_2(self):
        crd_tmp_list = self.cards_player2
        koz_flag = 0  # Указывает наличие козыря
        num = 0
        mast = self.kozyr[1]
        # Определяем наличие карты, которая имеет больший вес той же масти
        for i in range(len(crd_tmp_list)):
            crd_tmp = crd_tmp_list[i]
            if crd_tmp[2] > self.pole_plr_1[2] and crd_tmp[1] == self.pole_plr_1[1]:
                self.pole_plr_2 = self.cards_player2.pop(i)
                self.win_plr_2 = 1
                break
        #  Определяем мин. козырь
        if self.win_plr_2 == 0:
            # min = self.kozyr[2]
            min = 14
            crd_tmp_list = self.cards_player2
            for i in range(len(crd_tmp_list)):
                crd_tmp = crd_tmp_list[i]
                if crd_tmp[2] < min and crd_tmp[1] == self.kozyr[1]:
                    min = crd_tmp[2]
                    self.min_koz = crd_tmp
                    koz_flag = 1
                    n = i
            if koz_flag == 1:
                self.pole_plr_2 = self.cards_player2.pop(n)
                self.win_plr_2 = 1

        if self.win_plr_2 == 1:
            # Берем по карте из колоды
            if len(self.cards_player1) < 7:
                self.cards_player1.append(self.koloda_play.pop(0))
            if len(self.cards_player2) < 7:
                    self.cards_player2.append(self.koloda_play.pop(0))
            print('Игрок 2. Карта игрока 1 БИТА ', self.pole_plr_2)
            print('карты 2', self.cards_player2)
            print('карты 1', self.cards_player1)
        else:
            self.win_plr_1 = 1
            # Берет карту из колоды игрок 1
            if len(self.cards_player1) < 7:
                self.cards_player1.append(self.koloda_play.pop(0))
            self.cards_player2.append(self.pole_plr_1)
            print('Карта игрока 1 НЕ БИТА. Принимаю карту ', self.pole_plr_1)
            print('карты 2', self.cards_player2)
            print('карты 1', self.cards_player1)
        self.pole_plr_1.clear()
        self.pole_plr_2.clear()
        self.min_koz.clear()
        koz_flag = 0

if __name__ == '__main__':
     card_game = Cards()
    #card_game.otbil_plr_1()
    # card_game.mix_koloda()
    # card_game.give_cards()
    # card_game.win_plr_1 = 1
    #
    # for i in range(3):
    #     if card_game.win_plr_1 == 1:
    #         card_game.win_plr_1 = 0
    #         card_game.hod_plr_1()
    #         card_game.otbil_plr_2()
    #     elif card_game.win_plr_2 == 1:
    #         card_game.win_plr_2 = 0
    #         card_game.hod_plr_2()
    #         card_game.otbil_plr_1()
