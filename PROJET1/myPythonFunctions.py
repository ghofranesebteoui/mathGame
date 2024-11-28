#Partie1:myPythonFunctions.py

'''
Tâche 1 :

importation des modules random (pour générer des nombres aléatoires)
et os (pour gérer des fichiers)
'''
import random
import os

'''
Tâche 2 : Obtenir le score de l'utilisateur

1-Ouvrir le fichier userScores.txt en mode lecture
2-Parcourir chaque ligne pour vérifier si le nom d’utilisateur
correspond à celui passé en paramètre
3-Si trouvé, retourner le score ; sinon, retourne -1
'''
def getUserPoint(userName):
    try:
        with open('userScores.txt', 'r') as file:
            for line in file:
                name, score = line.strip().split(", ")
                if name == userName:
                    return int(score)
        return -1
    except FileNotFoundError:
        with open('userScores.txt', 'w') as file:
            pass  # Crée un fichier vide
        return -1



'''
Tâche 3 : Mettre à jour le score de l'utilisateur 

1-Mettre à jour ou ajouter le score de l'utilisateur dans le fichier userScores.txt
    1-Si newUser est True, ajouter une nouvelle ligne avec le nom et score
    2-Si newUser est False, créer un fichier temporaire pour
      mettre à jour le score de l’utilisateur
2-Remplacer userScores.txt par le fichier temporaire avec les scores mis à jour
'''

def updateUserPoints(newUser, userName, score):
    if newUser:
        with open('userScores.txt', 'a') as file:
            file.write(f"{userName}, {score}\n")
    else:
        with open('userScores.txt', 'r') as file, open('userScores.tmp', 'w') as temp_file:
            for line in file:
                name, user_score = line.strip().split(", ")
                if name == userName:
                    temp_file.write(f"{userName}, {score}\n")
                else:
                    temp_file.write(line)
        os.remove('userScores.txt')
        os.rename('userScores.tmp', 'userScores.txt')


'''
Tâche 4 : Génération des questions 

1-Créer une liste operandList avec 5 nombres aléatoires
2-Créer une liste operatorList de 4 opérateurs mathématiques choisis au hasard,
tout en évitant des opérateurs exposants (**) consécutifs
3-Former une expression mathématique sous forme de chaîne, puis évalue-la avec eval()
4-Remplacer ** par ^ dans l'affichage pour éviter la confusion avec l'exposant Python
'''

def generateQuestion():
    operandList = [random.randint(1, 10) for _ in range(5)]
    operatorDict = {1: "+", 2: "-", 3: "*", 4: "**"}
    operatorList = []

    for _ in range(4):
        operator = operatorDict[random.randint(1, 4)]
        while len(operatorList) > 0 and operatorList[-1] == "**" and operator == "**":
            operator = operatorDict[random.randint(1, 3)]
        operatorList.append(operator)

    questionString = f"{operandList[0]}"
    for i in range(4):
        questionString += f" {operatorList[i]} {operandList[i+1]}"
    result = eval(questionString.replace("^", "**"))
    questionString = questionString.replace("**", "^")
    return questionString, result





















