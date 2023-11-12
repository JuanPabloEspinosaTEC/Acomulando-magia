while True:
  counter = 0
  text = input("")
  x = text.split()
  for y in x:
    if y == "alexa":
      counter += 1
  if counter > 1:
    print("Solo tienes que decir mi nombre una vez")
  elif counter > 0:
    print("En que te puedo ayudar")
