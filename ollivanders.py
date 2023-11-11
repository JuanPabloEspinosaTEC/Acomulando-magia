total = 0
compras = 0
sauco = 0
espino = 0
sauce = 0
acebo = 0
A1 = input("hay algun cliente? si/no: ")
while A1 == "si":
  total += 1
  A2 = input("el cliente compro? si/no: ")
  while A2 == "si":
    compras +=1
    print("1. Varita de Saúco, 2. Varita de Espino, 3. Varita de Sauce y 4. Varita de Acebo.")
    A3 = int(input("Que varita va a comprar? 1, 2, 3 o 4"))
    if A3 == 1:
      sauco += 1
    elif A3 == 2:
      espino += 1
    elif A3 == 3: 
      sauce += 1
    elif A3 == 4:
      acebo += 1
    A2 = "no"
  A1 = input("hay aulgun cliente si/no: ")
print("Clientes totales " + str(total))
print("Hubo un total de " + str(compras) + " ventas")
print("Se vendieron " + str(sauco) + " varitas de sauco, " + str(espino) + " varitas de espino, ")
print(str(sauce) + " varitas de sauce, " + str(acebo) + " varitas de acebo ")
print("Que buen dia en harry potter")
