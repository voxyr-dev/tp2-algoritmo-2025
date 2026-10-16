#TP2- Cerri, Herrero, Quiroz, Speca


# Declaración de variables

# int

# global_novedad1_cod, global_novedad2_cod, global_novedad3_cod = int
# numero_random, max_intentos, intentos, indice_disponible, i, j, col, fila = int
# cant_aerolineas, cant_a_crear, vuelos_creados, codigo_a_modificar, codigo_a_eliminar, codigo_vuelo = int
# max_opcion, opcion_entero = int

# float

# precio_vuelo = float

# str

# global_novedad1_texto, global_novedad1_publicacion, global_novedad1_expiracion = string
# global_novedad2_texto, global_novedad2_publicacion, global_novedad2_expiracion = string
# global_novedad3_texto, global_novedad3_publicacion, global_novedad3_expiracion = string
# tipo_usuario_encontrado, tipo_usuario_logueado, entrada_usuario, entrada_clave, email, clave, clave2 = string
# nombre_aerolinea, codigo_iata, descripcion_aerolinea, cod_pais, confirmacion, respuesta = string
# origen, destino, fecha_vuelo, hora_vuelo, estado_vuelo, fecha_actual_cadena = string
# opcion, mensaje, ver_lista = string

# bool

# encontrado, condicion_login, codigo_valido, codigo_existe, tiene_vuelos_asociados, aerolinea_encontrada = int
# precio_valido, proceder_modificacion, vuelos_encontrados, continuar_busqueda, opcion_valida = int
# continuar_en_menu, continuar_en_submenu, control_sesion_general = int

# array

# usuarios, aerolineas, vuelos, asientos = array
# precios_vuelos = array

usuarios = [['' for _ in range(4)] for _ in range(10)]

aerolineas = [['' for _ in range(5)] for _ in range(20)]

vuelos = [['' for _ in range(7)] for _ in range(20)]

precios_vuelos = [0.0 for _ in range(20)]

asientos = [['' for _ in range(6)] for _ in range(40 * 20)]

import getpass
from datetime import datetime


global_novedad1_cod = 1
global_novedad1_texto = "Debido a tareas de mantenimiento, el aeropuerto permanecerá cerrado el próximo domingo. Se reprogramarán los vuelos afectados."
global_novedad1_publicacion = "2025-05-01"
global_novedad1_expiracion = "2025-06-08"

global_novedad2_cod = 2
global_novedad2_texto = "¡Felices fiestas! Ofrecemos un 10 porciento de descuento adicional en todos los vuelos para pasajeros Premium durante el mes de diciembre"
global_novedad2_publicacion = "2025-12-01"
global_novedad2_expiracion = "2025-12-31"

global_novedad3_cod = 3
global_novedad3_texto = "Requisitos nuevos para viajar a Europa"
global_novedad3_publicacion = "2025-05-07"
global_novedad3_expiracion = "2025-06-15"


numero_random = 42

def CargarUsuarios(usuarios_arr):
    """
    Carga los datos iniciales de usuarios en el array global.
    """
    usuarios_arr[0][0] = 0
    usuarios_arr[0][1] = "admin@ventaspasajes777.com"
    usuarios_arr[0][2] = "admin123"
    usuarios_arr[0][3] = "administrador"

    usuarios_arr[1][0] = 1
    usuarios_arr[1][1] = "ceo1@ventaspasajes777.com"
    usuarios_arr[1][2] = "ceo123"
    usuarios_arr[1][3] = "ceo"

    usuarios_arr[2][0] = 2
    usuarios_arr[2][1] = "ceo2@ventaspasajes777.com"
    usuarios_arr[2][2] = "ceo456"
    usuarios_arr[2][3] = "ceo"

    usuarios_arr[3][0] = 3
    usuarios_arr[3][1] = "ceo3@ventapasajes777.com"
    usuarios_arr[3][2] = "ceo789"
    usuarios_arr[3][3] = "ceo"

    usuarios_arr[4][0] = 4
    usuarios_arr[4][1] = "ceo4@ventapasajes777.com"
    usuarios_arr[4][2] = "ceo012"
    usuarios_arr[4][3] = "ceo"

    usuarios_arr[5][0] = 5
    usuarios_arr[5][1] = "ceo5@ventaspasajes777.com"
    usuarios_arr[5][2] = "ceo345"
    usuarios_arr[5][3] = "ceo"

    usuarios_arr[6][0] = 6
    usuarios_arr[6][1] = "usuario1@ventaspasajes777.com"
    usuarios_arr[6][2] = "usuario123"
    usuarios_arr[6][3] = "usuario"

    usuarios_arr[7][0] = 7
    usuarios_arr[7][1] = "Usuario2@ventaspasajes777.com"
    usuarios_arr[7][2] = "usuario456"
    usuarios_arr[7][3] = "usuario"

    usuarios_arr[8][0] = 8
    usuarios_arr[8][1] = ""
    usuarios_arr[8][2] = ""
    usuarios_arr[8][3] = ""

    usuarios_arr[9][0] = 9
    usuarios_arr[9][1] = ""
    usuarios_arr[9][2] = ""
    usuarios_arr[9][3] = ""

