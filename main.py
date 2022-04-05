from queue import PriorityQueue
import random
import string
import time

#Przypisanie randomowego tekstu,
#przedstawiającego pliki do wysłania
#string = """Projekt Pamsi"""

#Dla testu czasu obliczania, generujemy
#znaki do, na których będziemy operowali
def ustaw_plik():
    global string,ilosc_czesci
    string = []
    ile = int(input("Z ilu znaków ma się składac ?  ? "))
    ilosc_czesci = int(input("Na ile części chcesz podzielić tekst? "))
    for i in range(0,ile):
        n = random.randint(1,9)
        string.append(n)

def podziel_wiadomosc_na_n_czesci(wiadomosc, liczba_czesci):
    dlugosc = len(wiadomosc)
    znaki = int(dlugosc/liczba_czesci)
    podzielona_wiadomosc = []
    if(dlugosc % liczba_czesci != 0):
            nowa_dlugosc = round(dlugosc)
            for i in range(0, nowa_dlugosc, znaki):
                part = string[i: i + znaki]
                podzielona_wiadomosc.append(part)
            podzielona_wiadomosc[-2] = podzielona_wiadomosc[-2] + podzielona_wiadomosc[-1]
            podzielona_wiadomosc.pop()
            return podzielona_wiadomosc
    else:
        for i in range(0, dlugosc, znaki):
            part = string[ i : i+znaki]
            podzielona_wiadomosc.append(part)
        print("Wiadomosc jest podzielona na rowne czesc")
        return podzielona_wiadomosc

def kolejka_priorytetowa(elementy_do_kolejki):
    q = PriorityQueue()
    for i in range(len(elementy_do_kolejki)):
        q.put((i, elementy_do_kolejki[i]))
    return q

def obsluga_kolejki(kolejka):
    lista_z_elementami_kolejki = []
    while not kolejka.empty():
        next_item = kolejka.get()
        lista_z_elementami_kolejki.append(next_item)
    return lista_z_elementami_kolejki

def uporzadkuj_liste_z_wiadomosciami(lista_z_wiadomosciami):
    lista_indeksow = []
    lista_wartosci = []
    for i in lista_z_wiadomosciami:
        lista_indeksow.append(i[0])
        lista_wartosci.append(i[1])
    uporzadkowana = sorted(lista_indeksow)
    prawidlowa_lista = []
    for i in (uporzadkowana):
        index = lista_indeksow.index(i)
        prawidlowa_lista.append(lista_wartosci[index])
    return(prawidlowa_lista)

def wykonaj():
    ustaw_plik()
    start = time.perf_counter()

    tablica_wiadomosci = podziel_wiadomosc_na_n_czesci(string, ilosc_czesci)
    q = kolejka_priorytetowa(tablica_wiadomosci)
    lista = obsluga_kolejki(q)
    print("Przesłana wiadomosc - kolejka priorytetowa: \n {}".format(lista))
    random.shuffle(lista)
    print("Pomieszana lista:\n {}".format(lista))
    docelowa_lista = uporzadkuj_liste_z_wiadomosciami(lista)
    print("Poskladana wiadomosc:")
    print(docelowa_lista)

    print(time.perf_counter() - start)

if __name__ == '__main__':

    wykonaj()




