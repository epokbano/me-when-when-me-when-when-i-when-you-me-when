

def nigger(jaja, abrakadabra):
    print("zmien to huju >:( ")
    inp = input()
    jaja[abrakadabra] = inp
    print(f"jajawartosc1: --- {jaja[abrakadabra]}")

def nigger2(lista, jajunia, jajunia2, jajunia3, kaboom, kaboom2, kaboom3, kaboom4, kaboom5, kaboom6):
    while True:
        print("---" * 25)
        print(" a = usun slownik")
        print(" b = usun wartosc ze slownika :D")
        print(" c = wyjdz z programu")
        burger = input()

        if burger.lower() == "c":
            break

        while burger.lower() not in ["a", "b"]:
            print("ZABIJ SIE (napisz jeszcze raz bo zla odpowiedz plz)\n")
            burger = input()

        if burger == "a":
            print("ktory slownik chcesz usunac uwu?\n")
            print("opcje: jaja, \n jaja2, \n jaja3")
            ksiazkadelete = input()
            while ksiazkadelete.lower() not in ["jaja", "jaja2", "jaja3"]:
                print("nie\n")
            if ksiazkadelete.lower() == "jaja":
                lista.pop(0)
                print(lista)
                break
            elif ksiazkadelete.lower() == "jaja2":
                lista.pop(1)
                print(lista)
                break
            else:
                ksiazkadelete.lower() == "jaja3"
                lista.pop(2)
                print(lista)
                break
        elif burger == "b":
            print("no to najpierw wybierz z jakiego slownika chcesz usuwac drogi panie \n")
            print("opcje: jaja, \n jaja2, \n jaja3")
            hamburger = input()
            while hamburger.lower() not in ["jaja", "jaja2", "jaja3"]:
                print("nie. \n")
            if hamburger.lower() == "jaja":
                print("teraz jaka wartosc chcesz usunac drogi panie \n")
                print("jaja:\n jajawartosc1,\n jajawartosc2")
                hamburger1 = input()
                while hamburger1 not in ["jajawartosc1", "jajawartosc2"]:
                    print("nie. \n")
                    if hamburger1 == "jajawartosc1":
                        jajunia[kaboom].delete
                        print(jajunia)
                        break
                    else:
                        hamburger1 == "jajawartosc2"
                        jajunia[kaboom2].delete
                        print(jajunia)
                        break 
                break
            elif hamburger.lower() == "jaja2":
                print("teraz jaka wartosc chcesz usunac drogi panie \n")
                print("jaja2:\n jaja2wartosc1,\n jaja2wartosc2")
                hamburger2 = input()
                while hamburger2 not in ["jaja2wartosc1", "jaja2wartosc2"]:
                    print("nie. \n")
                if hamburger2 == "jaja2wartosc1":
                        jajunia2[kaboom3].delete
                        print(jajunia2)
                        break
                else:
                    hamburger2 == "jaja2wartosc2"
                    jajunia2[kaboom4].delete
                    print(jajunia2)
                    break
            elif hamburger.lower() == "jaja3":
                print("teraz jaka wartosc chcesz usunac drogi panie \n")
                print("jaja3:\n jaja3wartosc1,\n jaja3wartosc2")
                hamburger3 = input()
                while hamburger3 not in ["jaja3wartosc1", "jaja3wartosc2"]:
                    print("nie. \n")
                    if hamburger3 == "jaja3wartosc1":
                        jajunia3[kaboom5].delete
                        print(jajunia3)
                        break
                    elif hamburger3 == "jaja3wartosc2":
                        jajunia3[kaboom6].delete
                        print(jajunia3)
                        break
                    else:
                        print("niepoprawna wartosc. \n")
                        hamburger3 = input()
                        break
