# Exemple us de variables
#a = 12 
#print(f"hola el numerro es {a} ")

#[exercisi]

# Declara dues variables amb els teus números favorits i fes les 
# operacions bàsiques amb elles (suma, resta, multiplicació i divisió).

#a = 11
#b = 17

#suma = a + b
#resta = a - b
#multi = a * b 
#div = a / b 

#print(f"La suma es {suma}")
#print(f" La resta es {resta}")
#print(f"La multi es {multi}")
#print(f"La div es {div}")

#-----------------------------------------------------------
#Condicionals

#Exemple 1

#numero = 12 #Variable

#if numero % 2 == 0: #el % es fa servir per obtenir del residu del num div 2 si el 
# residu e 0 e num parell si no es senar

#    print(f"{numero} es parell")

#else:
#    print(f"{numero} es senar")

#[Exercisi Exemple 1 ]

#Exercici: Fes un programa que prengui un número de l’usuari i digui si és parell o senar.

#numero = int(input("Introdueix un numero "))

#if numero %2 == 0:
    #print(f"el num es parell")
#else:
    #print(f"el num es imparell")

#Exemple 2
#  en aquest exemple lo que podras observar sera el tema de comaprar 
# > mes gran que 
# < mes petit que
# >= mes gran o igual que
# <= mes petit o igual que
# == igual que 
# != diferent que

#edat = int(input("Introduiex una edat "))

#if edat >= 18:
#    print("ets major de edat")
#else:
#    print("Ets menor de edat")

#[Exercisi Exemple 2]

#Genera una codi que es porti amb 2 parts una que si ets major de 20 pots mirar pelis de adults
# pero si ets menro de 20 no 

#edat = int(input("Introdueix la teva edat "))

#if edat >= 20:
#    print (f"pots mirar les pelis ja que tens {edat} anys")
#else:
#    print(f"no ports mirar la peli ja que tens {edat} i nesesites 20 ")

#-----------------------------------------------------------

#Bucles 



#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------


#UF2

#Dijous 14 - Classes i Objectes

#    Classes
#        Una classe és una plantilla per crear objectes. Defineix els atributs (variables) i mètodes (funcions) que aquests objectes tindran.
#        Sintaxi: Es defineix amb la paraula clau class i comença amb una lletra majúscula per convenció.
#        Exemple:

#    class Persona:
 #       def __init__(self, nom, edat):
  #          self.nom = nom
   #         self.edat = edat

#Objectes

 #   Un objecte és una instància d'una classe que conté dades pròpies i accedeix als mètodes de la seva classe.
  #  Exemple:

   # persona1 = Persona("Maria", 25)

#Atributs i Mètodes

 #   Atributs: Són les propietats de la classe (com nom i edat).
  #  Mètodes: Són funcions dins de la classe (com saludar).
   # Exemple:

    #class Persona:
     #   def __init__(self, nom, edat):
      #      self.nom = nom
       #     self.edat = edat
        #
         #def saludar(self):
         #   return f"Hola, sóc {self.nom}"

#Encapsulació

 #   Els atributs privats es defineixen amb _ o __ al començament, indicant que no haurien de ser accedits fora de la classe.
  #  Exemple:

    #    class Persona:
     #       def __init__(self, nom, edat):
      #          self._edat = edat

#Divendres 15 - Subprogrames i Modularització

#    Funcions
 #       Una funció és un bloc de codi reutilitzable que realitza una tasca específica.
  #      Es defineix amb def, un nom, paràmetres (opcions d'entrada) i pot retornar un valor.
   #     Exemple:

    #def sumar(a, b):
#        return a + b

#Paràmetres i Paràmetres per Defecte

 #   Els paràmetres per defecte són opcions establertes si no es passa un valor.
  #  Exemple:

   # def saludar(nom="Convidat"):
    #    print(f"Hola, {nom}")

#*args i **kwargs

  #  *args: Permet passar una llista de paràmetres variables a una funció.
   # **kwargs: Permet passar arguments amb nom.
    #Exemple:

    #def sumar(*args):
     #   return sum(args)

#Modularització i Disseny Descendent

 #   Modularització: Dividir un problema gran en funcions més petites per facilitar el manteniment.
  #  Disseny Descendent: Descompondre una tasca en subfuncions.
   # Exemple:

    #    def calcular_mitjana(notes):
     #       return sum(notes) / len(notes)

#Dilluns 18 - Disseny Descendent i Recursivitat

 #   Disseny Descendent
  #      És la pràctica de dividir un problema gran en subprogrames més petits.
   #     Exemple:

    #def calcular_total_compra(preus):
     #   subtotal = sum(preus)
      #  return calcular_iva(subtotal)

    #def calcular_iva(subtotal):
     #   return subtotal * 0.21

#Recursivitat

 #   Una funció recursiva és aquella que es crida a si mateixa amb diferents paràmetres.
  #  Requereix una condició base per evitar bucles infinits.
   # Exemple:

    #    def factorial(n):
     #       if n == 1:
      #          return 1
       #     else:
        #        return n * factorial(n - 1)

#Dimarts 19 - Gestió de Fitxers (UF3)

 #   Obrir i Tancar Fitxers
  #      Els fitxers es poden obrir amb open() i tancar amb close().
   #     Modes comuns: 'r' (lectura), 'w' (escriptura), 'a' (afegir).
    #    Exemple:

    #fitxer = open("dades.txt", "r")
    #contingut = fitxer.read()
    #fitxer.close()

#Llegir i Escriure Fitxers

 #   Llegir: read(), readline() o readlines().
  ##  Escriure: write() per escriure al fitxer o writelines() per llistes.
    #Exemple d’escriptura:

    #fitxer = open("nou_fitxer.txt", "w")
    #fitxer.write("Hola món!")
    #fitxer.close()

#Gestió amb el Context Manager (with)

 #   El with tanca automàticament el fitxer.
  #  Exemple:

   #     with open("dades.txt", "r") as fitxer:
    #        contingut = fitxer.read()

#Dimecres 20 - Repàs Final UF2 i UF3

#Aquest dia pots repassar els conceptes principals:

 #   UF2: classes, objectes, mètodes, funcions, modularització, disseny descendent i recursivitat.
  #  UF3: obertura de fitxers, lectura, escriptura, modes i el with.