def CargarAerolineas(aerolineas_arr):
    """
    Carga datos iniciales de aerolíneas.
    """
    aerolineas_arr[0][0] = 1
    aerolineas_arr[0][1] = "Aerolineas Argentinas"
    aerolineas_arr[0][2] = "AR"
    aerolineas_arr[0][3] = "Principal aerolinea de Argentina"
    aerolineas_arr[0][4] = "ARG"

    aerolineas_arr[1][0] = 2
    aerolineas_arr[1][1] = "LATAM"
    aerolineas_arr[1][2] = "LA"
    aerolineas_arr[1][3] = "Una de las mayores aerolineas de Brasil"
    aerolineas_arr[1][4] = "CHI"

    aerolineas_arr[2][0] = 3
    aerolineas_arr[2][1] = "Fly Bondi"
    aerolineas_arr[2][2] = "FB"
    aerolineas_arr[2][3] = "Aerolínea Low-cost"
    aerolineas_arr[2][4] = "CHI"

    aerolineas_arr[3][0] = 4
    aerolineas_arr[3][1] = "Gol"
    aerolineas_arr[3][2] = "GB"
    aerolineas_arr[3][3] = "Principal aerolinea de Brasil"
    aerolineas_arr[3][4] = "BRA"

    aerolineas_arr[4][0] = 5
    aerolineas_arr[4][1] = "Sky Airline"
    aerolineas_arr[4][2] = "SA"
    aerolineas_arr[4][3] = "Aerolínea de alto nivel"
    aerolineas_arr[4][4] = "ARG"

def cartel():

    print("\033[1;93m╔════════════════════╗\033[0m")
    print("\033[1;93m║ En construcción... ║\033[0m")
    print("\033[1;93m╚════════════════════╝\033[0m")

def es_numero_entero(cadena):
    """
    Verifica si una cadena contiene solo dígitos.
    """
    if len(cadena) == 0:
        return 0
    i = 0
    while i < len(cadena):
        caracter = cadena[i]
        if not ('0' <= caracter <= '9'):
            return 0
        i += 1
    return 1

def controlar_credenciales(nombre_usuario, clave, usuarios_arr):
    """
    Verifica si las credenciales ingresadas coinciden con algún usuario.
    Retorna el tipo de usuario si las credenciales son válidas, de lo contrario cadena vacía.
    """
    tipo_usuario_encontrado = ""
    indice = 0
    encontrado = 0
    while indice < len(usuarios_arr) and encontrado == 0:
        if usuarios_arr[indice][1] == nombre_usuario and usuarios_arr[indice][2] == clave:
            tipo_usuario_encontrado = usuarios_arr[indice][3]
            encontrado = 1
        else:
            indice += 1
    return tipo_usuario_encontrado

def iniciar_sesion(usuarios_arr):
    """
    Maneja el proceso de inicio de sesión, incluyendo el control de intentos.
    Retorna el tipo de usuario si el login es exitoso, de lo contrario cadena vacía.
    """
    intentos = 0
    max_intentos = 3
    tipo_usuario_logueado = ""

    condicion_login = 0
    while condicion_login == 0:
        entrada_usuario = input("Ingrese su nombre de usuario: ")
        entrada_clave = getpass.getpass("Ingrese su contraseña: ")
        tipo_usuario_logueado = controlar_credenciales(entrada_usuario, entrada_clave, usuarios_arr)

        if tipo_usuario_logueado != "":
            print("Inicio de sesión exitoso. ¡Bienvenido,", entrada_usuario, "!")
            condicion_login = 1
        else:
            intentos += 1
            if intentos < max_intentos:
                print("Usuario o clave incorrectos. Intentos restantes:", str(max_intentos - intentos))
            else:
                print("Ha excedido el número máximo de intentos. Volviendo al menú principal.")
                condicion_login = -1
    return tipo_usuario_logueado

def registrar_usuario(usuarios_arr):
    print("\n--- Registro de Nuevo Usuario ---")
    indice_disponible = -1
    i = 8
    while i < 10 and indice_disponible == -1:
        if usuarios_arr[i][1] == "":
            indice_disponible = i
        i += 1

    if indice_disponible == -1:
        print("No hay más espacio para registrar nuevos usuarios.")
    else:
        email = input("Ingrese su email: ")
        i = 0
        encontrado = 0
        while i < 10 and encontrado == 0:
            if usuarios_arr[i][1] == email:
                encontrado = 1
            else:
                i += 1

        if encontrado == 1:
            print("Este email ya está registrado.")
        else:
            clave = getpass.getpass("Ingrese su contraseña: ")
            clave2 = getpass.getpass("Repita su contraseña: ")
            while clave != clave2:
                print("Las contraseñas no coinciden. Intente de nuevo.")
                clave = getpass.getpass("Ingrese su contraseña: ")
                clave2 = getpass.getpass("Repita su contraseña: ")

            usuarios_arr[indice_disponible][1] = email
            usuarios_arr[indice_disponible][2] = clave
            usuarios_arr[indice_disponible][3] = "usuario"
            print("Usuario registrado con éxito.")



