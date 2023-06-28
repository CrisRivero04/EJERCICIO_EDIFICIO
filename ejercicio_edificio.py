import fun_rec_hotel as fn

while True:
    fn.mostrar_menu_h()
    opcion = fn.validar_menu_h()
    if opcion == 1:
        fn.ver_edificio()
    elif opcion == 2:
        fn.comprar()
    elif opcion == 3:
        fn.buscar_dueño()
    elif opcion == 4:
        fn.ganancias()
    else:
        break
    