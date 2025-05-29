eimport random

juego_continua = True

#####################################################################################################



def intro_juego():
  print("\n")
  print("\t","######################  Bienvenido al juego de Anarquistas vs Fascistas  ######################")
  print("\n")

  ancho_tablero = input("Indique el ancho del tablero con el que desea jugar: ") 
  alto_tablero = input("Indique el alto del tablero con el que desea jugar: ")

  if  es_numerico(ancho_tablero) == False or es_numerico(alto_tablero) == False:
    print()
    print("Debe ingresar valores de dimension validos")
    print()
    return intro_juego()
  
  if int(ancho_tablero) < 2 or int(alto_tablero) < 2 :
    print()
    print("El tablero debe ser de al menos 2x2 celdas")
    print()
    return intro_juego()
  
  if int(ancho_tablero) > 50 or int(alto_tablero) > 20 :
    print()
    print("El tablero debe ser de como maximo de 50x20 celdas")
    print()
    return intro_juego()
  

  else:
    return empezar_juego(int(ancho_tablero),int(alto_tablero))


#####################################################################################################

def es_numerico(numero):

  if type(numero)!= str or numero == "":
    return False
  else:

    indice = 0
    lista_numeros = "0123456789"


    while indice < len(lista_numeros):

      if numero == "":
        return True

      elif numero[0] ==  lista_numeros[indice]:
        indice = 0
        numero = numero[1:]
      else:
        indice += 1
    return False

#####################################################################################################


def empezar_juego(ancho_tablero,alto_tablero):

  tablero = crear_tablero(ancho_tablero,alto_tablero)
  tablero = insertar_eventos_p_n(tablero)
  cantidad_colectivos = pedir_cantidad_colectivos(ancho_tablero)
  print("\n") 
  coleccion_colectivos = crear_colectivos(cantidad_colectivos)
  tablero = insertar_colectivos(tablero, coleccion_colectivos)
  print()
  print("\t", "######################  EMPIEZA LA PARTIDA  ######################")
  print("\t", "######################   TABLERO INICIAL    ######################")
  print()
  print("\t", "# LOS COLECTIVOS HAN INGRESADO AL TABLERO #")
  print()
  imprimir_tablero(tablero)
  contador_rondas = 1
  while juego_continua == True:

    print("\n")
    print("\t", "######################  COMIENZA EL TURNO DE LOS FASCISTAS 😡  ######################")
    print("\n")
    tablero = mover_colectivos(tablero,encontrar_posicion_colectivo(tablero,cantidad_colectivos,0),encontrar_posicion_colectivo(tablero,cantidad_colectivos,0),
                               encontrar_posicion_colectivo(tablero,cantidad_colectivos,1), encontrar_posicion_colectivo(tablero,cantidad_colectivos,1))
    print("\n")
    print("\t", "######################  TERMINO EL TURNO DE LOS FASCISTAS 😡 ######################")
    print("\n")
    imprimir_tablero(tablero)
    print("\n")
    print("\t", "######################  COMIENZA EL TURNO DE LOS ANARQUISTAS 🥶  ######################")
    print("\n")
    tablero = mover_colectivos(tablero,encontrar_posicion_colectivo(tablero,cantidad_colectivos,1),encontrar_posicion_colectivo(tablero,cantidad_colectivos,1),
                               encontrar_posicion_colectivo(tablero,cantidad_colectivos,0), encontrar_posicion_colectivo(tablero,cantidad_colectivos,0))
    print("\n")
    print("\t", "######################  TERMINA EL TURNO DE LOS ANARQUISTAS 🥶  ######################")
    print("\n")
    print("\t", "—————————————————— FIN DE LA RONDA", contador_rondas,"——————————————————")
    print("\n")
    contador_rondas += 1
    imprimir_tablero(tablero)
  else:
    return terminar_juego(tablero)



#####################################################################################################


def terminar_juego(tablero):
  print("\n")
  print("\t", "EL JUEGO HA TERMINADO")
  print("\t", "EL BANDO GANADOR HA SIDO", tablero[0][len(tablero[0]) -1][0])
  print("\t", "EL COLECTIVO", tablero[0][len(tablero[0]) -1], "HA LLEGADO A LA META")
  print("\n")
  imprimir_tablero(tablero)
  


  exit()

#####################################################################################################


