#la recursividad es la función llamandose a si misma dentro del cuerpo de la función.
def countdown (num):
    if num == 0: #condición de salida 
        print("ka-booom")
    else:
        print(num)
        countdown(num - 1)    
countdown(5)

#todo lo que se puede resolver con recursión se puede resolver de otras maneras pero no todos los problemas  se puede resolver con recursión. 

#countdown2 
print("----------------------------------------------------")

def countdown2 (num):
    for number in range (-num,1):
        if number == 0:
            print("ka-boom")
        else:
            print(-number)
countdown2(5)         

print("-----------------------------------------------------")
#countdown3 
def countdown3 (num):
    for numbers in range(-num,0):
        print(-numbers)
    print("ka-boom") 
countdown3(6)  
   
print("--------------------------------------------------")

def infinite_recursion(word):
    print(word)
    infinite_recursion(word)
infinite_recursion("palabra")