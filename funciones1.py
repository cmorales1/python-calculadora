#!usr/bin/env python
#-*- coding: utf-8 -*- 

#conding-----------
import os
import time
#operative system
#cls windows
#clear linux, MacOS
def menu():	
	a=True
	while a==True:
		os.system("cls")
		print "---------Calculadora-----------"
		print "------------Menu--------------"
		print "seleccione una de nuestras operaciones"
		print "1. suma"
		print "2. resta"
		print "3. multiplicacion"
		print "4. division"


	#si ingresa a la opcion invalida que regrese al menu y si esta bien que continue con el procedimiento
	
	
		Noopcion = raw_input("ingrese numero de opcion")
		if Noopcion == "1":
			os.system("cls")
			print "seleccionaste suma"
			a=False		
			suma()
		elif Noopcion == "2":
			os.system("cls")
			print "seleccionaste resta"
			a=False
			resta()
		elif Noopcion == "3":
			os.system("cls")
			print "seleccionaste multiplicacion"
			a=False
			multiplicacion()
		elif Noopcion == "4":
			os.system("cls")
			print "seleccionaste division"
			division()
		else:
			print "opcion invalida"
			time.sleep(2)

				

	


	
def suma():
	Dato1 = input("ingrese numero")
	Dato2 = input("ingrese numero")
	ab=Dato1+Dato2
	print "tu resultado es "+ str(ab)
	#dibujos ascii dar forma al menu
	#si quiere continuar sumando que siga sumando
	#si no que termine


def resta():
	Dato1 = input("ingrese numero")
	Dato2 = input("ingrese numero")
	ab=Dato1-Dato2
	print "tu resultado es "+ str(ab)
	
	
def multiplicacion():
	Dato1 = input("ingrese numero")
	Dato2 = input("ingrese numero")
	ab=Dato1*Dato2
	print "tu resultado es "+ str(ab)
def division():
	Dato1 = input("ingrese numero")
	Dato2 = input("ingrese numero")
	ab=Dato1/Dato2
	print "tu resultado es "+ str(ab)
		

# tarea ----------------ciclo while---------------------------	
	






menu()