def pedir_cantidad_colectivos(ancho_tablero):

  cantidad_colectivos = input("Indique la cantidad de colectivos totales (Se dividira entre Fascistas y Anarquistas): ")
  
  if es_numerico(cantidad_colectivos) == False:
    print()
    print("Debe ingresar una cantidad valida de colectivos")
    print()
    return pedir_cantidad_colectivos(ancho_tablero)
  
  if int(cantidad_colectivos) > int(ancho_tablero):
    print()
    print("La cantidad de colectivos debe ser como máximo el ancho del tablero")
    print()


    return pedir_cantidad_colectivos(ancho_tablero)
  if int(cantidad_colectivos) %2 != 0 or int(cantidad_colectivos) <= 0:
    print()
    print("La cantidad de colectivos debe ser un número par positivo, para poder tener la misma cantidad de ambos bandos")
    print()
    return pedir_cantidad_colectivos(ancho_tablero)
  else:
    return int(cantidad_colectivos)
  

#####################################################################################################

def crear_colectivos(cantidad_colectivos):

  if type(cantidad_colectivos) != int:
    return "E100"
  
  colectivos_creados = 0
  coleccion_colectivos = []
  while colectivos_creados < cantidad_colectivos:
    
    if colectivos_creados %2 == 0:  #Este if crea colectivos fascistas
      nuevo_colectivo = ["F",colectivos_creados]
      coleccion_colectivos += [nuevo_colectivo]
      colectivos_creados +=1 
    else:
      #Este if crea colectivos anarquistas
      nuevo_colectivo = ["A",colectivos_creados ]
      coleccion_colectivos += [nuevo_colectivo]
      colectivos_creados +=1 
    
  return coleccion_colectivos



#####################################################################################################

def crear_tablero(ancho_tablero,alto_tablero):

  if type(ancho_tablero)!= int or type(alto_tablero)!= int:
    print()
    print("Debe ingresar cantidad valida. E10")
    print()
    return intro_juego()
  
  cantidad_filas = 0
  cantidad_celdas = 0
  matriz_resultado = []

  while cantidad_filas < alto_tablero:
    nueva_fila = []

    while cantidad_celdas < ancho_tablero:

      nueva_fila = nueva_fila + [" "]
      cantidad_celdas += 1

    matriz_resultado = matriz_resultado + [nueva_fila]
    cantidad_celdas = 0
    cantidad_filas += 1



  return matriz_resultado

#####################################################################################################


def insertar_colectivos(tablero, coleccion_colectivos ):

  if type(tablero)!= list or type(coleccion_colectivos)!= list:
    return "E050"
  

  rondas_dados = 0
  lista_dados_repetidos = []
  
  while rondas_dados < len(coleccion_colectivos):
   
    if rondas_dados %2 == 0:
      dado_inicial = random.randrange(0,len(tablero[0]),2)

      while verificar_dados_repetidos(dado_inicial, lista_dados_repetidos) == False:
        dado_inicial = random.randrange(0,len(tablero[0]) ,2)

      tablero[len(tablero)-1][dado_inicial] = coleccion_colectivos[rondas_dados]
      rondas_dados += 1
      lista_dados_repetidos = lista_dados_repetidos + [dado_inicial]


    else:

      dado_inicial = random.randrange(1,len(tablero[0]) ,2 )

      while verificar_dados_repetidos(dado_inicial, lista_dados_repetidos) == False:
        dado_inicial = random.randrange(1,len(tablero[0]),2)

      tablero[len(tablero)-1][dado_inicial] = coleccion_colectivos[rondas_dados]

      rondas_dados += 1
      lista_dados_repetidos = lista_dados_repetidos + [dado_inicial]

  return tablero 
#####################################################################################################

def verificar_dados_repetidos(dado,lista_dados_vistos):
  
  if type(dado)!= int or type(lista_dados_vistos)!= list:
    return "E150"
  indice = 0

  while indice < len(lista_dados_vistos):

    if dado == lista_dados_vistos[indice]:
      return False
    indice+=1

  return True

#####################################################################################################

def imprimir_tablero(tablero):


  largo_filas = len(tablero)
  largo_columnas= len(tablero[0])
  fila = 0
  columna = 0

  while fila < largo_filas:

    print("=====" * largo_columnas , end=" ")
    print()

    while columna < largo_columnas:
      print("|", tablero[fila][columna], end=" |")
      columna += 1


    print()
    fila += 1 
    columna =0
  print("=====" * largo_columnas , end=" ")
  return print()


