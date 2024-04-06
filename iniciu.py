import hashlib
usuaris= "Usuaris.txt"
def llegir_llibres():
    try:
        with open('Llibres.txt', "r") as fitxer:
            contingut = fitxer.readlines()
    except FileNotFoundError:
        print("El fitxer 'Llibres.txt' no existeix.")
    return contingut

def inicisesio( usuari, contra):
    users = {}
    usuaris= "Usuaris.txt"
    with open(usuaris, 'r') as archivo:
        
        print(f"{contra}")
        for linea in archivo:
            usuari1, contrasenya = linea.strip().split('|')
            
            users[usuari] = contrasenya
            if usuari1 == usuari and users[usuari] == contra:
                flag = True
        return flag
def tria():
  try:
    opcio = int(input("Diges una opcio \n ================\n1. Mostrar un Llibre\n2.Mostrar tots els llibres\n3.Afegir un llibre\n4.Eliminar un llibre\n5.Edita un llibre"))
  except ValueError as value:
    print("ha donat un error",value)

  if opcio == 1:
    mostrar_llibre()
  elif opcio == 2:
    mostrar_tots_llibres()
  elif opcio == 3:
    afegir_llibre()
  elif opcio == 4:
    eliminar_llibre()
  elif opcio == 5:
    Editar()
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
    isbn_afegir = input("Inserta isbn del llibre")
    try:
        with open('Llibres.txt', "a") as fitxer:
            
            fitxer.write("\n" + titol_afegir + "|" + autor_afegir + "|" + any_de_publicacio_afegir + "|" + genere_afegir + "|" + isbn_afegir)
    except FileNotFoundError:
        print("El fitxer 'Llibres.txt' no existeix.")
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
def eliminar_llibre(nom_fitxer, titol_llibre):
    fitxer = 'Llibres.txt'
    
    titol_a_eliminar = input("quin llibre vols eliminar")
    with open(nom_fitxer, 'r') as fitxer:
        llibres = fitxer.readlines()

    llibres_modificats = []
    llibre_eliminat = False

    for linia in llibres:
        if titol_llibre not in linia:
            llibres_modificats.append(linia)
        else:
            llibre_eliminat = True


    with open(nom_fitxer, 'w') as fitxer:
        fitxer.writelines(llibres_modificats)
def editar_llibre(archivo, camp_editar, valor_antiga, valor_nova):
    with open(archivo, 'r') as f:
        linees = f.readlines()

    with open(archivo, 'w') as f:
        for linia in linees:
            parts = linia.split('|')
            if parts[camp_editar].strip() == valor_antiga:
                parts[camp_editar] = valor_nova
                nova_linia = '|'.join(parts)
                f.write(nova_linia)
            else:
                f.write(linia)

def Editar():
    arxiu = 'llibres.txt'  
    camp_editar = int(input("que vols editar\n 0 Titol\n1 Autor\n Any de publicacio\n3 Gènere\n4 ISBN"))  
    valor_antiga = input("que posava anterior ment")  
    valor_nova = input("que vols que posi en el camp que has selecionat")  

    editar_llibre(arxiu, camp_editar, valor_antiga, valor_nova)



intents = 1
users = {}

while intents<=3:
    try:
        usuari = input("Diges el nom del teu usuari\n")
    except ValueError as value:
        print("nom d'usuari no valid")
    try:
        contra = input("Diges la teva contrasenya \n")
        contra = hashlib.md5(contra.encode()).hexdigest()
        
    except ValueError:
        print("contrasenya no valida")
    esUsuariCorrecte = inicisesio(usuari, contra)
    
    if esUsuariCorrecte:
        tria()

    intents = intents+1 
    if intents == 4:
        print("has fallat mases cops")

