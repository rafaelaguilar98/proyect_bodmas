import random as r
import os
file_name = 'user_scores.txt'
temporary_file_name = "userScores.tmp"

def getUserPoint(user_name):
    try:
        score_file = open(file_name, 'r')
        for info in score_file:
            separeted_score = info.split(',')
            if separeted_score[0] == user_name:
                score_file.close()
                return separeted_score[1]
        score_file.close()
        return "-1"
    except IOError:
        print("\nEl archivo no existe, se creará uno nuevo")
        score_file = open(file_name, 'w')
        score_file.close()
        return "-1"

def updateUsersPoints(new_user, user_name, score):
    try:
        register = "\n"+user_name + "," + str(score)
        if new_user == True:
            file_score = open(file_name, 'a')
            file_score.write(register)
            file_score.close()
        else:
            temp_file = open(temporary_file_name, 'w')
            file_score = open(file_name, 'r')
            for line in file_score:
                separeted = line.split(',')
                if separeted[0] == user_name:
                    register = user_name + "," + str(score) + "\n"
                    temp_file.write(register)
                else:
                    temp_file.write(line)
            temp_file.close()
            file_score.close()
            os.remove(file_name)
            os.rename(temporary_file_name, file_name) 
        #return("Score actualizado correctamente")
    except Exception as e:
        print("Error al actualizar score", e)

def generateQuestion():
    operand_list = []
    operator_list = []
    operator_dic ={1:"+", 2:"-", 3:"**", 4:"*"}
    question_string = ""

    #Fill the operand_list array
    for i in range(0,5):
        operand_list.append(r.randint(1,9))

    #Fill the operator_list array
    for i in range(0,4):
        operator = operator_dic[r.randint(1,4)]
        if len(operator_list)!=0 and operator == "**":
            if operator_list[-1] == "**":
                operator = operator_dic[r.randint(1,4)]
        operator_list.append(operator)

    #Concatenate the "operator" and the "operand" arrays
    for i in range(len(operator_list)):
        question_string += str(operand_list[i]) + operator_list[i]
    '''
        Add the last element of the array because the iteratation before is for the 4 operators and 4 numbers 
        but we need the 5 numbers and we need to add the last number at the end of the string

    '''
    question_string += str(operand_list[-1])
    '''
        eval is for "transform" the string expression and evaluated as a mathematical expression. 
        Gives the result of the expression (e.g: eval(2+3+2) returns 7)
    '''
    result = eval(question_string)
    question_string = question_string.replace("**", "^")

    #Interaction with the user
    user_answer = input("¿Cuál es el resultado de la siguiente operación?: "+question_string+" ")
    while True:
        try:
            
            if int(user_answer) == result:
                print("Correcto, tienes un punto")
                return 1
            else:
                print("Casi, pero te faltó un poco :(, intenta de nuevo :D, la respuesta correcta es: "+str(result))
                return 0
        except Exception as e:
            print("Ocurrió el siguiente error: ",e)
            user_answer = input("¿Cuál es el resultado de la siguiente operación?: "+ question_string+" ")

if __name__ == "__main__":
    generateQuestion()