#####################################################################################################

def encontrar_posicion_colectivo(tablero,cantidad_colectivos,turno):
  """
  Verificaciones
  """

  posicion_fila = 0
  posicion_columna = 0

  if turno == 0:
    colectivo_fascista_activo = random.randrange(0,cantidad_colectivos,2)

    while posicion_fila < len(tablero):
     
      while posicion_columna< len(tablero[0]):
        if tablero[posicion_fila][posicion_columna][0] != " ":
          if colectivo_fascista_activo == tablero[posicion_fila][posicion_columna][1]:
            posicion = [posicion_fila,posicion_columna]
            return posicion
          
        posicion_columna += 1
      
      posicion_fila += 1
      posicion_columna = 0

  if turno == 1:
    colectivo_anarquista_activo = random.randrange(1,cantidad_colectivos,2)

    while posicion_fila < len(tablero):

      while posicion_columna< len(tablero[0]):
        if tablero[posicion_fila][posicion_columna][0] != " ":
          if colectivo_anarquista_activo == tablero[posicion_fila][posicion_columna][1]:
            posicion = [posicion_fila,posicion_columna]
            return posicion
          
        posicion_columna += 1
      
      posicion_fila += 1
      posicion_columna = 0

#####################################################################################################

def tirar_dados():

  dado1_casillas = random.randint(1,4)
  dado2_cantidad_proyecto = random.randint(1,4)
  dado3_exito_proyectos = random.randint(1,4)

  if dado3_exito_proyectos %2 != 0:
  
    print("\t","# EL COLECTIVO HA DESARROLLADO", dado2_cantidad_proyecto, "PROYECTOS CON EXITO #")
    print("\t","# AVANZA", dado2_cantidad_proyecto, "CASILLAS ADICIONALES #")
    dado1_casillas = dado1_casillas + dado2_cantidad_proyecto
  
  else:
    print("\t", "# EL COLECTIVO HA FALLADO EN LA EJECUCIÓN DE SUS PROYECTOS #")
  cantidad_casillas = dado1_casillas

  return cantidad_casillas 


#####################################################################################################


def mover_colectivos(tablero,posicion_colectivo,posicion_antigua,posicion_colectivo2,posicion_antigua2):

  cantidad_casillas = tirar_dados()
  nuevo_tablero = avanzar_colectivos(cantidad_casillas,tablero,posicion_colectivo,posicion_antigua)
  tablero = retroceder_colectivos(cantidad_casillas,nuevo_tablero,posicion_colectivo2,posicion_antigua2)
  imprimir_tablero(tablero)
  return tablero


#####################################################################################################


def retroceder_colectivos(cantidad_casillas,tablero,posicion_colectivo,posicion_antigua):

  antigua_posicion = posicion_antigua
  posicion = posicion_colectivo 

  print("\t", "# EL COLECTIVO", tablero[antigua_posicion[0]][antigua_posicion[1]], "RETROCEDE", cantidad_casillas, "CASILLAS #")

  while cantidad_casillas > 0:

    if posicion[0] == len(tablero) -1 and posicion[1] == 0:
      print("\n")
      print("\t", "# EL COLECTIVO", tablero[antigua_posicion[0]][antigua_posicion[1]], "SE HA DEVUELTO HASTA EL INICIO DEL TABLERO #")  
      print("\n")
      cantidad_casillas = 0


    
    if posicion[1] == 0 and cantidad_casillas != 0:
      cantidad_casillas -=1
      posicion[0] = posicion[0] +1
      posicion[1] = len(tablero[0]) -1

    if cantidad_casillas != 0:
      cantidad_casillas -=1
      posicion[1] = posicion[1] - 1


  if tablero[posicion[0]][posicion[1]] != " " and tablero[posicion[0]][posicion[1]][1] == "P": 
    print("\t", "# EL COLECTIVO", tablero[antigua_posicion[0]][antigua_posicion[1]], "HA CAIDO EN UN EVENTO POSITIVO #")
    dado_evento = random.randint(1,4)
    return avanzar_colectivos(dado_evento,tablero,posicion,antigua_posicion)

  elif tablero[posicion[0]][posicion[1]] != " " and tablero[posicion[0]][posicion[1]][1] == "N": 
    print("\t", "# EL COLECTIVO", tablero[antigua_posicion[0]][antigua_posicion[1]], "HA CAIDO EN UN EVENTO NEGATIVO #")
    dado_evento = random.randint(1,4)
    return retroceder_colectivos(dado_evento,tablero,posicion,antigua_posicion)

  if detectar_colision_colectivos(tablero,posicion) == True:
      if evento_colision_colectivos() == True:  

        print("\t", "# LOS DEFENSORES HAN GANADO EL CHOQUE DE COLECTIVOS - EL COLECTIVO DEFENSOR SE ADELANTA HASTA LA POSICION ORIGINAL DEL ATACANTE #")
        print("\n")
        tablero = intercambio_posicion_defensor(posicion,antigua_posicion,tablero)
        return tablero
      else:
        print("\n")
        print("\t", "# LOS DEFENSORES HAN PERDIDO EL CHOQUE DE COLECTIVOS - LOS ATACANTES NO RETROCEDEN SU POSICION Y LOS DEFENSORES NO AVANZAN #")
        print("\n")
        return tablero

  else:  
 
    tablero[posicion[0]][posicion[1]] = tablero[antigua_posicion[0]][antigua_posicion[1]]
    tablero[antigua_posicion[0]][antigua_posicion[1]] = " "

  return tablero

