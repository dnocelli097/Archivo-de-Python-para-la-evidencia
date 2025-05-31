
def MENU_PRINCIPAL ():
 print("\n--- MENÚ PRINCIPAL ---")    
print("***Bienvenidos al Centro de monitoreo de Agro Tech Coop***")
print("MENU PRINCIPAL")
print("+-+-+-+-+-+-+-+-+")
print("1. CAMPO")
print("2. PARCELA")
print("3. SENSOR")
print("4. SALIR")
opcion=input("Seleccione una opcion: ")

def sub_menu_campo ():
    print("\n--- SUB MENÚ CAMPO ---")
print("---Usted se encuentra en el submenú CAMPO----")    
print("1. Ver Campo")
print("2. Agregar Nuevo Campo")
print("3. Eliminar Campo")
print("4. Volver al Menú principal")
opcion=input("Selecciones una opcion: ")


def sub_menu_sensor ():
    print("\n--- SUB MENÚ SENSORES ---")
print("---Usted se encuentra en el submenú SENSORES----")    
print("1. Ver Sensor")
print("2. Agregar Nuevo Sensor")
print("3. Eliminar Sensor")
print("4. Volver al Menú principal")
opcion=input("Selecciones una opcion: ")


while opcion !=0 :
    
    def MENU_PRINCIPAL ():
     print("\n--- MENÚ PRINCIPAL ---")    
    print("***Bienvenidos al Centro de monitoreo de Agro Tech Coop***")
    print("MENU PRINCIPAL")
    print("+-+-+-+-+-+-+-+-+")
    print("1. CAMPO")
    print("2. PARCELA")
    print("3. SENSOR")
    print("4. SALIR")
    opcion=input("Seleccione una opcion: ")
    
    while opcion  != 0:
       if opcion=="1":
        def SUBMENU_CAMPO ():
         print("\n--- SUBMENU CAMPO ---")
        
        print("SUBMENU CAMPO.")
        print("+-+-+-+")
        print("1. Ver campo")
        print("2. Agregar campo")
        print("3. Eliminar campo")
        print("4. Volver al menu principal")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1": 
               
                print("1. Numero de campo")
                numcamp=input("ingrese el numero de campo:")
                print("1. Siguiente")
                print("2. volver al submenu campo")
                opcion=input("Selecciones una opcion: ")
                if opcion=="1":
                        print("Se verá el campo con todos los datos")
                elif opcion=="2":
                     print("Se vuelve al menú campo")    
                else:
                       print("opción invalida")
        elif opcion=="2":
            print("Agregar campo")
            numcamp=int(input("ingrese un nuevo numero de campo"))
            print("1. Registrar campo")
            print("2. volver al menu CAMPO")
            opcion=input("Seleccione una opcion: ")
            if opcion=="1":
                print("campo registrado con exito")
            elif opcion=="2":
                print("vuelve al menu CAMPO")
            else:
                print("opcion invalida")        
        elif opcion=="3":
            numcampo=int(input("ingrese el numero de campo que quiere eliminar"))    
        elif opcion=="4":
            print("MENU PRINCIPAL")
            print("+-+-+-+-+-+-+-+-+")
            print("1. CAMPO")
            print("2. PARCELA")
            print("3. SENSOR")
            print("4. SALIR")
            opcion=input("Seleccione una opcion: ")
    
        
    
        elif opcion=="2":
            def SUBMENU_PARCELA ():
                print("\n--- SUBMENU PARCELA ---")
                print("PARCELA.")
                print("+-+-+-+")
                print("1. Ver parcela")
                print("2. Agregar parcela")
                print("3. Eliminar parcela")
                print("4. Volver al menu principal")
        ocion=input("Seleccione una opcion: ")
        if opcion=="1":
            print("1. Ver parcela")
            numparc=int(input("ingrese el numero de parcela que desa ver:"))
        elif opcion=="2":
            print("Agregar parcela")
            numparc=int(input("ingrese un nuevo numero de parcela: "))
        elif opcion=="3":
            numparc=int(input("ingrese el numero de parcela que quiere eliminar"))    
        elif opcion=="4":
            print("MENU PRINCIPAL")
            print("+-+-+-+-+-+-+-+-+")
            print("1. CAMPO")
            print("2. PARCELA")
            print("3. SENSOR")
            print("4. SALIR")
            opcion=input("Seleccione una opcion: ")
        
        elif opcion=="3":
         print("SENSOR.")
        print("+-+-+-+")
        print("1. Ver sensor")
        print("2. Agregar sensor")
        print("3. Eliminar sensor")
        print("4. Volver al menu principal")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            print("1. Ver sensor")
            numcamp=int(input("ingrese el sensor que desa ver:"))
        elif opcion=="2":
            print("Agregar sensor")
            numcamp=int(input("ingrese un nuevo numero de sensor: "))
        elif opcion=="3":
            numcampo=int(input("ingrese el numero de sensor que quiere eliminar: "))    
        elif opcion=="4":
            print("MENU PRINCIPAL")
            print("+-+-+-+-+-+-+-+-+")
            print("1. CAMPO")
            print("2. PARCELA")
            print("3. SENSOR")
            print("4. SALIR")
            opcion=input("Seleccione una opcion: ")
        
        
        break
       elif opcion=="4":
        print("SALIR")
        break
     
    print("opcion invalida")

                           