def entero_random(max_val):
    """
    Genera un número random entre 0 y max_val-1.
    """
    global numero_random
    a = 1664525
    c = 1013904223
    m = 2**32
    numero_random = (a * numero_random + c) % m
    return numero_random % max_val

def InicializarAsientos(indice_vuelo, asientos_arr):
    """
    Inicializa los 240 asientos de un vuelo con estados aleatorios.
    """
    fila_inicio = indice_vuelo * 40
    fila_fin = fila_inicio + 40
    
    fila = fila_inicio
    while fila < fila_fin:
        col = 0
        while col < 6:
            
            indice_estado = entero_random(3)
            
            
            if indice_estado == 0:
                estado_asiento = 'L'  
            elif indice_estado == 1:
                estado_asiento = 'O'  
            else: 
                estado_asiento = 'R'  
            
            asientos_arr[fila][col] = estado_asiento
            col += 1
        fila += 1
        
    print("Matriz de asientos para el vuelo con código", vuelos[indice_vuelo][0], "inicializada aleatoriamente.")



def CrearAerolinea(aerolineas_arr):
    print("Bienvenido. En este menú podrá crear su aerolínea(s).")
    
    cant_aerolineas = 0
    while not (cant_aerolineas >= 1 and cant_aerolineas <= 20):
        cant_aerolineas_cadena = input("Ingrese la cantidad de aerolíneas a crear (1 a 20): ")
        if es_numero_entero(cant_aerolineas_cadena):
            cant_aerolineas_entero = int(cant_aerolineas_cadena)
            if cant_aerolineas_entero >= 1 and cant_aerolineas_entero <= 20:
                cant_aerolineas = cant_aerolineas_entero
            else:
                print("La cantidad debe estar entre 1 y 20.")
        else:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    i_creacion = 0
    while i_creacion < cant_aerolineas:
        print("\n...Creando nueva aerolínea " + str(i_creacion + 1) + " de " + str(cant_aerolineas) + "...")
        
        indice_disponible = -1
        i = 0
        while i < len(aerolineas_arr):
            if aerolineas_arr[i][0] == "":
                indice_disponible = i
                i = len(aerolineas_arr)
            i += 1

        if indice_disponible == -1:
            print("No hay espacio disponible para crear más aerolíneas.")
            i_creacion = cant_aerolineas
        else:
            cod_aerolinea = 0
            codigo_valido = 0
            while codigo_valido == 0:
                cod_aerolinea_cadena = input("Ingrese el código de la aerolínea: ")
                if es_numero_entero(cod_aerolinea_cadena):
                    cod_aerolinea_entero = int(cod_aerolinea_cadena)
                    codigo_existe = 0
                    i = 0
                    while i < len(aerolineas_arr):
                        if aerolineas_arr[i][0] == cod_aerolinea_entero:
                            codigo_existe = 1
                            i = len(aerolineas_arr)
                        i += 1
                    
                    if codigo_existe == 1:
                        print("Error: El código de aerolínea ya existe.")
                    else:
                        cod_aerolinea = cod_aerolinea_entero
                        codigo_valido = 1
                else:
                    print("Entrada inválida. Ingrese un número entero para el código.")

            nombre_aerolinea = input("Ingrese el nombre de la aerolínea (Máx. 100 caracteres): ")
            while len(nombre_aerolinea) > 100:
                print("Excediste el límite de caracteres.")
                nombre_aerolinea = input("Ingrese el nombre de la aerolínea (Máx. 100 caracteres): ")
            
            codigo_iata = input("Ingrese el código IATA (Máx. 3 caracteres): ")
            while len(codigo_iata) > 3:
                print("Excediste el límite de caracteres.")
                codigo_iata = input("Ingrese el código IATA (Máx. 3 caracteres): ")

            descripcion_aerolinea = input("Ingrese la descripción (Máx. 200 caracteres): ")
            while len(descripcion_aerolinea) > 200:
                print("Excediste el límite de caracteres.")
                descripcion_aerolinea = input("Ingrese la descripción (Máx. 200 caracteres): ")

            cod_pais = input("Ingrese el código del país (ARG - BRA - CHI): ")
            while not (cod_pais == "ARG" or cod_pais == "BRA" or cod_pais == "CHI"):
                print("Código incorrecto. Opciones: ARG - BRA - CHI")
                cod_pais = input("Ingrese el código del país (ARG - BRA - CHI): ")

            aerolineas_arr[indice_disponible][0] = cod_aerolinea
            aerolineas_arr[indice_disponible][1] = nombre_aerolinea
            aerolineas_arr[indice_disponible][2] = codigo_iata
            aerolineas_arr[indice_disponible][3] = descripcion_aerolinea
            aerolineas_arr[indice_disponible][4] = cod_pais

            print("\nAerolínea creada con éxito.")
        i_creacion += 1

