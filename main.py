import time
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Colores
verde = "\033[32m"
rojo = "\033[31m"
azul = "\033[34m"
amarillo = "\033[33m"
reset = "\033[39m"

# Parametros

Npreg = 10 # Numero de preguntas maximo
Descuento = 10 # Descuento por error
Aumento = 10 # Aumento por acierto
puntaje_inicial = 50

# Tiempos, Puntaje,operacion y nivel de dificultad
Tiempos = []
ListaPuntos = []
ListaOperacion = []
ListaNivel = []
# Funcion de resumen de intentos
def resumen(ListaPuntos, user_name):
  print(rojo+'RESUMEN DE PUNTAJE:'+reset)
  print("Usuario: ", verde+user_name+reset)
  for el in enumerate(ListaPuntos):
    if el[1]=='Perdió':
      print("Intento ",el[0]+1, " (",ListaOperacion[el[0]]," y nivel ",ListaNivel[el[0]],"): ", el[1], " en ", '%.2f' % Tiempos[el[0]], " segundo(s)")
    else:
      print("Intento ",el[0]+1, " (",ListaOperacion[el[0]]," y nivel ",ListaNivel[el[0]],"): ", el[1], " puntos en ", '%.2f' % Tiempos[el[0]], " segundo(s)")
# Diccionarios con la correspondencia entre letras y opciones

dic_topicos = {'a':'Suma', 'b': 'Multiplicación', 'c': 'División'}
dic_nivel = {'a': 1, 'b': 2, 'c': 3}
dic_dificultad = {'a': 'Fácil', 'b': 'Medio', 'c': 'Difícil'}
dic_operacion = {'a': '+', 'b': 'x', 'c': '÷'}

# Funcion de cierre
def cierre(ListaPuntos, user_name):
  cerrar = input("¿Desea cerrar la trivia?: ").lower()
  # Validacion ####################################
  while cerrar not in ['si', 'no']:
    cerrar = input("Responda con 'SI' o 'NO': ").lower()
  #################################################
  if cerrar == 'si':
    print("\n")
    # Queremos saber si esta seguro
    EstaSeguro = input("Si cierra la trivia se perderá el progreso del usuario se perderá ¿está seguro?: ").lower()
    # Validacion ####################################
    while EstaSeguro not in ['si', 'no']:
      EstaSeguro = input("Responda con 'SI' o 'NO': ").lower()
    #################################################
      
    if EstaSeguro == 'si':
      resumen(ListaPuntos, user_name) # Si esta seguro le damos el resumen de           sus intentos
    else:
      cierre(ListaPuntos, user_name)
  else:
    DeNuevo = input("¿Le gustaría volver a hacer la trivia?: ").lower()
    # Validacion ####################################
    while DeNuevo not in ['si', 'no']:
      DeNuevo = input("Responda con 'SI' o 'NO': ").lower()
    #################################################
      
    if DeNuevo == 'si':
      Empezar_trivia()
    else:
      # Vuelve a ejecutar la funcion ya que dijo que le gustaria volver a hacer        # la trivia
      cierre(ListaPuntos, user_name)

# Funcion de validacion de formato de respuesta:


def Respuesta_Validacion(respuesta):
  respuesta=respuesta.replace(',','.')
  flag = False
  
  if respuesta in ['a', 'b', 'c']:
    flag = False
  else:
    try:
      float(respuesta)
    except:
      flag = True
    
  return flag
    


# Funciones con las preguntas:

