class Mathics:
    def __init__(self):
        self.matrix_el = []
        self.dimension = [0, 0]

    def enter_el(self):
        print("Вводіть значення кожного рядка через пробіл(Для завершення, введіть 0):\n")
        el = list(map(int, input().split(" ")))
        self.dimension[1] = len(el)
        self.matrix_el.append(el)
        while True:
            el = list(map(int, input().split(" ")))
            if len(el) > self.dimension[1] > len(el):
                print("Неправильна кількисть елементів рядка")
            elif el == [0]:
                break
            else:
                self.matrix_el.append(el)
        self.dimension[0] = len(self.matrix_el)

    def output_of_matrix_el(self):
        for i in self.matrix_el:
            print(i)

    def max_el(self):
        return print(max(self.matrix_el))

    def min_el(self):
        return print(min(self.matrix_el))