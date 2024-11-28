#Partie 2: mathGame.py 

'''
Tâche 1 :Importation et initialisation

1-Importer le fichier de fonctions myPythonFunctions.
2-Demander le nom de l’utilisateur, puis récupèrer ou initialiser son score.
'''
import myPythonFunctions as mpf

userName = input("Entrez votre nom : ")
userScore = mpf.getUserPoint(userName)
newUser = userScore == -1
if newUser:
    userScore = 0

'''
Tâche 2 :Boucle de jeu principale

1-Tant que l'utilisateur ne tape pas -1, génèrer une nouvelle question
et vérifier la réponse.
2-Met à jour le score selon que la réponse est correcte ou non.
'''
userChoice = ""
while userChoice != "-1":
    question, answer = mpf.generateQuestion()
    print(f"Question : {question}")
    try:
        userResponse = int(input("Votre réponse : "))
        if userResponse == answer:
            print("Correct !")
            userScore += 1
        else:
            print(f"Incorrect. La bonne réponse était : {answer}")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    userChoice = input("Tapez '-1' pour quitter ou appuyez sur 'Entrée' pour continuer : ")

'''
Tâche 3 :Sauvegarde finale

1-Une fois la boucle terminée, appelle updateUserPoints() pour sauvegarder le score.
'''
mpf.updateUserPoints(newUser, userName, userScore)
print("Merci d'avoir joué ! Votre score a été enregistré.")
