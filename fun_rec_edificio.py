#FUNCIONES HOTEL
import time
import msvcrt

def mostrar_menu_h():
    print("""MENU OPCIONES DEL HOTEL:
    1. Ver edificio
    2. Comprar edificio
    3. Buscar dueño
    4. Total de ganancias
    5. Salir""")

def validar_menu_h():
    while True:
        try:
            opc_menu_h = int(input("Por favor ingrese una opcion del menu : "))
            if opc_menu_h in(1,2,3,4,5):
                return opc_menu_h
            else:
                print("ERROR! Opcion del menu no valida!")
        except:
            print("ERROR! Debe ingresar un numero entero")

#funciones del grafico del edificio
import numpy
edificio = numpy.zeros((10,4), int)
lista_ruts = []
lista_nombres = []
lista_filas = []
lista_columnas = []
#variables auxiliares de uso
lista_letras = ["A","B","C","D"]
lista_pisos = [10,9,8,7,6,5,4,3,2,1]

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut(Sin puntos ni digito verfificador) : "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT NO ES VALIDO")
        except:
            print("ERROR! DEBE INGRESAR UN NUMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre : ")
        if len(nombre.strip()) >= 2 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE ES INCORRECTO!")

def ver_edificio():
    print("        A B C D")
    for x in range(10):
        print("Piso",lista_pisos[x], end="\t")
        for y in range(4):
            print(edificio[x][y], end=" ")
        print()    

def validar_piso():
    while True:
        try:
            piso = int(input("Porfavor ingrese el piso de su departamento : "))
            if piso in lista_pisos:
                return piso
            else:
                print("ERROR! PISO NO VALIDO")
        except:
            print("ERROR! DEBE INGRESAR UN NUMERO ENTERO!")

def validar_departamento():
    while True:
        departamento = input("Ingrese departamento(A,B,C,D) : ")
        if departamento.upper() in lista_letras:
            return departamento
        else:
            print("ERROR! DEPARTAMENTO INCORRECTO")

def comprar():
    if 0 not in edificio:
        print("NO ESTA DISPONIBLE EL DEPARTAMENTO")
        time.sleep(3)
        return
    rut = validar_rut()
    nombre = validar_nombre()
    while True:
        ver_edificio()
        piso = validar_piso()
        departamento = validar_departamento()
        piso_comprar = lista_pisos.index(piso)
        dpto_comprar = lista_letras.index(departamento.upper())
        if edificio[piso_comprar][dpto_comprar] == 0:
            if piso_comprar in(0,1,2):
                valor = 200000000
            else:
                valor = 150000000
            dinero = int(input("Ingrese dinero : "))
            if dinero == valor:
                edificio[piso_comprar][dpto_comprar] = 1
                lista_ruts.append(rut)
                lista_nombres.append(nombre)
                lista_filas.append(piso_comprar)
                lista_columnas.append(dpto_comprar)
                print("DEPARTAMENTO COMPRADO CON EXITO!")
                break
            else:
                print("DINERO INSUFICIENTE!")
                return
        else:
            print("DEPARTAMENTO NO DISPONIBLE")

def ganancias():
    acum = 0
    for x in range(10):
        for y in range(4):
            if x in (0,1,2) and edificio[x][y] == 1:
                acum += 200000000
            elif edificio[x][y] == 1:
                acum += 150000000
    return

def buscar_dueño():
    rut = validar_rut()
    for x in range(len(lista_ruts)):
        if rut == lista_ruts[x]:
            print("Su nombre",lista_nombres[x])
            print(lista_filas[x])
            print(lista_columnas[x])
            
            print("Presione una tecla para continuar")
            msvcrt.getch()
            return
        else:
            print("Usted no cuenta con un departamento.")
            time.sleep(3)
            return
        