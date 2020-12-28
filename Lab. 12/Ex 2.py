class TRational:
    def __init__(self, chiselnik, znamenuk):
        self.chiselnik = chiselnik
        self.znamenuk = znamenuk

    def add(self, num):
        self.chiselnik += num.chiselnik
        self.znamenuk += num.znamenuk

    def diff(self, num):
        self.chiselnik -= num.chiselnik
        self.znamenuk -= num.znamenuk

    def comp(self, num):
        self.chiselnik *= num.chiselnik
        self.znamenuk *= num.znamenuk

    def fract(self, num):
        self.chiselnik /= num.chiselnik
        self.znamenuk /= num.znamenuk

    def to_string(self):
        print(str(self.chiselnik) + "/" + str(self.znamenuk))