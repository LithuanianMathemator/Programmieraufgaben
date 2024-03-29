
# Beispiel einer Int-Vektorklasse

import math

class IntVektor:

    def __init__(self, x, y, z):
        if type(x) != type(0) or type(y) != type(0)or type(z) != type(0):
            raise TypeError("Vektoreintrag keine ganze Zahl.")
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({0:n},{1:n},{2:n})'.format(self.x, self.y, self.z)

    def __getitem__(self, i):
        if type(i) != type(0):
            raise TypeError("Index keine ganze Zahl.")
        if i < 0 or i > 2:
            raise IndexError("Index nicht im zul. Bereich.")
        elif i == 0:
            return self.x
        elif i == 1:
            return self.y
        elif i == 2:
            return self.z

    def __add__(self, other):
        if isinstance(other, IntVektor):
            return IntVektor(self.x+other.x, self.y+other.y, self.z+other.z)
        else:
            raise TypeError("Formate passen nicht.")

    def __mul__(self, other):
        if isinstance(other, IntVektor):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == type(0):
            return IntVektor(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Formate passen nicht.")

    def __rmul__(self, other):
        if isinstance(other, IntVektor):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == type(0):
            return IntVektor(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Formate passen nicht.")

    def copy(self):
        return IntVektor(self.x, self.y, self.z)


class Teilgitter(IntVektor):

    def __init__(self, x, y, z):

        self.Koordinate_1 = y
        self.Koordinate_2 = x-(self.Koordinate_1 * 2)

        if (self.Koordinate_1 + (self.Koordinate_2 * 5)) != z:
            raise TypeError("Vektor liegt nicht im Teilgitter.")

        # use intvektor class for __init__
        super().__init__(x, y, z)

    def __str__(self):

        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+"); \
Koordinate 1: " + str(self.Koordinate_1) + ", \
Koordinate 2: " + str(self.Koordinate_2) + ""

    # for rest see intvektor, same implementation
    def __add__(self, other):

        if isinstance(other, Teilgitter):
            return Teilgitter(self.x+other.x, self.y+other.y, self.z+other.z)
        else:
            raise TypeError("Formate passen nicht.")

    def __mul__(self, other):

        if isinstance(other, Teilgitter):
            return super().__mul__(other)
        elif type(other) == type(0):
            return Teilgitter(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Formate passen nicht.")

    def __rmul__(self, other):

        if isinstance(other, Teilgitter):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == type(0):
            return Teilgitter(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Formate passen nicht.")

    def copy(self):

        intv = super().copy()

        gitter = Teilgitter(intv.x, intv.y, intv.z)

        return gitter