def Preguntas(nivel, n, topico):
  
  li = 10**(dic_nivel[nivel]-1)# limite inferior
  ls = 10**(dic_nivel[nivel])# limite superior
  
  x = random.randint(li,ls)
  y = random.randint(li,ls)

  # De acuerdo al tipo de operacion generamos las alternativas
  if dic_topicos[topico] == 'Suma':
    # Color de operacion:
    color = rojo
    # Alternativa correcta y errores 
    respuesta_correcta = x+y # La respuesta correcta
    
    # Tratamos de obtener numeros cercanos a la respuesta correcta
    error_1 = respuesta_correcta + random.randint(li,int(ls/2))
    error_2 = int(respuesta_correcta - respuesta_correcta*random.randint(2,ls)**(-1))
    # Cambiamos el ultimo digito si el nivel es medio o dificil:
    if (nivel == 'b') or (nivel == 'c'):
      # La siguiente operacion hace que los ultimos digitos de todas
      # las alternativas coincidan
      error_1 = error_1 - error_1%10 + respuesta_correcta%10
      error_2 = error_2 - error_2%10 + respuesta_correcta%10
      
      # Corregimos si son iguales a respuesta_correcta
      if error_1 == respuesta_correcta:
        error_1 = error_1 - random.randint(1,2)*10**(dic_nivel[nivel]-1)
        error_1 = int(error_1) # a entero
      if error_2 == respuesta_correcta:
        error_2 = error_2 + random.randint(1,2)*10**(dic_nivel[nivel]-1)
        error_2 = int(error_2) # a entero
        
    # Agrupamos las alternativas en una lista
    listaAlternativas = [respuesta_correcta, error_1, error_2]
  
  elif dic_topicos[topico] == 'Multiplicación':
  # Color de operacion:
    color = azul
  # Alternativa correcta y errores 
    respuesta_correcta = x*y # La respuesta correcta
    
  # Tratamos de obtener numeros cercanos a la respuesta correcta
    error_1 = x*(y + random.randint(1,5))
    error_2 =int((x*y)*random.randint(7,9)/10)
  # Cambiamos el ultimo digito si el nivel es medio o dificil:
    if (nivel == 'b') or (nivel == 'c'):
      # La siguiente operacion hace que los ultimos digitos de todas
      # las alternativas coincidan
      error_1 = error_1 - error_1%10 + respuesta_correcta%10
      error_2 = error_2 - error_2%10 + respuesta_correcta%10

      # Corregimos si son iguales a respuesta_correcta
      if error_1 == respuesta_correcta:
        error_1 = error_1 - random.randint(1,2)*10**(dic_nivel[nivel]-1)
        error_1 = int(error_1)
      if error_2 == respuesta_correcta:
        error_2 = error_2 + random.randint(1,2)*10**(dic_nivel[nivel]-1)
        error_2 = int(error_2)
    # Agrupamos las alternativas en una lista
    listaAlternativas = [respuesta_correcta, error_1, error_2]

  else: # Division
    # Corresponde a division
    
    # Color de operacion:
    color = amarillo
    # Alternativa correcta y errores
    # x = random.randint(li,ls)
    y = random.randint(li+1,ls) 
    
    # La respuesta correcta es un entero aleatorio y es solucion de dividir
    # -> y*respuesta_correcta/y
    respuesta_correcta = random.randint(2,ls) 
    
    # Tratamos de obtener numeros cercanos a la respuesta correcta
    error_1 = respuesta_correcta + random.randint(li,int(ls/2))
    error_2 = int(respuesta_correcta - respuesta_correcta*random.randint(2,ls)**(-1))
  
    listaAlternativas = [respuesta_correcta, error_1, error_2]


  # Ordenamos aleatoriamente las alternativas
  random.shuffle(listaAlternativas)
  # Claves
  listaClaves = ['a', 'b', 'c']
  
  # Guardamos la alternativa de la respuesta correcta:
  ind = listaAlternativas.index(respuesta_correcta)
  Alternativa_correcta = listaClaves[ind]
  
  # Pregunta:
  if dic_topicos[topico]=='División':
    
    numerador = respuesta_correcta*y
    denominador = y
    # Print de pregunta y alternativas para division
    print("Pregunta ",n,":\n")
    print("¿Cuál es el valor de ", numerador, color+dic_operacion[topico]+reset, denominador,"?\n")
    # Alternativas
    for enu in enumerate(listaAlternativas):
        print(listaClaves[enu[0]],") ",enu[1],"\n")
  else:
    # Print de pregunta y alternativas para multiplicacion y suma
    print("Pregunta ",n,":\n")
    print("¿Cuál es el valor de ", str(x), color+dic_operacion[topico]+reset, str(y),"?\n")
    # Alternativas
    for enu in enumerate(listaAlternativas):
        print(listaClaves[enu[0]],") ",enu[1],"\n")

  # La respuesta dada
  respuesta = input("Ingrese el número resultante o la alternativa de su respuesta: ").lower()
  # Validacion
  Vflag = Respuesta_Validacion(respuesta)
  while Vflag:
    respuesta = input("Solo se aceptan números o alguna de las alternativas (a, b o c): ").lower()
    Vflag = Respuesta_Validacion(respuesta)
 

  # Cambiamos respuesta de acuerdo a si es alternativa o numero y
  # hacemos print del resultado
    
  if respuesta in listaClaves:
    
    if respuesta == Alternativa_correcta:
      print(verde+"¡Correcto! Tienes 10 puntos más\n"+reset)
      EsCorrecto = True
    else:
      print(rojo+"Incorrecto, se te restan 10 puntos\n"+reset)
      EsCorrecto = False
      
  else:
    respuesta=respuesta.replace(',','.')
    respuesta = float(respuesta) #Transformamos la respuesta a float
    if respuesta == respuesta_correcta:
      print(verde+"¡Correcto!\n"+reset)
      EsCorrecto = True
    else:
      print(rojo+"Incorrecto\n"+reset)
      EsCorrecto = False

  return EsCorrecto
    

  