def ModificarAerolinea(aerolineas_arr):
    print("\n--- Modificar Aerolínea ---")
    codigo_a_modificar = -1
    while not (codigo_a_modificar >= 0):
        codigo_cadena = input("Ingrese el código de la aerolínea a modificar: ")
        if es_numero_entero(codigo_cadena):
            codigo_a_modificar = int(codigo_cadena)
        else:
            print("Entrada inválida. Ingrese un número entero.")

    indice_encontrado = -1
    i = 0
    while i < len(aerolineas_arr):
        if aerolineas_arr[i][0] == codigo_a_modificar:
            indice_encontrado = i
            i = len(aerolineas_arr)
        i += 1

    if indice_encontrado != -1:
        print("\nAerolínea encontrada. Ingrese los nuevos datos (deje vacío para mantener):")

        entrada_nombre = input("Nuevo nombre (" + str(aerolineas_arr[indice_encontrado][1]) + "): ")
        if len(entrada_nombre) > 0:
             while len(entrada_nombre) > 100:
                print("Excediste el límite de caracteres.")
                entrada_nombre = input("Nuevo nombre: ")
             aerolineas_arr[indice_encontrado][1] = entrada_nombre

        entrada_iata = input("Nuevo código IATA (" + str(aerolineas_arr[indice_encontrado][2]) + "): ")
        if len(entrada_iata) > 0:
            while len(entrada_iata) > 3:
                print("Excediste el límite de caracteres.")
                entrada_iata = input("Nuevo código IATA: ")
            aerolineas_arr[indice_encontrado][2] = entrada_iata
        
        
        print("\n¡Aerolínea modificada con éxito!")
    else:
        print("Código de aerolínea no encontrado.")




def verNovedades():
    print("\n--- Novedades del Sistema ---")
    print("------------------------------------------------------")
    print("Novedad nro:", global_novedad1_cod)
    print("Texto:", global_novedad1_texto)
    print("------------------------------------------------------")
    print("Novedad nro:", global_novedad2_cod)
    print("Texto:", global_novedad2_texto)
    print("------------------------------------------------------")
    print("Novedad nro:", global_novedad3_cod)
    print("Texto:", global_novedad3_texto)
    print("------------------------------------------------------")

def editarNovedades():
    global global_novedad1_texto, global_novedad2_texto, global_novedad3_texto
    codigo = -1
    while not (codigo >= 0):
        codigo_cadena = input("Ingrese el código de la novedad a modificar (1, 2, o 3): ")
        if es_numero_entero(codigo_cadena):
            codigo = int(codigo_cadena)
        else:
            print("Entrada inválida.")
    
    if codigo == global_novedad1_cod:
        global_novedad1_texto = input("Ingrese el nuevo texto: ")
        print("¡Novedad 1 modificada con éxito!")
    elif codigo == global_novedad2_cod:
        global_novedad2_texto = input("Ingrese el nuevo texto: ")
        print("¡Novedad 2 modificada con éxito!")
    elif codigo == global_novedad3_cod:
        global_novedad3_texto = input("Ingrese el nuevo texto: ")
        print("¡Novedad 3 modificada con éxito!")
    else:
        print("Código de novedad no encontrado.")

def CrearNovedad():
    cartel()

def EliminarNovedad():
    cartel()



def BuscarAerolineaPorIATA(cod_iata, aerolineas_arr):
    """
    Busca una aerolínea por su código IATA. Retorna 1 si la encuentra, 0 si no.
    """
    i = 0
    encontrada = 0
    while i < len(aerolineas_arr) and encontrada == 0:
        if aerolineas_arr[i][2] == cod_iata:
            encontrada = 1
        i += 1
    return encontrada

from datetime import datetime

