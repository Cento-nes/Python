#Aqui pordras observar exercisis de variables 

#Exercici 1: Declara dues variables amb els teus números favorits i fes 
# la suma, resta, multiplicació i divisió. Imprimeix els resultats de 
# cadascuna d'aquestes operacions.

# a = 17
# b = 11

# suma = a + b 
# resta = a - b 
# multi = a * b 
# div = a / b 

# print(f"la suma es {suma}")
# print(f"la resta es {resta}")
# print(f"la multi es {multi}")
# print(f"la div es {div}")


#Exercici 2: Declara una variable amb el valor de l'edat d'una persona. 
# Després, declara una segona variable amb el nombre d'anys fins a la 
# seva jubilació (per exemple, 65 - edat) i imprimeix-la.

#edat = int(input("Introdueix la teva edat: "))

#edat_jub = 65 - edat

#print(f"Queden {edat_jub} anys fins poder jubilarte.")

#Exercici 3: Declara una variable amb la quantitat de productes i una 
# altra amb el preu per producte. Calcula el total a pagar multiplicant
#  aquests dos valors i imprimeix el resultat.

#quantitat = int(input("Posa un numero de productes: "))

#preu_productes = int(input("intorudiex el preu del procu "))

#resultat = quantitat * preu_productes 

#print(f"El preu es: {resultat}")

#Exercici 4: Declara una variable amb el preu d’un objecte i una altra
#  amb el percentatge d’impost (per exemple, 21%). Calcula el preu 
# final aplicant aquest impost i imprimeix el resultat.

#Preu = int(input("introdueix el preu del objectre: "))

#impost = 21 / 100

#resultat = Preu + (Preu * impost)

#print(f"el preu final seria el seguent: {resultat}")


#Intercanvi de Valors:

 #   Declara dues variables x i y amb els valors 10 i 20, respectivament.
  #  Intercanvia els valors de x i y sense utilitzar una tercera variable.
   # Mostra els nous valors de x i y.

#Àrea d'un Rectangle:

 #   Declara dues variables base i altura amb valors numèrics.
  #  Calcula l'àrea del rectangle (base * altura) i emmagatzema el resultat en una variable area.
   # Mostra el valor d'area.

#Conversió de Temperatura:

 #   Declara una variable celsius amb un valor que representi la temperatura en graus Celsius.
  #  Converteix aquesta temperatura a graus Fahrenheit i guarda el resultat en una variable fahrenheit. La fórmula és: fahrenheit = celsius * 9/5 + 32.
   # Mostra el valor de fahrenheit.

#Calculadora de Preu Total amb IVA:

 #   Declara una variable preu amb un valor numèric que representi el preu d'un producte.
  #  Declara una altra variable iva amb un percentatge d'IVA (per exemple, 21).
   # Calcula el preu total amb IVA i guarda'l en una variable preu_total.
    #Mostra el valor de preu_total.

#Suma i Promig de Tres Números:

 #   Declara tres variables a, b, i c amb diferents valors numèrics.
  #  Calcula la suma i el promig d'aquests tres números i guarda els resultats en variables suma i promig.
   # Mostra els valors de suma i promig.


#Conversió de tipus: Crea una variable x de tipus float amb el valor 5.7. Converteix x sencer i mostra el valor resultant.



#Càlcul d'àrees: Demana a l'usuari la base i l'alçada d'un triangle i calcula la seva àrea.



#Concatenació de cadenes: Crea dues variables, nom i cognom. Mostra en pantalla el nom complet concatenant les dues variables.



#Intercanvi de variables: Crea dues variables a i b amb valors inicials, i intercanvia els valors sense utilitzar una variable auxiliar.



#Operacions Matemàtiques: Donat un nombre enter n, mostra el quadrat, el cub i l'arrel quadrada de n.





#-------------------------------------------------------------------------------------------------------------
#Aqui pordras observar exercisis de condicionals 



#Exercici 1: Escriu un programa que demani un número i imprimeixi si 
# és positiu, negatiu o zero.

#numero = int(input("Posa un numero: "))

#if numero > 0:
#    print("el num e posiitiu")
#elif numero <= 0:
#    print("el num es negatiu")
#else:
#    print ("el nuemro es 0")

#Exercici 2: Escriu un programa que demani l'edat d'una persona i 
#imprimeixi si és menor d'edat (menor de 18) o major d'edat.

#edat = int(input("introdueix la teva edat: "))

#if edat >= 18:
#    print("Es major de edat")
#else:
#    print("es menor de edat")

#Exercici 3: Escriu un programa que demani una temperatura i 
# imprimeixi si és alta (per sobre de 30 graus), moderada 
# (entre 15 i 30 graus) o baixa (per sota de 15 graus).


