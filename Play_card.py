import random

class Cards():
    def __init__(self):
        # Колода карт. Обозначение мастей В - буби, С -червы, Т - трефы, Р - пики.
        # J - валет, Q - дама, K - король, А - туз.
        self.koloda = ['6B', '6T', '6C', '6P', '7B', '7T', '7C', '7P', '8B', '8T', '8C', '8P', '9B', '9T', '9C', '9P',
                       '10B', '10T', '10C', '10P', 'JB', 'JT', 'JC', 'JP', 'QB', 'QT', 'QC', 'QP', 'KB', 'KT', 'KC', 'KP',
                       'AB', 'AT', 'AC', 'AP']
        self.dict_ves_card = {'6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
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
        # Определяем вес и масть карты, с которой пошел игрок 2.
        crd_tmp = str(self.pole_plr_2)
        crd_num2 = crd_tmp[0]
        crd_mst2 = crd_tmp[1]    # масть карты
        list_ves_crd = list(self.dict_ves_card.items())
        for i in range(len(self.dict_ves_card)):
            tmp = list_ves_crd[i]
            if crd_num2 == tmp[0]:
                ves_crd2 = tmp[1]    # вес карты
        #print('Карта игрока 2', ves_crd2, crd_mst2)

        # Определяем карту для ответа или принимаем карту игрока 2
        crd_tmp_list = self.cards_player1
        for i in range(len(crd_tmp_list)):
            # crd_tmp = str(crd_tmp_list[i])
            # crd_num1 = crd_tmp[0]
            # crd_mst1 = crd_tmp[1]

            for j in range(len(self.dict_ves_card)):
                crd_tmp = str(crd_tmp_list[i])
                crd_num1 = crd_tmp[0]
                crd_mst1 = crd_tmp[1]
                tmp = list_ves_crd[j]
                if crd_num1 == tmp[0]:
                    ves_crd1 = tmp[1]
                    if  ves_crd1 > ves_crd2 and crd_mst1 == crd_mst2:
                        self.pole_plr_1 = self.cards_player1.pop(i)
                        break
        print('Карта игрока 1 БИТА ', self.pole_plr_1 )




    def otbil_plr_2(self):
        pass
if __name__ == '__main__':
    card_game = Cards()
    card_game.mix_koloda()
    card_game.give_cards()
    #card_game.hod_plr_1()
    card_game.hod_plr_2()
    card_game.otbil_plr_1()