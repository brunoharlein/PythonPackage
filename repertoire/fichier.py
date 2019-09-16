def table(nb, max=10):
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

def loops():
    while 1:
        lettre = input("lettre q pour sortir de la boucle")
        if lettre == "q":
            print("Vous sortez")
            break
        print("mauvaise lettre")