from random import randrange


def un_tirage(B, R):
    u = ["B"] * 3 + ["R"] * 4
    b1 = u.pop(randrange(len(u)))
    b2 = u.pop(randrange(len(u)))
    if "R" in b1 and "B" in b2:
        return True
        print("1")
    else:
        return False
        print("2")
