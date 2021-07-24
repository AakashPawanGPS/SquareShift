import math


def isPrime(n):
    if (n == 1):
        return 0
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return 0
    return 1


def isMul2n(n):
    return n & (n - 1)


def orderSeating(seating):
    prime = []
    power_of_2 = []
    Others = []
    for idx in seating:
        if (isPrime(idx) == 1):
            prime.append(idx)
        elif (isMul2n(idx) == 0):
            power_of_2.append(idx)
        else:
            Others.append(idx)
    seating = prime
    seating.extend(power_of_2)
    seating.extend(Others)
    print(seating)
    return seating


def AisleSeats(aeroplane_seating, passenger_idx):
    i = j = 0
    k = -1
    index = 0
    for idx in passenger_idx:
        try:
            aeroplane_seating[i][j][k] = passenger_idx[index]
            index = index + 1
        except:
            return aeroplane_seating, index
        if k == -1:
            i = i + 1
            k = 0
        else:
            k = -1
            if i == len(aeroplane_seating) - 1:
                i = 0
                j = j + 1

    return aeroplane_seating, index


def WindowSeats(aeroplane_seating, passenger_idx):
    i = j = k = 0
    index = 0
    for idx in passenger_idx:
        try:
            aeroplane_seating[i][j][k] = passenger_idx[index]
            index = index + 1
        except:
            return aeroplane_seating, index
        if i == 0:
            i = k = -1
        elif i == -1:
            i = k = 0
            j = j + 1

    return aeroplane_seating, index


def MiddleSeats(aeroplane_seating, passenger_idx):
    i = j = 0
    k = 1
    index = 0
    for idx in passenger_idx:
        try:
            aeroplane_seating[i][j][k] = passenger_idx[index]
            k = k + 1
            index = index + 1
        except:
            return aeroplane_seating
        if k == len(aeroplane_seating[i][j]) - 1:
            k = 1
            i = i + 1

        if i == len(aeroplane_seating[i][j]) - 1:
            i = 0
            j = j + 1

    return aeroplane_seating