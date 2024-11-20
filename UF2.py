#Aqui trobaras exersisi de la UF2

#Exercici 1: Crear una Classe Persona

#Crea una classe anomenada Persona amb els atributs nom, edat i un mètode mostrar_info() que mostri el nom i l'edat de la persona.
#Exercici 2: Crear una Subclasse Cotxe

#Defineix una classe Cotxe que hereti de la classe Persona. La classe Cotxe ha de tenir els atributs marca i model i un mètode mostrar_info() que mostri tota la informació de la persona i del cotxe.

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

persona1 = Persona("Cento", 20)
def mostrar_info(self):
    return f"hola soc {self.nom} i tinc {self.edat}"

#Divendres 15: Exercicis de Funcions i Modularització (UF2)

#Exercici 3: Funció per Calcular la Mitjana

#Crea una funció que accepti una llista de números i retorni la seva mitjana. Fes que la funció validi que la llista no estigui buida.



#Exercici 4: Funció de Saluda

#Crea una funció anomenada saludar() que agafi un paràmetre nom i imprimeixi "Hola, {nom}!". Si no es passa el paràmetre, utilitza un valor per defecte.



#Exercici 5: Funció per Comptar Paraules

#Crea una funció anomenada comptar_paraules() que accepti una cadena de text i retorni el nombre de paraules.



#Dissabte 16: Exercicis de Pràctica UF2
#Exercici 13: Creació de la Classe Cotxe i Subclasse

#Crea una classe Cotxe amb atributs com marca, model, i un mètode per mostrar la informació. Crea una subclasse CotxeElèctric amb un mètode per mostrar si el cotxe està carregat o no.
#Exercici 14: Funció de Promig

#Crea una funció que accepti una llista de notes i retorni el promig, la nota màxima i la mínima.



#Dilluns 18: Exercicis de Disseny Descendent i Recursivitat (UF2)
#Exercici 6: Factorial Recursiu

#Implementa una funció recursiva que calculi el factorial d'un número donat. La funció ha de tenir una condició base per aturar la recursivitat.



#Exercici 7: Descomposició de Problema

#Crea un programa per calcular el cost d'una compra. Descompon el programa en dues funcions: una que calcule el subtotal (suma de preus) i una altra que calcule l'IVA (21% del subtotal).