def CrearVuelo(vuelos_arr, aerolineas_arr, precios_vuelos_arr, asientos_arr):
    print("\n--- Crear Nuevo(s) Vuelo(s) ---")
    
    cant_a_crear = 0
    while cant_a_crear <= 0:
        cant_cadena = input("Ingrese la cantidad de vuelos que desea crear: ")
        if es_numero_entero(cant_cadena):
            cant_entero = int(cant_cadena)
            if cant_entero > 0 and cant_entero <= 20:
                cant_a_crear = cant_entero
            else:
                print("Error: La cantidad debe ser un número entre 1 y 20.")
        else:
            print("Error: Ingrese un número entero válido.")

    vuelos_creados = 0
    while vuelos_creados < cant_a_crear:
        print("\n--- Creando Vuelo " + str(vuelos_creados + 1) + " de " + str(cant_a_crear) + " ---")
        
        indice_disponible = -1
        i = 0
        while i < len(vuelos_arr):
            if vuelos_arr[i][0] == "":
                indice_disponible = i
                i = len(vuelos_arr) 
            i += 1

        if indice_disponible == -1:
            print("No hay más espacio disponible para crear vuelos. Proceso cancelado.")
            vuelos_creados = cant_a_crear 
        else:
            cod_vuelo = 0
            verificacion_codigo = 1
            while verificacion_codigo == 1:
                cod_vuelo_cadena = input("Ingrese el código del vuelo: ")
                if es_numero_entero(cod_vuelo_cadena):
                    cod_vuelo_entero = int(cod_vuelo_cadena)
                    codigo_existe = 0
                    i = 0
                    while i < len(vuelos_arr):
                        if vuelos_arr[i][0] == cod_vuelo_entero:
                            codigo_existe = 1
                            i = len(vuelos_arr) 
                        i += 1
                    
                    if codigo_existe == 1:
                        print("Error: El código de vuelo ya existe.")
                    else:
                        cod_vuelo = cod_vuelo_entero
                        verificacion_codigo = 0
                else:
                    print("Entrada inválida. Ingrese un número entero.")

            cod_aerolinea_iata = ""
            aerolinea_encontrada = 0
            while aerolinea_encontrada == 0:
                entrada_iata = input("Ingrese el código IATA de la aerolínea (disponibles: AR, LA, FB, GB, SA): ")
                if BuscarAerolineaPorIATA(entrada_iata, aerolineas_arr) == 1:
                    cod_aerolinea_iata = entrada_iata
                    aerolinea_encontrada = 1
                else:
                    print("Código IATA no encontrado. Intente de nuevo.")

            origen = input("Ingrese el origen del vuelo: ")
            destino = input("Ingrese el destino del vuelo: ")
            fecha_vuelo = input("Ingrese la fecha del vuelo (AAAA-MM-DD): ")
            
            # --- SECCIÓN DE VALIDACIÓN DE HORA MODIFICADA ---
            hora_vuelo = ""
            hora_valida = 0
            while hora_valida == 0:
                hora_cadena = input("Ingrese la hora del vuelo (HH:MM): ")
                # 1. Validar formato general (longitud 5 y ':' en el medio)
                if len(hora_cadena) == 5 and hora_cadena[2] == ':':
                    # Extraer hora y minuto usando slicing de cadena
                    hora_str = hora_cadena[0:2]
                    minuto_str = hora_cadena[3:5]
                    
                    # 2. Validar que ambas partes sean numéricas
                    if es_numero_entero(hora_str) and es_numero_entero(minuto_str):
                        hora = int(hora_str)
                        minuto = int(minuto_str)
                        
                        # 3. Validar el rango numérico de la hora y minuto
                        if (hora >= 0 and hora <= 23) and (minuto >= 0 and minuto <= 59):
                            hora_vuelo = hora_cadena
                            hora_valida = 1 # Hora correcta, salir del bucle
                        else:
                            print("Error: La hora (0-23) o los minutos (0-59) están fuera de rango.")
                    else:
                        print("Error: La hora y los minutos deben ser números.")
                else:
                    print("Error: El formato debe ser HH:MM.")
            # --- FIN DE LA SECCIÓN MODIFICADA ---

            precio_vuelo = -1.0
            precio_valido = 0
            while precio_valido == 0:
                precio_cadena = input("Ingrese el precio del vuelo: ")
                if es_numero_entero(precio_cadena):
                    precio_vuelo = float(precio_cadena)
                    if precio_vuelo > 0:
                        precio_valido = 1
                    else:
                        print("El precio debe ser un número positivo.")
                else:
                    print("Entrada inválida para el precio.")
            
            fecha_actual_cadena = datetime.now().strftime("%Y-%m-%d")
            estado_vuelo = "A"
            if fecha_vuelo < fecha_actual_cadena:
                estado_vuelo = "E"
                print("AVISO: La fecha es anterior a la actual. El estado será 'Expirado'.")

            vuelos_arr[indice_disponible][0] = cod_vuelo
            vuelos_arr[indice_disponible][1] = cod_aerolinea_iata
            vuelos_arr[indice_disponible][2] = origen
            vuelos_arr[indice_disponible][3] = destino
            vuelos_arr[indice_disponible][4] = fecha_vuelo
            vuelos_arr[indice_disponible][5] = hora_vuelo
            vuelos_arr[indice_disponible][6] = estado_vuelo
            precios_vuelos_arr[indice_disponible] = precio_vuelo
            
            InicializarAsientos(indice_disponible, asientos_arr)

            print("\n¡Vuelo creado con éxito!")
            vuelos_creados += 1

