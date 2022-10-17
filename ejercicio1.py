import random
contador=1
while True:
  niveles=int(input("¿Qué dificultad quieres jugar del 1 al 4?"))
  if niveles > (4):
    print("Todavía no hemos desarollado ese nivel")
  if niveles == (1): #nivel1
    num1=random.randint(0,100)
    while True:
      intento=int(input("Adivina un número entre el 1 y el 100:"))
      if intento == num1:
        print("Enhorabuena has adivinado el número")
        nombre_usuario= input("Introduzca su usuario:")
        print(nombre_usuario,contador,"intentos")
        break
        contador=contador+1
      elif intento < num1:
        print("El número que buscas es mayor")
        contador=contador+1
      elif intento > num1:
        print("El número que buscas es menor")
        contador=contador+1
      if contador >= 6:
        print("Derrota has superado el límite de intentos")
        break
  elif niveles == (2): #nivel2
    num2=random.randint(0,1000)
    while True:
      intento=int(input("Adivina un número entre el 1 y el 1000:"))
      if intento == num2:
        print("Enhorabuena has adivinado el número")
        nombre_usuario= input("Introduzca su usuario:")
        print(nombre_usuario,contador,"intentos")
        break
        contador=contador+1
      elif intento < num2:
        print("El número que buscas es mayor")
        contador=contador+1
      elif intento > num2:
        print("El número que buscas es menor")
        contador=contador+1
      if contador >= 12:
        print("Derrota has superado el límite de intentos")
        break
  elif niveles == (3): #nivel3
    num3=random.randint(0,1000000)
    while True:
      intento=int(input("Adivina un número entre el 1 y el 1000000:"))
      if intento == num3:
        print("Enhorabuena has adivinado el número")
        nombre_usuario= input("Introduzca su usuario:")
        print(nombre_usuario,contador,"intentos")
        break
        contador=contador+1
      elif intento < num3:
        print("El número que buscas es mayor")
        contador=contador+1
      elif intento > num3:
        print("El número que buscas es menor")
        contador=contador+1
      if contador >= 24:
        print("Derrota has superado el límite de intentos")
        break
  elif niveles == (4): #nivel4
    num4=random.randint(0,1000000000000)
    while True:
      intento=int(input("Adivina un número entre el 1 y el 1000000000000:"))
      if intento == num4:
        print("Enhorabuena has adivinado el número")
        nombre_usuario= input("Introduzca su usuario:")
        print(nombre_usuario,contador,"intentos")
        break
        contador=contador+1
      elif intento < num4:
        print("El número que buscas es mayor")
        contador=contador+1
      elif intento > num4:
        print("El número que buscas es menor")
        contador=contador+1
      if contador >= 40:
        print("Derrota has superado el límite de intentos")
        break
  
  break
