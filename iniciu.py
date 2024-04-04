import hashlib
usuaris= "Usuaris.txt"

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
    if opcio == 1:
      Mostrar()
    elif opcio == 2:
      Mostrartots()
    elif opcio == 3:
      Afegir()
    elif opcio == 4:
      Eliminar()
    elif opcio == 5:
      Editar()
def Eliminar():
    eliminar = input("quin llibre vols eliminar")
    
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