def ModificarVuelo(vuelos_arr, aerolineas_arr, precios_vuelos_arr):
    print("\n--- Modificar Vuelo ---")
    codigo_a_modificar = -1
    while not (codigo_a_modificar >= 0):
        codigo_cadena = input("Ingrese el código del vuelo a modificar: ")
        if es_numero_entero(codigo_cadena):
            codigo_a_modificar = int(codigo_cadena)
        else:
            print("Entrada inválida.")

    indice_encontrado = -1
    i = 0
    while i < len(vuelos_arr):
        if vuelos_arr[i][0] == codigo_a_modificar:
            indice_encontrado = i
            i = len(vuelos_arr)
        i += 1

    if indice_encontrado != -1:
        estado_vuelo = vuelos_arr[indice_encontrado][6]
        proceder_modificacion = 0

        if estado_vuelo == "B":
            respuesta = input("El vuelo está dado de baja. ¿Desea activarlo para modificarlo? (S/N): ")
            if respuesta == "S" or respuesta == "s":
                vuelos_arr[indice_encontrado][6] = "A"
                print("Vuelo reactivado.")
                proceder_modificacion = 1
            else:
                print("Modificación cancelada.")
        elif estado_vuelo == "A":
            proceder_modificacion = 1

        if proceder_modificacion == 1:
            print("\nIngrese los nuevos datos (deje vacío para mantener):")
            
            
            entrada_origen = input("Nuevo origen (" + vuelos_arr[indice_encontrado][2] + "): ")
            if len(entrada_origen) > 0:
                vuelos_arr[indice_encontrado][2] = entrada_origen
            
            entrada_precio = input("Nuevo precio (" + str(precios_vuelos_arr[indice_encontrado]) + "): ")
            if len(entrada_precio) > 0 and es_numero_entero(entrada_precio):
                precios_vuelos_arr[indice_encontrado] = float(entrada_precio)
            
            print("\n¡Vuelo modificado con éxito!")
    else:
        print("Código de vuelo no encontrado.")

def EliminarVuelo(vuelos_arr):
    
    print("\n--- Eliminar Vuelo (Baja Lógica) ---")
    codigo_a_eliminar = -1
    while not (codigo_a_eliminar >= 0):
        codigo_cadena = input("Ingrese el código del vuelo que desea dar de baja: ")
        if es_numero_entero(codigo_cadena):
            codigo_a_eliminar = int(codigo_cadena)
        else:
            print("Entrada inválida.")

    indice_encontrado = -1
    i = 0
    while i < len(vuelos_arr):
        if vuelos_arr[i][0] == codigo_a_eliminar:
            indice_encontrado = i
            i = len(vuelos_arr)
        i += 1

    if indice_encontrado != -1:
        if vuelos_arr[indice_encontrado][6] == "A":
            confirmacion = input("¿Está seguro de que desea dar de baja este vuelo? (S/N): ")
            if confirmacion == "S" or confirmacion == "s":
                vuelos_arr[indice_encontrado][6] = "B"
                print("¡Vuelo dado de baja con éxito!")
            else:
                print("Operación cancelada.")
        else:
            print("El vuelo ya se encuentra dado de baja o expirado.")
    else:
        print("Código de vuelo no encontrado.")

def ListarVuelos(vuelos_arr, precios_vuelos_arr):
    print("\n--- Listado de Vuelos ---")
    vuelos_encontrados = 0
    i = 0
    while i < len(vuelos_arr):
        if vuelos_arr[i][0] != "":
            vuelos_encontrados = 1
            print("------------------------------------------------------")
            print("Código:", vuelos_arr[i][0])
            print("Aerolínea (IATA):", vuelos_arr[i][1])
            print("Origen:", vuelos_arr[i][2])
            print("Destino:", vuelos_arr[i][3])
            print("Fecha:", vuelos_arr[i][4])
            print("Hora:", vuelos_arr[i][5])
            print("Estado:", vuelos_arr[i][6])
            print("Precio: $", precios_vuelos_arr[i])
            print("------------------------------------------------------")
        i += 1
    if vuelos_encontrados == 0:
        print("No hay vuelos registrados.")



def buscar_y_listar_vuelos(vuelos_arr, precios_vuelos_arr):
    print("\n--- Búsqueda de Vuelos por Fecha ---")
    fecha_salida_busqueda = input("Ingrese la fecha desde la cual buscar (AAAA-MM-DD): ")
    
    print("\n==========================================================================================================================")
    print("                              LISTADO DE VUELOS DISPONIBLES EN EL SISTEMA")
    print("==========================================================================================================================")
    print("CÓDIGO\t\tAEROLÍNEA\t\tORIGEN\t\tDESTINO\t\t\tFECHA\t\tHORA\t\tPRECIO")
    print("--------------------------------------------------------------------------------------------------------------------------")
    
    vuelos_encontrados = 0
    i = 0
    while i < len(vuelos_arr):
        vuelo = vuelos_arr[i]
        if vuelo[0] != "" and vuelo[6] == "A" and vuelo[4] >= fecha_salida_busqueda:
            codigo_vuelo = str(vuelo[0])
            aerolinea = str(vuelo[1])
            origen = str(vuelo[2])
            destino = str(vuelo[3])
            fecha = str(vuelo[4])
            hora = str(vuelo[5])
            precio = str(precios_vuelos_arr[i])
            
            print(codigo_vuelo + "\t\t" + aerolinea + "\t\t\t" + origen + "\t\t" + destino + "\t\t\t" + fecha + "\t" + hora + "\t$" + precio)
            vuelos_encontrados = vuelos_encontrados + 1
        i = i + 1

    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Total de vuelos encontrados:", vuelos_encontrados)

