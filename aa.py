def llegir_llibres():
    try:
        with open('Llibres.txt', "r") as fitxer:
            contingut = fitxer.readlines()
    except FileNotFoundError:
        print("El fitxer 'Llibres.txt' no existeix.")
    return contingut


def mostrar_llibre():
    titol_buscar = input("Introdueixi el títol del llibre: ")
    llibres = llegir_llibres()
    for linia in llibres:
        titol, autor, any_de_publicacio, genere, isbn = linia.split("|")
        if titol == titol_buscar:
            print("\nInformació del llibre:")
            print("Títol: ", titol)
            print("Autor/a: ", autor)    
            print("Any de publicació: ", any_de_publicacio)
            print("Gènere: ", genere)
            print("ISBN:", isbn)
            return
    print("El llibre no s'ha trobat.")


def mostrar_tots_llibres():
    llibres = llegir_llibres()
    numero = 0
    
    for linia in llibres:
        if numero == 0:
            None
        elif numero >= 1:
            titol, autor, any_de_publicacio, genere, isbn = linia.strip().split("|")
            print("=======================================")
            print("Informació del llibre", numero, ":")
            print("Títol: ", titol)
            print("Autor/a: ", autor)    
            print("Any de publicació: ", any_de_publicacio)
            print("Gènere: ", genere)
            print("ISBN:", isbn)
            print("=======================================")
        numero = numero+1


def afegir_llibre():
    titol_afegir = input("Inserta el titol del llibre que vols afegir: \n")
    llibres = llegir_llibres()
    for linia in llibres:
        titol, autor, any_de_publicacio, genere, isbn = linia.split("|")
        if titol_afegir == titol:
            print("\nEl titol de llibre que vols afegir ja existeix.")
            return
    autor_afegir = input("Inserta autor del llibre ")
    any_de_publicacio_afegir = input("Inserta any de publicació del llibre")
    genere_afegir = input("Inserta genere del llibre")
    isbn_afegir = input("Inserta any de publicació del llibre")
    try:
        with open('Llibres.txt', "a") as fitxer:
            fitxer.write("\n" + titol_afegir + "|" +)
    except FileNotFoundError:
        print("El fitxer 'Llibres.txt' no existeix.")
    