#####################################################################################################

def intercambio_posicion_defensor(posicion,posicion_antigua,tablero):

  temp = tablero[posicion_antigua[0]][posicion_antigua[1]]
  tablero[posicion_antigua[0]][posicion_antigua[1]] = tablero[posicion[0]][posicion[1]]
  tablero[posicion[0]][posicion[1]] = temp

  return tablero

#####################################################################################################

def evento_colision_colectivos():

  
  colectivo_activo_gana = random.randint(1,4)
  
  if colectivo_activo_gana == 1:
    return True
  else:
    return False
  
#####################################################################################################

def detectar_colision_colectivos(tablero,posicion_actual):
  
  if tablero[posicion_actual[0]][posicion_actual[1]] != " ":
    print("\n")
    print("\t", "###########################################################################################")
    print("\t", "# OH NO, HUBO UN CHOQUE DE COLECTIVOS EN LA FILA", posicion_actual[0]+1, "CASILLA",posicion_actual[1] +1, "#")
    print("\t", "###########################################################################################")
    print("\n")
    return True
  else:
    return False

#####################################################################################################

def avanzar_colectivos(cantidad_casillas,tablero,posicion_colectivo,posicion_antigua):

  antigua_posicion = posicion_antigua
  posicion = posicion_colectivo  

  print("\t","# EL COLECTIVO", tablero[antigua_posicion[0]][antigua_posicion[1]], "AVANZA", cantidad_casillas, "CASILLAS #")


  while cantidad_casillas > 0:
  

    if posicion[0] == 0 and posicion[1] == len(tablero[0]) -1:
      cantidad_casillas = 0
      print("\n")
      print("\t", "# EL COLECTIVO", tablero[antigua_posicion[0]][antigua_posicion[1]], "AVANZA HASTA LA META #")
      print("\n")

      tablero[posicion[0]][posicion[1]] = tablero[antigua_posicion[0]][antigua_posicion[1]]
      tablero[antigua_posicion[0]][antigua_posicion[1]] = " "
      terminar_juego(tablero)
      

    
    if posicion[1] == len(tablero[0]) -1 and cantidad_casillas != 0:
      cantidad_casillas -=1
      posicion[0] = posicion[0] - 1
      posicion[1] = 0

    else:
      cantidad_casillas -=1
      posicion[1] = posicion[1] + 1

  if tablero[posicion[0]][posicion[1]] != " " and tablero[posicion[0]][posicion[1]][1] == "P": 
    print("\t","# EL COLECTIVO", tablero[antigua_posicion[0]][antigua_posicion[1]], "HA CAIDO EN UN EVENTO POSITIVO #")
    dado_evento = random.randint(1,4)
    return avanzar_colectivos(dado_evento,tablero,posicion,antigua_posicion)

  elif tablero[posicion[0]][posicion[1]] != " " and tablero[posicion[0]][posicion[1]][1] == "N": 
    print("\t","# EL COLECTIVO", tablero[antigua_posicion[0]][antigua_posicion[1]], "HA CAIDO EN UN EVENTO NEGATIVO #")
    dado_evento = random.randint(1,4)
    return retroceder_colectivos(dado_evento,tablero,posicion,antigua_posicion)

  
  if detectar_colision_colectivos(tablero,posicion) == True:
      if evento_colision_colectivos() == True:  
   
        print("\t", "# LOS ATACANTES HAN GANADO EL CHOQUE DE COLECTIVOS - LOS DEFENSORES SE RETRASAN HASTA LA POSICION ORIGINAL DEL ATACANTE #")
        print("\n")
        tablero = intercambio_posicion_atacante(posicion,antigua_posicion,tablero)
        return tablero
      else:
        print("\n")
        print("\t", "# LOS ATACANTES HAN PERDIDO EL CHOQUE DE COLECTIVOS - LOS DEFENSORES MANTIENEN SU POSICION Y LOS ATACANTES NO AVANZAN #")
        print("\n")
        return tablero
  
  else:
    tablero[posicion[0]][posicion[1]] = tablero[antigua_posicion[0]][antigua_posicion[1]]
    tablero[antigua_posicion[0]][antigua_posicion[1]] = " "


  return tablero
  