def buscar_asientos(vuelos_arr, asientos_arr):
    print("\n--- Búsqueda de Asientos ---")
    
    continuar_busqueda = 1
    while continuar_busqueda == 1:
        codigo_vuelo_cadena = input("Ingrese el código del vuelo que desea buscar (o 'S' para salir): ")
        
        if codigo_vuelo_cadena == "S" or codigo_vuelo_cadena == "s":
            continuar_busqueda = 0
        elif es_numero_entero(codigo_vuelo_cadena):
            codigo_vuelo = int(codigo_vuelo_cadena)
            
            indice_vuelo = -1
            i = 0
            while i < len(vuelos_arr):
                if vuelos_arr[i][0] == codigo_vuelo:
                    indice_vuelo = i
                    i = len(vuelos_arr)
                i += 1
            
            if indice_vuelo != -1:
                fecha_vuelo_cadena = vuelos_arr[indice_vuelo][4]
                fecha_actual_cadena = datetime.now().strftime("%Y-%m-%d")
                estado_vuelo = vuelos_arr[indice_vuelo][6]
                
                
                if estado_vuelo == "A" and fecha_vuelo_cadena >= fecha_actual_cadena:
                    print("\nVuelo encontrado y vigente. Mostrando estado de los asientos:")
                    
                    
                    print("     A B C   D E F")
                    
                    fila_inicio_vuelo = indice_vuelo * 40
                    fila_fin_vuelo = fila_inicio_vuelo + 40
                    
                    fila_relativa = 0
                    fila_absoluta = fila_inicio_vuelo
                    while fila_absoluta < fila_fin_vuelo:
                        fila_cadena = ""
                        col = 0
                        
                        while col < 6:
                            estado = asientos_arr[fila_absoluta][col]
                            fila_cadena += estado + " "
                            if col == 2: 
                                fila_cadena += "  " 
                            col += 1
                        
                        num_fila_cadena = str(fila_relativa + 1)
                        if len(num_fila_cadena) == 1:
                            num_fila_cadena = "0" + num_fila_cadena
                            
                        print(num_fila_cadena + "  " + fila_cadena)
                        
                        fila_relativa += 1
                        fila_absoluta += 1
                    
                    print("\nLeyenda: L=Libre, O=Ocupado, R=Reservado.")
                    print("El pasillo es el espacio entre los asientos C y D.")
                    
                    
                else:
                    print("El vuelo no está vigente (su fecha ya pasó o fue dado de baja).")
                
            else:
                print("Código de vuelo no encontrado.")
        else:
            print("Entrada inválida.")
    print("Volviendo al menú de usuario.")
    


def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Registrarme")
    print("2. Iniciar Sesión")
    print("3. Salir")

def obtener_opcion_valida(mensaje, max_opcion):
    opcion = ""
    opcion_valida = 0
    while opcion_valida == 0:
        entrada_opcion = input(mensaje)
        if es_numero_entero(entrada_opcion):
            opcion_entero = int(entrada_opcion)
            if opcion_entero >= 1 and opcion_entero <= max_opcion:
                opcion = entrada_opcion
                opcion_valida = 1
        
        if opcion_valida == 0:
            print("Opción inválida. Ingrese un número entre 1 y", max_opcion)
    return opcion

def mostrar_menu_administrador():
    print("\n--- Menú Administrador ---")
    print("1. Gestión de aerolíneas")
    print("2. Aprobar/Denegar promociones")
    print("3. Gestión de novedades")
    print("4. Reportes")
    print("5. Cerrar Sesión")

def ejecutar_menu_administrador():
    continuar_en_menu = 1
    while continuar_en_menu == 1:
        mostrar_menu_administrador()
        opcion = obtener_opcion_valida("Seleccione una opción: ", 5)
        if opcion == '1':
            ejecutar_menu_gestionar_aerolineas(aerolineas)
        elif opcion == '2': cartel()
        elif opcion == '3': ejecutar_menu_gestionar_novedades()
        elif opcion == '4': cartel()    
        elif opcion == '5':
            print("Cerrando sesión de administrador.")
            continuar_en_menu = 0

def mostrar_menu_gestionar_aerolineas():
    print("\n--- Administrar Aerolíneas ---")
    print("1. Crear Aerolínea")
    print("2. Modificar Aerolínea")
    print("3. Eliminar Aerolínea")
    print("4. Volver")

