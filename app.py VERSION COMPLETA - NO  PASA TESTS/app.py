# Lista para almacenar los productos
import os


productos = []

# Inicio declaracion de variables globales
# UMBRAL_STOCK = 10 #Opción de umbral para control de mínimos de stock disponible en próxima version


# Fin declaracion de variables globales

################################################## Inicio sección declaracion de funciones #################################################


##### Funciones auxiliares carga de Productos en el Inventario #####
def solicitarCodigoProducto(contador):
    codigoSinValidar = input(
        f"\nPor favor, ingresá el código del {contador+1}° producto (0 para finalizar): "
    )
    # Valido el ingreso con isdigit() por simplicidad, aunque bien podría haberlo manejado con exceptiones (try/except)
    if codigoSinValidar.isdigit():
        # Código ingresado es un entero mayor o igual a 0(condición de salida)
        codigo_validado = int(codigoSinValidar)
        if codigo_validado < 0:
            # Sí el código es un entero menor a 0 entrego codigo_validado con el flag de inválido
            codigo_validado = -1  # -1 es el flag de código inválido
    else:
        # print("El código ingresado es inválido, deben ser enteros mayores a 0")
        # Uso el -1 como valor de código inválido para informarlo a la función que invoca a solicitarCodigoProducto()
        codigo_validado = -1  # -1 es el flag de código inválido
    return codigo_validado


def solicitarNombreProducto():
    nombre = ""
    while nombre == "":
        nombre = input("Ingresá el nombre: ")
        if nombre == "":
            print("\nEl nombre del producto no puede quedar vacío.\n")
    return nombre


