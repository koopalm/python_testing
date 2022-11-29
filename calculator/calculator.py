def plus(luku1:int, luku2:int):
    return float(luku1 + luku2)

def miinus(luku1:int, luku2:int):
    return float(luku1 - luku2)

def jako(luku1:int, luku2:int):
    try:
        return float(luku1 / luku2)
    except ZeroDivisionError:
        print("Do not divide by 0")


def kerto(luku1:int, luku2:int):
    return float(luku1 * luku2)

if __name__ == '__main__':
    print(plus(3,3))
    print(miinus(3,3))
    print(jako(3,3))
    print(kerto(3,3))
    print(jako(3,0))
