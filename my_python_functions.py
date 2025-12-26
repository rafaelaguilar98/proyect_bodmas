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
        register = "\n"+user_name + "," + score
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
                    register = user_name + "," + score + "\n"
                    temp_file.write(register)
                else:
                    temp_file.write(line)
        temp_file.close()
        file_score.close()
        os.remove(file_name)
        os.rename(temporary_file_name, file_name) 
        return("Score actualizado correctamente")
    except Exception as e:
        print("Error ", e)

if __name__ == "__main__":
    print(updateUsersPoints(False, "Carol", '300'))
