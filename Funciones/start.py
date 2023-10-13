import os
import time 
import random
from Funciones.questions_bank import questions_bank

def start():

    countPositive=0
    countNegative=0
    opts=[0,1,2,3]
    randoms=list(range(10))
    random.shuffle(randoms)
    for i in range(1,11):
        print("Pregunta #",i)
        q=questions_bank(randoms[i-1]) #take a randonm question from questions_bank
        random.shuffle(opts) #randomiza el indice que se utilizará en las respuestas [2,1,0,3]
        print(q["question"],"\n","A. ",q["options"][opts[0]],"\n","B. ",q["options"][opts[1]],"\n","C. ",q["options"][opts[2]],"\n","D. ",q["options"][opts[3]])
        ans=input("Ingrese la opcion de su respuesta\n")
        ans_opts={
        "A":q["options"][opts[0]],
        "B":q["options"][opts[1]],
        "C":q["options"][opts[2]],
        "D":q["options"][opts[3]]}
        if ans == "A":
            if ans_opts["A"]==q["answer"]:  
                countPositive+=1
            else:countNegative+=1
        elif ans == "B":
            if ans_opts["B"]==q["answer"]:
                countPositive+=1
            else:countNegative+=1
        elif ans == "C":
            if ans_opts["C"]==q["answer"]:
                countPositive+=1
            else:countNegative+=1
        elif ans == "D":
            if ans_opts["D"]==q["answer"]:
                countPositive+=1
            else:countNegative+=1
        else:
            pass
            

    return [countPositive,countNegative]