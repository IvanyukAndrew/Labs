class TSquare:

    def __init__(self, length_side = 0):
        if length_side < 0:
            raise Exception('Side length should be positive')
        else:
            self.__side_len = length_side

    @property
    def side_length(self):
        return self.__length_side

    @side_length.setter
    def side_length(self, x):
        if x < 0:
            raise Exception('Side length should be positive')
        else:
            self.__slength_side = x

    @property
    def square_area(self):
        return self.__length_side ** 2

    @property
    def square_perimeter(self):
        return self.__length_side * 4

    def enter_side(self):
        self.length_side = float(input("Enter side length: "))

    def show_side(self):
        print(self.length_side)

    def __add__(self, other):
        return TSquare(self.side_length + other.side_length)

    def __sub__(self, other):
        return TSquare(self.side_length - other.side_length)

    def __mul__(self, other):
        return TSquare(self.side_length * other)