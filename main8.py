import math


def dist(metry, cm):
    return math.ceil((float(cm)/2.7)*int(metry))

cm=12
metry=350

print(dist(metry, cm))