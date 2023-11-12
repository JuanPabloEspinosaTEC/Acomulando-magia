def event(ev):
  points = 0
  if ev == "goal":
    points = 10
  elif ev == "snitch":
    points = 150
  elif ev == "foul":
    points = -30
  else:
    print("Ese evento no existe")
  return points

slS = 0
gRS = 0
num = int(input("Ingresa el número de eventos en el partido de Quidditch: "))
while num > 0:
  point = event(input("Ingresa un evento (goal/snitch/foul): "))
  team = input("¿Qué equipo anotó (Gryffindor o Slytherin): ")
  if team == "Gryffindor":
    gRS += point
  elif team == "Slytherin":
    slS += point
  else:
    print("Ese equipo no existe")
    
  num -= 1

print("Gryffindor: " + str(gRS) + " puntos")
print("Slytherin: " + str(slS) + " puntos")
if gRS > slS:
  print("Fryffindor gana!!!")
elif gRS == slS:
  print("Es un empate")
else:
  print("Slytherin gana!!!")
