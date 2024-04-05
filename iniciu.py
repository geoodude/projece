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
    Afegir()
  elif opcio == 4:
    eliminar_llibre()
  elif opcio == 5:
    Editar()
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


    if llibre_eliminat:
        print(f'Llibre "{titol_llibre}" eliminat amb èxit.')
    else:
        print(f'Llibre "{titol_llibre}" no trobat.')


    with open(nom_fitxer, 'w') as fitxer:
        fitxer.writelines(llibres_modificats)





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