# defino funciones para validar si una cadena es un float en el formato válido para python
def is_float(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False


def is_float_v2(cadena):
    if cadena.replace(".", "").isnumeric():
        return True
    else:
        return False


def solicitarPrecioUnitarioProducto():
    precio = 0.0
    validacion = False

    while validacion == False:
        precioStr = input("Ingresá el precio unitario en formato 0.0: ")

        validacion = is_float(precioStr)

        if validacion:
            precio = float(precioStr)
            if precio <= 0.0:
                print("\nEl precio del producto debe ser mayor a 0.0\n")
                validacion = False
        else:
            print(
                "\nEl precio ingresado tiene un formato erróneo. Debe ser mayor a 0.0\n"
            )

    return precio


def solicitarCantidadProducto():
    cantidad = 0  # Si solicito cantidad de productos, no puedo agregar un producto nuevo (inventariarlo) sin stock, es decir algo con cant = 0 no es valido.
    while cantidad <= 0:
        cantidadSinValidar = input("Ingresá la cantidad de unidades: ")
        # Valido el ingreso con isdigit() por simplicidad, aunque bien podría haberlo manejado con exceptiones (try/except)
        if cantidadSinValidar.isdigit():
            # Cantidad ingresada es un entero mayor o igual a 0(condición de salida)
            cantidad = int(cantidadSinValidar)
            if (
                cantidad <= 0
            ):  # Sí la cantidad ingresada es un entero menor o igual a 0 lo pongo en 0 para que vuelva a interar y lo informo.
                print("La cantidad ingresada debe ser un número entero mayor a 0.")
                cantidad = 0
            else:
                break
        else:
            print("La cantidad ingresada es incorrecta, debe ser un número mayor a 0.")
            # Uso el -1 como valor de código inválido y vuelve a iterar el while.  Informo el error también.
            cantidad = -1  # -1 es el flag de código inválido
    return cantidad


def buscarProductoPorCodigo(codigoIngresado):
    posicion = 0
    cantidadPoductos = len(productos)
    # Inicializo el array de 2 posiciones para la respuesta de la búsqueda por código. En la posición 0 de respuesta guardo el resultado lógico de la búsqueda.
    # En la posición 1 de respuesta guardo el valor de la posición (índice) en el array de productos, que coincide con codigoIngresado (será -1 en caso de no existir).
    respuesta = [False, -1]
    while posicion < cantidadPoductos:
        if productos[posicion][0] == codigoIngresado:
            respuesta = [True, posicion]
            # print(
            #     f'El código de producto "{codigoIngresado}" ya fue ingresado previamente al inventario.'
            # )
        ### este else es redundante porque respuesta fue inicializado en False, sólo se agregó para debugging.
        # else:
        #     print(
        #         f'El código de producto "{codigoIngresado}" NO está registrado en el inventario.'
        #     )
        posicion += 1
    return respuesta


def buscarProductoPorNombre(nombreIngresado):
    posicion = 0
    cantidadPoductos = len(productos)
    # Inicializo el array de 2 posiciones para la respuesta de la búsqueda por nombre. En la posición 0 de respuesta guardo el resultado lógico de la búsqueda.
    # En la posición 1 de respuesta guardo el valor de la posición (índice) en el array de productos, que coincide con nombreIngresado (será -1 en caso de no existir).
    respuesta = [False, -1]
    while posicion < cantidadPoductos:
        if productos[posicion][1] == nombreIngresado:
            respuesta = [True, posicion]
            # print(
            #     f'El nombre de producto "{nombreIngresado}" ya fue ingresado previamente al inventario.'
            # )
        ### este else es redundante porque respuesta fue inicializado en False, sólo se agregó para debugging.
        # else:
        #     print(
        #         f'El nombre de producto "{nombreIngresado}" NO está registrado en el inventario.'
        #     )
        posicion += 1
    return respuesta


def ingresarProductoPorCodigoAlInventario(codigoIngresado):
    resultado = False
    respuestaBusquedaCodigo = buscarProductoPorCodigo(
        codigoIngresado
    )  # array de dos posiciones: en la pos 0 está valor logico del match en el Inventario y en la pos 1 el índice del match.
    respuestaBusquedaNombre = (
        False  # Resultado lógico de la existencia del nombreProducto en el Inventario.
    )

    if respuestaBusquedaCodigo[0] == False or respuestaBusquedaCodigo[1] == -1:
        print(f'Cargando el producto código "{codigoIngresado}" en el inventario.')
        nombre_producto = solicitarNombreProducto()
        respuestaBusquedaNombre = buscarProductoPorNombre(nombre_producto)
        if respuestaBusquedaNombre[0] == False or respuestaBusquedaNombre[1] == -1:
            precio_unitario = solicitarPrecioUnitarioProducto()
            cantidad = solicitarCantidadProducto()
            # Agregamos los datos del producto como una lista dentro de la lista de productos
            productos.append(
                [codigoIngresado, nombre_producto, precio_unitario, cantidad]
            )
            # print(
            #     f'\nEl producto "{codigoIngresado}" se ingresó al inventario exitosamente.\n'
            # )
            resultado = True
        else:
            print(
                f'El producto "{nombre_producto}" ya existe en el inventario.\nDeberá seleccionar la opción "Modificar Producto" del Menú Principal para editar el registro preexistente.'
            )
            resultado = False
    else:
        print(
            f'El producto "{codigoIngresado}" ya existe en el inventario.\nDeberá seleccionar la opción "Modificar Producto" del Menú Principal para editar el registro preexistente.'
        )
        resultado = False

    return resultado


##### Fin Funciones auxiliares carga de Productos en el Inventario #####


def cargarProductosAlInventario():
    productos_en_inventario = 0
    os.system(
        # "clear"  #Para otros entornos
        "cls"  # Para entorno windows
    )  # Limpio la pantalla antes de iniciar el módulo de carga de productos.
    try:
        # Solicitamos el primer código de producto
        print(f"\nAlta de productos en el inventario:\n\n\n")
        codigo_producto = solicitarCodigoProducto(productos_en_inventario)
        # Usamos el bucle while para ingresar los datos mientras el código no sea 0
        while codigo_producto != 0:
            if codigo_producto != -1:
                if ingresarProductoPorCodigoAlInventario(codigo_producto):
                    productos_en_inventario += 1  # incremento el contador en caso que el producto sea nuevo y con los datos validados.
                else:  # este else es redundante porque la función "ingresarProductoPorCodigoAlInventario" ya informa internamente el resultado de la operación.
                    print(
                        f'La carga de datos sobre el producto "{codigo_producto}" no fue realizada.'
                    )
            else:
                print(
                    "El código ingresado es inválido, debe ser un número entero mayor a 0.\n"
                )
            # Solicitamos nuevamente el código del siguiente producto
            codigo_producto = solicitarCodigoProducto(productos_en_inventario)
    except ValueError:
        print(
            "\nError en la carga de datos al inventario. Salida abrupta del módulo de carga.\n\n\n"
        )


##### Funciones para Listar los Productos cargados en el Inventario #####
def mostrarProductosDelInventario():
    os.system(
        # "clear"  #Para otros entornos
        "cls"  # Para entorno windows
    )  # Limpio la pantalla antes de mostrar los resultados

    # Mostramos la lista final de productos del inventario
    print("\nListado de Productos del Inventario")

    print("-" * 150, "\n")

    if len(productos) == 0:
        print("\n")
        print(
            'El inventario está vacío.\nSi desea iniciar la carga productos deberá seleccionar "1. Agregar productos" en el Menú Principal.\n'
        )
    else:
        for producto in productos:
            print(
                "Código: ",
                producto[0],
                "\t\t",
                f"Nombre: '{producto[1]}'",
                "\t\t",
                "Precio(xU.): ",
                producto[2],
                "\t\t",
                "Cantidad: ",
                producto[3],
            )
    print("\n")
    print("-" * 150, "\n")
    input("Presione cualquier tecla para continuar...")


##### Funciones para el manejo del Menú Gestión del Inventario #####
def mostrarOpcionesMenu():
    print("\n--- Menú Principal de Inventario ---")
    ###### Muestro en el menú las opciones habilitadas para la Pre-entrega
    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Salir")
    ###### las siguientes opciones formarán parte del menú de la versión final según README.md ######
    # print("1. Alta de productos nuevos")
    # print("2. Consulta de datos de productos")
    # print("3. Modificar la cantidad en stock de un producto")
    # print("4. Dar de baja productos")
    # print("5. Listado completo de los productos")
    # print("6. Lista de productos con cantidad bajo mínimo")
    # print("7. Salir")


def ingresarOpcionValida(opcionStr, opcionSalida):
    opcion = 0
    if opcionStr.isdigit():
        # si el caracter ingresado es numérico entonces valida que sea un valor dentro de las opciones disponibles, sino itera hasta conseguir un número dentro del rango de las opciones del Menú.
        opcion = int(opcionStr)
        while opcion < 1 or opcion > int(
            opcionSalida
        ):  # valida que se ingrese una opción válida
            print("error, ingrese opción válida")
            opcionStr = input(f"(1-{opcionSalida}) >\t")
            if opcionStr.isdigit():
                opcion = int(opcionStr)
    else:
        opcion = (
            -1
        )  # valor de opción inválida en caso que el caracter ingresado no sea numérico.
    return opcion


def procesarOpcionElegida(opcion, opcionSalida):
    # Proceso: Elección de opcion y ejecución de las sentencias aoci
    if opcion == 1:
        cargarProductosAlInventario()  # ENTRADA
    elif opcion == 2:  # sino si
        mostrarProductosDelInventario()  # SALIDA
    elif opcion == int(opcionSalida):
        print(f"Elegiste salir del programa de inventario.")
    else:
        print(f"Opción no válida - Ingrese un número del 1 al {opcionSalida}")


######################################################### Fin seccion de funciones #########################################################


# Función principal para el sistema de inventario (NO ELIMINAR)
def main():
    # AQUÍ PUEDES COMENZAR A DESARROLLAR LA SOLUCIÓN

    opcionSalida = "3"  # variable que setea el número de opción "Salir" en el "Menú Principal de Inventario". Se debe setear como String obligatoriamente.
    opcionStr = ""  # variable que guarda la opción elegida como un String.
    opcion = 0  # Variable que guarda la opción elegida como un Integer.

    # PROCESO
    # INICIO DEL LOOP DEL PROGRAMA PRINCIPAL
    while opcionStr != opcionSalida:
        # os.system("clear")  # en windows comentar esta linea
        os.system("cls")  # en windows DESCOMENTAR esta linea
        mostrarOpcionesMenu()  # El menú permite según las opciones controlar la Entrada, Proceso y Salida de los Datos.
        opcionStr = input(f"Elija una opción (1-{opcionSalida})\t")
        opcion = ingresarOpcionValida(opcionStr, opcionSalida)
        if opcion > 0 and opcion <= int(opcionSalida):
            ##print("Eligiste la opción ", opcion)
            procesarOpcionElegida(opcion, opcionSalida)  # PROCESO
            if opcion == int(opcionSalida):
                break
        else:
            print(
                f"Opción no válida - Ingrese un número del 1 al {opcionSalida}"
            )  # Salida

        # input("Presione Enter para continuar.")

    print("Fin del programa inventario.")


# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    main()
