i = 1
while i <= 15:
    if i == 1:
        for j in range(1, 16):
            if j == 1:
                print(" ", end=" ")
            if 2 <= j <= 14:
                print("#", end=" ")
            if j == 15:
                print(" ")
    if 2 <= i <= 3:
        for j in range(1, 16):
            print("#", end=" ")
        print("")
    if 4 <= i <= 5:
        for j in range(1, 4):
            print("#", end=" ")
        for j in range(4, 13):
            print(" ", end=" ")
        for j in range(13, 16):
            print("#", end=" ")
        print("")
    if 6 <= i <= 7:
        for j in range(1, 4):
            print("#", end=" ")
        print("")
    if i == 8:
        for j in range(1, 4):
            print("#", end=" ")
        for j in range(4, 8):
            print(" ", end=" ")
        for j in range(8, 15):
            print("#", end=" ")
        print("")
    if 9 <= i <= 10:
        for j in range(1, 4):
            print("#", end=" ")
        for j in range(4, 7):
            print(" ", end=" ")
        for j in range(7, 16):
            print("#", end=" ")
        print("")
    if i == 11:
        for j in range(1, 4):
            print("#", end=" ")
        for j in range(4, 8):
            print(" ", end=" ")
        for j in range(8, 16):
            if j in range(11, 13):
                print(" ", end=" ")
            else:
                print("#", end=" ")
        print("")
    if 12 <= i <= 13:
        for j in range(1, 4):
            print("#", end=" ")
        for j in range(4, 13):
            print(" ", end=" ")
        for j in range(13, 16):
            print("#", end=" ")
        print("")
    if 14 <= i <= 15:
        for j in range(1, 16):
            print("#", end=" ")
        print("")
    if i == 15:
        for j in range(1, 16):
            if j == 1:
                print(" ", end=" ")
            if 2 <= j <= 14:
                print("#", end=" ")
            if j == 15:
                print(" ")

    i = i + 1
