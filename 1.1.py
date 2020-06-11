from math import *

print("Problem 1.1")
# constants and variables
M = 1.9891 * 10 ** 30
G = 6.6738 * 10 ** (-11)
# for Earth
le = 1.4710 * 10 ** 11
ve = 3.0287 * 10 ** 4
# for Halley's comet
lh = 8.7830 * 10 ** 10
vh = 5.4529 * 10 ** 4


# functions
def coefficient2(v, l):
    cof2 = (-(2 * G * M) / (v * l))
    return cof2


def coefficient3(v, l):
    cof3 = -(v ** 2 - ((2 * G * M) / l))
    return cof3


def quad(a, b, c):
    # print("First method: ")
    if (b ** 2 - 4 * (a * c)) < 0:
        print("non real answer")
    elif (b ** 2 - 4 * (a * c)) == 0:  # if it is zero there is only one answer, + or - zero is the same thing
        x1 = ((-b + sqrt((b ** 2) - (4 * (a * c)))) / (2 * a))
    else:
        x1 = ((-b + sqrt((b ** 2) - (4 * (a * c)))) / (
                    2 * a))  # error when adding because the top is very close to zero
        x2 = ((-b - sqrt((b ** 2) - (4 * (a * c)))) / (2 * a))
    if (b ** 2 - 4 * a * c) < 0:
        print("non real answer")
    elif (b ** 2 - 4 * (a * c)) == 0:
        x_1 = ((2 * c) / (-b) - sqrt((b ** 2) - 4 * (a * c)))
    else:
        x_1 = ((2 * c) / ((-b) - sqrt((b ** 2) - 4 * (a * c))))
        x_2 = ((2 * c) / ((-b) + sqrt((b ** 2) - 4 * (a * c))))
    # we want to return the accurate answers which would be x_1 (first x method 2) and x2 (second x first method)
    # print("Best results: ",x_1, x2)
    if (x_1 < x2):
        return x_1
    else:
        return x2


def calculations(l1, l2, v1):
    print("semi-major axis")
    a = (1.0 / 2.0) * (l1 + l2)
    print(a)
    print("semi-minor axis")
    b = sqrt(l1 * l2)
    print(b)
    print("orbital period")
    T = ((2 * pi * a * b) / (l1 * v1 * 3.154 * 10 ** 7))
    print(T)
    print("Orbital eccentricity")
    e = (l2 - l1) / (l2 + l1)
    print(e)


# for Earth:
Ec2 = coefficient2(ve, le)
Ec3 = coefficient3(ve, le)
quad(1, Ec2, Ec3)
l2e = le * ve / quad(1, Ec2, Ec3)

# for Halley's:
Hc2 = coefficient2(vh, lh)
Hc3 = coefficient3(vh, lh)
quad(1, Hc2, Hc3)
l2h = lh * vh / quad(1, Hc2, Hc3)

print("Earth")
calculations(le, l2e, ve)
print()
print("Halley's")
calculations(lh, l2h, vh)