#temp = float(input("Introdueix la temperatura: "))


#if temp > 30:
#    print("La temperatura es alta.")
#elif temp >= 15:
#    print("La temperatura es moderada.")
#else:
#    print("La temperatura es baixa.")

#Exercici 4: Escriu un programa que demani a l'usuari una quantitat 
# d'hores i calculi el cost total a pagar si la tarifa és de 10 
# euros per hora. Si la quantitat d'hores és superior a 40, aplica 
# una tarifa de 15 euros per hora per les hores extres.

#h = int(input("Introdueix el nombre d'hores: "))

#if h > 40:
#    total = (40 * 10) + ((h - 40) * 15)
#else:
#    total = hores * 10

#print(f"El cost total a pagar és: {total} euros")


#Verificar Nombre Parell o Senar:

 #   Demana a l'usuari que introdueixi un número.
  #  Si el número és parell, mostra el missatge: "El número és parell".
   # Si és senar, mostra el missatge: "El número és senar".


#x = int(input("Introduiex un numero del 1 al 10: "))

#if x in [2,4,6,8,10]:
 #  print(f"el numero {x} es parell")
#else:
 # print(f"El numero {x} es senar")



#Determinar el Major de Tres Números:

 #   Demana a l'usuari que introdueixi tres números.
  #  Mostra quin és el major dels tres números.


#x = int(input("introdueix un numero: "))
#y = int(input("introdueix un altre numero: "))
#z = int(input("introdueix un altre numero: "))

#major = max (x, y, z)
#print (f"El numero mes gran es {major}")


#Classificació d'Edat:

 #   Demana a l'usuari que introdueixi la seva edat.
  #  Si té menys de 12 anys, mostra el missatge "Ets un nen".
   # Si té entre 12 i 17 anys, mostra "Ets un adolescent".
    #Si té 18 anys o més, mostra "Ets un adult".


#edat = int(input("Introdueix la teva edat: "))

#if edat < 12:
 #   print(f"Tens {edat} ets un nen")
#elif 12 <= edat <= 17:
 #   print(f"Tens {edat} ets un adolescent")
#else:
 #   print(f"Ets un adult amb la edat de {edat} anys")


#Assignació de Notes:

 #   Demana a l'usuari que introdueixi la seva nota (0 a 100).
  #  Mostra la qualificació segons el rang:
   #     90-100: "Excel·lent"
    #    70-89: "Notable"
     #   50-69: "Aprovat"
      #  Menys de 50: "Suspès"

#nota = int(input("introdueix la teva nota(0-100): "))

#if 90 <= nota <= 100:
#    print("Excel·lent")
#elif 70 <= nota <= 89:
#   print("Notable")
#elif 50 <= nota <= 69:
#   print("Aprovat")
#else:
#    print("suspes")


#Calculadora Senzilla:

 #   Demana a l'usuari que introdueixi dos números i un operador (+, -, *, /).
  #  Realitza l'operació indicada per l'usuari i mostra el resultat.
   # Si l'usuari introdueix un operador no vàlid, mostra un missatge d'error.


#Número Parell o Senar: Demana a l'usuari un nombre enter i determina si és parell o imparell.



#Major de Tres Números: Demana tres números i mostra quin és el més gran.



#Classificació d'Edat: Demana a l'usuari la seva edat i mostra un missatge segons el rang (nen, adolescent, adult, gran).



#Any Bisiesto: Demana a l'usuari un any i determina si és de traspàs.



#Notes Acadèmiques: Demana una qualificació i mostra "Aprovat" si és major o igual a 5, i "Reprovat" si és menor.



#-------------------------------------------------------------------------------------------
#Aqui trobaras exersisis de Bucles

#Sumatòria de Números: Sol·licita un número n i calcula la suma de tots els números des d'1 fins a n.

#n = int(input("introdueix un num: "))

#suma = sum(range(1,n+1))
#print("La suma es:", suma)

#Taula de multiplicar: Demana un número i mostra la seva taula de multiplicar fins al 10.

#m = int(input("introdueix un num: "))
#for i in range (1,11):
 #   print(f"{m} x {i} = {m * i}")

#Suma de Parells: Demana un número n i calcula la suma de tots els números parells fins a n.

n = int(input("posa un numero: "))
suma = sum(i for i in range(2, n+1, 2))
print("La suma de parells es:", suma)


#Endevina el número: Crea un programa que generi un nombre aleatori i permeti a l'usuari endevinar-lo.



#Compte Regressiu: Demana un número i mostra un compte regressiu fins a 0.