# A partir de aca empieza la trivia:
def Empezar_trivia():
  global user_name
  PuntosAcumulados = puntaje_inicial #Puntaje
  try:
    print("¡Hola de nuevo ",verde+user_name+reset,"!")
  except:
    print("¡Bienvenido a mi trivia!")
  
    user_name = input("Escriba su nombre de usuario:\n-> ")
    while user_name == "":
      user_name = input("Debe ingresar un nombre de usuario: ")
      
  # DicUsuarios[user_name] = 
    print("¡Hola", verde+user_name+reset,"!\n")
  
  print("En esta trivia vamos a poner a prueba tu velocidad de cálculo.\n" )
  print("Usted empezará con 50 puntos. Cada pregunta errónea le restará ",Descuento, " punto(s), mientras que cada pregunta correcta le sumará ", Aumento, " punto(s). Cada intento termina cuando usted llega a 0 puntos, en cuyo caso ha perdido, o cuando responde el máximo de preguntas.\n" )
  print("Selecciona la operación que más te guste:","\n",
        "a)", rojo+"Suma"+reset,"\n",
        "b)", azul+"Multiplicación"+reset, "\n",
        "c)", amarillo+"División"+reset,"\n")
  
  topico = input("Escriba la letra que corresponde al tópico de su preferencia:\n-> ").lower()
  
  ############ Validacion #####################
  
  while topico not in ["a","b","c"]:
    topico = input("Ingrese la letra (a, b o c) que corresponde al tópico de su preferencia: \n->").lower()
    
  # Guardamos el topico u operacion elegida despues de la validacion
  ListaOperacion.append(dic_topicos[topico])
  
  #############################################
  print("Ahora selecciona el nivel de dificultad:","\n",
        "a)", verde+"Fácil"+reset,"\n",
        "b)", amarillo+"Medio"+reset, "\n",
        "c)", rojo+"Difícil"+reset,"\n")
  
  nivel = input("Escriba la letra que corresponde a la dificultad de su preferencia:\n-> ").lower()
  
  ############ Validacion #####################

  while nivel not in ["a","b","c"]:
    nivel = input("Ingrese la letra (a, b o c) que corresponde a la dificultad de su preferencia:\n-> ").lower()
    
  # Guardamos el nivel de dificultad elegido despues de la validacion
  ListaNivel.append(dic_dificultad[nivel])
  
  #############################################
  print("\n")
  if nivel == "a":
    print("¡Está bien para empezar!\n")
    time.sleep(2)
    cls()
  elif nivel == "b":
    print("¡Bien!\n")
    time.sleep(2)
    cls()
  else:
    print("Se ve que tienes agallas...\n")
    time.sleep(2)
    cls()
    
  print("Elegiste ",dic_topicos[topico], " y el nivel ", dic_dificultad[nivel],"\n")
  input("Presione enter para empezar la trivia y que el tiempo empiece a correr:")
  cls()
  tiempo_inicio = time.time()
  print("\n")
  
  i=1
  while (i <= Npreg) & (PuntosAcumulados > 0):
    # Un pequeno aviso de que si falla una vez mas perdera
    if PuntosAcumulados == 10:
      cls()
      print("Cuidado! Te quedan 10 puntos, si cometes un error más perderás\n")
      input("Presione enter para continuar")
      cls()
      
    EsCorrecto=Preguntas(nivel, i, topico)
    i += 1 # Actualizamos el numero de la pregunta
    input("Presione enter para pasar a la siguiente pregunta")
    cls()
    if EsCorrecto:
      PuntosAcumulados += Aumento
    else:
      PuntosAcumulados -= Descuento
  else:
    tiempo_final = time.time()
    Duracion = tiempo_final-tiempo_inicio
    Tiempos.append(Duracion)
    input("¡Terminó!")
    cls()
    if PuntosAcumulados <= 0:
      print("Te quedaste sin puntos, perdiste xd\n")
      resultado = "Perdió"
      ListaPuntos.append(resultado)
    else:
      print("Llegaste al límite de preguntas, obtuviste:", PuntosAcumulados, "puntos")
      resultado = PuntosAcumulados
      ListaPuntos.append(resultado)
  
  if PuntosAcumulados <= 0:
    DeseaContinuar = input("¿Le gustaría volver a intentarlo?: ").lower()
    while DeseaContinuar not in ['si', 'no']:
        DeseaContinuar = input("Responda con 'SI' o 'NO': ").lower()
        
    if DeseaContinuar=='si':
      Empezar_trivia()
    else:
      cierre(ListaPuntos, user_name)
  else:
    DeNuevo = input("¿Le gustaría volver a hacer la trivia?: ").lower()
    while DeNuevo not in ['si', 'no']:
      DeNuevo = input("Responda con 'SI' o 'NO': ").lower()
      
    if DeNuevo == 'si':
      Empezar_trivia()
    else:
      cierre(ListaPuntos, user_name)



#########################################################################
# SE EJECUTA LA TRIVIA
Empezar_trivia()
  




