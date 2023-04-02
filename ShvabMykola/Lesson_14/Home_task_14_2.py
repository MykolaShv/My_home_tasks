class Chess_figure():
    colour = 'white' or 'black'
    place_figure = x, y = 5, 5

    def change_colour(self):
        if self.colour == 'black':
            return 'white'
        else:
            return 'black'

    def valid_place(self):
        a = self.a
        b = self.b
        return 0 < a < 9 and  0 < b < 9


class King(Chess_figure):
    def check(self):
        self.a, self.b = a, b
        if self.valid_place():
            return abs(self.a - self.x) <= 1 and abs(self.b - self.y) <= 1
        else:
            return('out')


class Queen(Chess_figure):
    def check(self):
        self.a, self.b = a, b
        if self.valid_place():
            return abs(self.a - self.b) == abs(self.x - self.y) or self.a == self.x \
                   or self.b == self.y
        else:
            return ('out')


class Rook(Chess_figure):
    def check(self):
        self.a, self.b = a, b
        if self.valid_place():
            return abs(self.a - self.b) == abs(self.x - self.y)
        else:
            return ('out')


class Bishop(Chess_figure):
    def check(self):
        self.a, self.b = a, b
        if self.valid_place():
            return self.a == self.x or self.b == self.y
        else:
            return ('out')

class Knight(Chess_figure):
    def check(self):
        self.a, self.b = a, b
        if self.valid_place():
            delta_x, delta_y = abs(self.a - self.x), abs(self.b - self.y)
            return delta_x == 1 and delta_y == 2 or delta_x == 2 and delta_y == 1
        else:
            return ('out')

class Pawn(Chess_figure):
    def check(self):
        self.colour = colour
        self.a, self.b = a, b
        if self.valid_place():
            return self.colour == 'white' and self.a ==  self.x and self.b - self.y == 1\
                or self.colour == 'black' and self.a ==  self.x and self.b - self.y == -1
        else:
            return ('out')



def out_result(a,b, colour):
    result_list = []
    king = King()
    if  king.check() == 'out':
        print(a, b, colour, 'The place is out of the board')
    else:
        if king.check(): result_list.append('King')
        queen = Queen()
        if queen.check(): result_list.append('Queen')
        rook = Rook()
        if rook.check(): result_list.append('Rook')
        bishop = Bishop()
        if bishop.check(): result_list.append('Bishop')
        knight = Knight()
        if knight.check(): result_list.append('Knight')
        pawn = Pawn()
        if pawn.check(): result_list.append('Pawn')
        print(a, b, colour, result_list) if result_list else print(a, b, colour, 'No figures')

a, b = 5, 6
colour = 'white'
out_result(a,b, colour)
a, b = 5, 10
colour = 'white'
out_result(a,b, colour)

a, b = -5, 3
colour = 'white'
out_result(a,b, colour)
a, b = 6, 6
colour = 'white'
out_result(a,b, colour)
a, b = 5, 4
colour = 'black'
out_result(a,b, colour)
a, b = 5, 4
colour = 'white'
out_result(a,b, colour)
a, b = 8, 8
colour = 'black'
out_result(a,b, colour)
a, b = 1, 2
colour = 'black'
out_result(a,b, colour)
