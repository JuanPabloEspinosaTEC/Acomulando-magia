num = int(input("Cuantas lecturas dio el sensor: "))
cont = 1
cnt = 0
while num + 1 > cont:
  x = float(input("Cual es la " + str(cont) + " lectura?: "))
  if x >= 10 and x <= 40:
    cnt += 1
  cont += 1
print("Hubo " + str(cnt) + " lectura correcta")
print("el rango de error es del " + str((1 - (float(cnt) / float(num))) * 100) + "% ")
