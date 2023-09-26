import random
from copy import copy


class QueenBoard:
    """
    инициализируем объект
    """
    def __init__(self, length: int):
        self.length = length
        self.board = []
        self.all_variants = []
        self._place_next_queen(0)

    """
    можем ли мы разместить ферзи на доске
    """

    def _can_we_place(self, rows: int, num: int):
        for i, value in enumerate(self.board):
            if value == num or (i - rows) == (value - num) or (i - rows) == (num - value):
                return False
        return True

    """
    поставить следующую королеву
    """

    def _place_next_queen(self, rows: int):
        if rows == self.length:
            self.all_variants.append(copy(self.board))
        else:
            for coll in range(self.length):
                if self._can_we_place(rows, coll):
                    self.board.append(coll)
                    self._place_next_queen(rows + 1)
                    self.board.pop()

    """
    проверка вариантов на доске
    """

    def check(self, board: list[int]):
        return board in self.all_variants


"""
генератор случайных чисел для случайной расстановки ферзей
"""


def get_random_board(board=None):
    if board is None:
        board = [0, 1, 2, 3, 4, 5, 6, 7]
    random.shuffle(board)
    return board


if __name__ == '__main__':
    length_of_board = 8
    my_boards = QueenBoard(length_of_board)
    print(my_boards.all_variants)
    get_board_from_user = [0] * length_of_board
    for count in range(length_of_board):
        row, col = (int(i) - 1 for i in input(f"Введите пару координат № {count + 1} через пробел: ").split(" "))
        get_board_from_user[col] = row
    print(get_board_from_user)
    print(my_boards.check(get_board_from_user))
    count = 0
    while count < 4:
        random_board = get_random_board()
        if my_boards.check(random_board):
            print(random_board)
            count += 1