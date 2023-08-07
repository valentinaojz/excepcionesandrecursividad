fruits = ["banana","apple","stawberry","watermelon","pinapple"]
while True:
  user_option = input("ingrese una opción, q para salir\n")

  if user_option == "q":
   break
  try:
    print(fruits[int(user_option)])
  except ValueError as valueerror: #as me deja el mensaje del error original 
    print("ingresa un número, no letras.", valueerror)  
  except IndexError:
    print("ingresa un número de 0 al 4")  
  

