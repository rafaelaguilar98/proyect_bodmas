import my_python_functions as m
try:
    user_name = input("Hola, ¿Cuál deseas que sea tu nombre de usuario? ")
    user_score = int(m.getUserPoint(user_name))
    if user_score == -1:
        new_user = True
        user_score = 0
    else:
        new_user = False

    user_choise = 0

    while user_choise !="-1":
        user_score += m.generateQuestion()
        election = input("Si no deseas continuar, escribe t, de lo contrario presiona enter ")
        if election == "t":
            user_choise = "-1"
            print("Hasta luego "+user_name)
    m.updateUsersPoints(new_user, user_name, user_score)
        
except Exception as e:
    print("Ocurrió el siguiente error: "+ e)