# Правила игры в лото.
#
# Игра ведется с помощьюспе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с числами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.

from random import shuffle


class Sack:
    """
    constants
    """
    __SACK_SIZE = 90  # number of "kegs" in the "sack"

    def __init__(self):
        self._kegs_in_sack = [i for i in range(1, Sack.__SACK_SIZE + 1)]
        shuffle(self._kegs_in_sack)
        self._current_keg = 0

    def draw_keg(self, arg_num_to_draw=0):
        if arg_num_to_draw:
            start = self._current_keg
            self._current_keg += arg_num_to_draw
            return self._kegs_in_sack[start:self._current_keg]
        else:
            result = self._kegs_in_sack[self._current_keg]
            self._current_keg += 1
            return result


class Card:
    """
    constants
    """
    __LINES = 3  # quantity of lines on lotto card
    __LINE_PLACES = 9  # quantity of placeholders in each line
    __NUM_PER_LINE = 5  # quantity of numbers in each line
    __EMPTY_PLACES = __LINE_PLACES - __NUM_PER_LINE
    __DIVIDER_LEN = __LINE_PLACES * 3 - 1  # divider length
    __DIVIDER = __DIVIDER_LEN * '─' + '\n'  # divider string

    def __init__(self, arg_title):
        card_gen = Sack()
        self.sheet = []
        for i in range(Card.__LINES):
            numbers = card_gen.draw_keg(Card.__NUM_PER_LINE)
            numbers.sort()
            numbers = iter(numbers)
            line = [True] * Card.__NUM_PER_LINE + [''] * Card.__EMPTY_PLACES
            shuffle(line)
            for j in range(Card.__LINE_PLACES):
                if line[j]:
                    line[j] = next(numbers)
            self.sheet.append(line)
        self.title = arg_title
        self.not_crossed_numbers = Card.__LINES * Card.__NUM_PER_LINE

    def __str__(self):
        result = self.title.center(Card.__DIVIDER_LEN) + '\n' + Card.__DIVIDER
        for line in self.sheet:
            for element in line:
                result += '{:2} '.format(element)
            result += '\n'
            result += Card.__DIVIDER
        return result

    def cross(self, arg_number):
        for line in self.sheet:
            try:
                line[line.index(arg_number)] = ' ─'
                self.not_crossed_numbers -= 1
                return True
            except ValueError:
                pass
        return False

    def check(self, arg_number):
        for line in self.sheet:
            try:
                if line.index(arg_number) >= 0:
                    return True
            except ValueError:
                pass
        return False


class Lotto:
    def __init__(self):
        self.__sack = Sack()

    def game(self, arg_card1, arg_card2):
        in_game = True
        while in_game:
            keg = self.__sack.draw_keg()
            print('\n\nБочёнок №', keg)
            print(arg_card1)
            print(arg_card2)
            arg_card2.cross(keg)
            while True:
                user_answer = input('Зачеркнуть число? (y/n)? ')
                if user_answer in 'yY':
                    if arg_card1.cross(keg):
                        if arg_card1.not_crossed_numbers == 0:
                            if arg_card2.not_crossed_numbers == 0:
                                print('\n\nВы одновремнно вычеркнули все числа и сыграли вничью!')
                            else:
                                print('\n\nВы первыми вычеркнули все числа и победили!')
                            in_game = False
                    else:
                        print('\n\nТакого числа нет на вашей карточке. Вы проиграли!')
                        in_game = False
                    break
                elif user_answer in 'nN':
                    if arg_card1.check(keg):
                        print('\n\nТакое число есть на вашей карте! Вы проиграли!')
                        in_game = False
                    break
            if arg_card2.not_crossed_numbers == 0 and arg_card1.not_crossed_numbers > 0:
                print('\n\nКомпьютер первым вычеркнул все числа на своей карте. Вы проиграли!')
                in_game = False


player_card = Card('Ваша карточка')
computer_card = Card('Карточка компьютера')
current_game = Lotto()
current_game.game(player_card, computer_card)