#####################################################################################################


def intercambio_posicion_atacante(posicion,antigua_posicion,tablero):

  temp = tablero[antigua_posicion[0]][antigua_posicion[1]]
  tablero[antigua_posicion[0]][antigua_posicion[1]] = tablero[posicion[0]][posicion[1]]
  tablero[posicion[0]][posicion[1]] = temp

  return tablero

#####################################################################################################

def insertar_eventos_p_n(tablero):

  if type(tablero)!= list:
    return "El tablero debe ser una lista E180" 
  

  fila = 0
  columna = 0

  largo_fila = len(tablero) - 1
  largo_columna = len(tablero[0]) -1 

  while fila < largo_fila:

    while columna < largo_columna:

      posibilidad_evento = random.randint(1,7)

      if posibilidad_evento  == 1:
        tablero[fila][columna] = ["P", "P"]
      
      
      elif posibilidad_evento == 5:
        tablero[fila][columna] = ["N", "N"]
      columna +=1
    fila +=1
    columna = 0

  return tablero







#####################################################################################################

if __name__ == "__main__":
    intro_juego()






"""
ANOTACIONES

  24/05/2025 - Debo añadir una funcion en crear colectivos fascitas y anarquistas, para que la cantidad maxima sea proporcional a las dimensiones del tablero, por ahora solo establecere maximo 5, minimo 2
  
  24/05/2025 - Debo arreglar que al tirar el dado inicial, para decidir la posicion de los colectivos, los colectivos puedan caer en el mismo lugar, y que si eso pasa, se suporponen

  24/05/2025 - Debo cambiar a la hora de asignar una posicion a los colectivos, que sea por pares/impares, sino que la posicion donde se asignen, se vaya añadiendo a una lista de 
  posiciones usadas, y while  posicion de un colectivo == lista_posiciones_usadas[indice], que vuelva a tirar el dado por una nueva posicion 

  25/05/2025 - Tengo que manejar el evento de que cuando una comunidad avance en una casilla, hacia otra casilla donde ya hay otra comunidad, crear un choque entre las comunidades
  si son colectivos opuestos, y hacer algo si son del mismo bando, para que no se sobreescriban las comunidades

  25/05/2025 - Tengo que cambiar la funcion de encontrar posicion de un colectivo, para que en vez de la posicion en [4,1], me devuelva la posicion actual y la posicion antigua en una 
  sola lista, para no tener que pasarte 4 funciones iguales a la funcion mover_colectivos, tal que quede
  TAMBIEN PUEDO SOLAMENTE LLAMAR A LAS FUNCIONES DENTRO DE LA PROPIA FUNCION MOVER COLECTIVOS, Y OBTENER AHI LAS POSICIONES
  [[4,1],[4,1]]
  y vaya cambiando
  [[4,2],[4,1]]
  [[4,3],[4,1]]
  [[4,4],[4,1]]
  [[3,0],[4,1]]
  [[3,1],[4,1]] etc
  prueeeeba
"""