def ejecutar_menu_gestionar_aerolineas(aerolineas_arr):
    continuar_en_submenu = 1
    while continuar_en_submenu == 1:
        mostrar_menu_gestionar_aerolineas()
        opcion = obtener_opcion_valida("Seleccione una opción: ", 4)
        if opcion == '1': CrearAerolinea(aerolineas_arr)
        elif opcion == '2': ModificarAerolinea(aerolineas_arr)
        elif opcion == '3': cartel() 
        elif opcion == '4': continuar_en_submenu = 0

def mostrar_menu_gestionar_novedades():
    print("\n--- Gestionar Novedades ---")
    print("1. Crear Novedad")
    print("2. Editar Novedades")
    print("3. Eliminar Novedad")
    print("4. Ver Novedades")
    print("5. Volver")

def ejecutar_menu_gestionar_novedades():
    continuar_en_submenu = 1
    while continuar_en_submenu == 1:
        mostrar_menu_gestionar_novedades()
        opcion = obtener_opcion_valida("Seleccione una opción: ", 5)
        if opcion == '1': CrearNovedad()
        elif opcion == '2': editarNovedades()
        elif opcion == '3': EliminarNovedad()
        elif opcion == '4': verNovedades()
        elif opcion == '5': continuar_en_submenu = 0

def mostrar_menu_ceo():
    print("\n--- Menú CEO ---")
    print("1. Gestión de vuelos")
    print("2. Gestión de promociones")
    print("3. Reportes")
    print("4. Cerrar sesión")

def ejecutar_menu_ceo():
    continuar_en_menu = 1
    while continuar_en_menu == 1:
        mostrar_menu_ceo()
        opcion = obtener_opcion_valida("Seleccione una opción: ", 4)
        if opcion == '1':
            ejecutar_menu_gestionar_vuelos()
        elif opcion == '2': cartel()
        elif opcion == '3': cartel()
        elif opcion == '4':
            print("Cerrando sesión de CEO.")
            continuar_en_menu = 0

def mostrar_menu_gestionar_vuelos():
    print("\n--- Administrar Vuelos ---")
    print("1. Crear Vuelo")
    print("2. Modificar Vuelo")
    print("3. Eliminar Vuelo")
    print("4. Listar Vuelos")
    print("5. Volver")

def ejecutar_menu_gestionar_vuelos():
    continuar_en_submenu = 1
    while continuar_en_submenu == 1:
        mostrar_menu_gestionar_vuelos()
        opcion = obtener_opcion_valida("Seleccione una opción: ", 5)
        
        if opcion == '1' or opcion == '2' or opcion == '3':
            ver_lista = input("¿Desea ver los vuelos ya cargados? (S/N): ")
            if ver_lista == 'S' or ver_lista == 's':
                ListarVuelos(vuelos, precios_vuelos)

        if opcion == '1': CrearVuelo(vuelos, aerolineas, precios_vuelos, asientos)
        elif opcion == '2': ModificarVuelo(vuelos, aerolineas, precios_vuelos)
        elif opcion == '3': EliminarVuelo(vuelos)
        elif opcion == '4': ListarVuelos(vuelos, precios_vuelos)
        elif opcion == '5': continuar_en_submenu = 0

def mostrar_menu_usuario():
    print("\n--- Menú Usuario ---")
    print("1. Buscar vuelos por fecha")
    print("2. Buscar asientos de un vuelo")
    print("3. Reservar Vuelos")
    print("4. Gestionar reservas")
    print("5. Ver historial de compras")
    print("6. Ver novedades")
    print("7. Cerrar sesión")

def ejecutar_menu_usuario():
    continuar_en_menu = 1
    while continuar_en_menu == 1:
        mostrar_menu_usuario()
        opcion = obtener_opcion_valida("Seleccione una opción: ", 7)
        if opcion == '1': buscar_y_listar_vuelos(vuelos, precios_vuelos)
        elif opcion == '2': buscar_asientos(vuelos, asientos)
        elif opcion == '3': cartel()
        elif opcion == '4': cartel()
        elif opcion == '5': cartel()
        elif opcion == '6': verNovedades()
        elif opcion == '7':
            print("Cerrando sesión.")
            continuar_en_menu = 0

def programa_principal():
    CargarUsuarios(usuarios)
    CargarAerolineas(aerolineas)

    control_sesion_general = 0
    while control_sesion_general == 0:
        mostrar_menu_principal()
        opcion_principal = obtener_opcion_valida("Seleccione una opción: ", 3)

        if opcion_principal == '1':
            registrar_usuario(usuarios)
        elif opcion_principal == '2':
            tipo_usuario = iniciar_sesion(usuarios)
            if tipo_usuario == "administrador":
                ejecutar_menu_administrador()
            elif tipo_usuario == "ceo":
                ejecutar_menu_ceo()
            elif tipo_usuario == "usuario":
                ejecutar_menu_usuario()
        elif opcion_principal == '3':
            print("Saliendo del programa.")
            control_sesion_general = 1

programa_principal()