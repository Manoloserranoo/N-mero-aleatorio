import random
numero=random.randint(0,100)
while True:
  intento=int(input("Introduzca un número:"))
  if intento == numero:
    print("Enhorabuena has adivinado el número")
    break
  elif intento < numero:
    print("El número que buscas es mayor")
  elif intento > numero:
    print("El número que buscas es menor")
  