class Rect:
    def __init__(self):
        self._a = 0
        self._b = 0

    def __getitem__(self, key):
        if key == 'a':
            return self._a
        elif key == 'b':
            return self._b
        else:
            raise Exception("Wrong key")

    def __setitem__(self, key, value):
        if value > 0:
            if key == 'a':
                self._a = value
            elif key == 'b':
                self._b = value
            else:
                raise Exception("Wrong key")
        else:
            raise Exception("Length must be bigger than 0")

    @property
    def P(self):
        return (self._a * 2) + (self._b * 2)

    @property
    def S(self):
        return self._a * self._b