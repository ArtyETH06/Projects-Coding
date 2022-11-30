#Ceci est un code python afin d'aider les débutant à la programmation Python, avec des données simplifiées
#Cela va créer un autre fichier Python avec les explication + choix de l'utilisateur
#J'ai essayé au maximum d'expliquer les bases le plus simplement...
#Tache finale NSI 1er

from PIL import Image

#On a des problèmes après avec les guillemets
guillement = ' " '

#On définit la fonction "python_code_maker"
def python_code_maker():
    print("Console: Bienvenue dans Python code maker !")
    print("Console: Vous allez pouvoir créer un code python facilement et rapidement")

#On initialise les choix
    choix = 1
    choice2 = 0

    #La boucle
    while choix != 0:

        #Choix de l'utilisateur
        choix = int(input("Console: Veuillez faire un choix: \n0_quitter\n1-Reset\n2-Afficher quelque chose\n3-Créer une variable\n4-Importer un module/fichier\n5-Aide\n6-Exemple\n7-Créer un input\n?-???????\nVous avez sélectionné le menu " + str(choix) + "!"))

#--------------------------------------------------------------------Choix 1 (reset)------------------------------------------------------------------
        if choix == 1:

            #On travaille sur le fichier "Python code"
            with open("Python code.py", "w+") as file:
                print("")


#--------------------------------------------------------------------Choix 2 (Afficher quelque chose)------------------------------------------------------------------
        elif choix == 2:
            #Ce que l'utilisateur souhait print dans le terminal
            to_print = input("Console: Que voulez vous afficher ?")
            #On travaille sur le fichier "Python code"
            with open("Python code.py", "a+") as file:
                #Permet de concatoner toute la string
                final_print = 'print('+guillement+to_print+guillement+')'
                file.write('\n#Pour afficher quelque chose dans le terminal, on utilise print("")\n')
                #Mettre dans le code "Python Code" ce que l'utilsateur veut print
                file.write(final_print)
                print("Console: Vous venez d'afficher " + to_print + "!")
                file.close


#--------------------------------------------------------------------Choix 3 (créer une variable)------------------------------------------------------------------
        elif choix == 3:

            choice2 = int(input("Console: Quel est le type de variable que vous voulez créer ?\n1-Une chaine de caractère\n2-Un nombre"))
            if choice2 == 1:
                name = input("Quel est le nombre de votre variable ? ")
                value = input("Quel est la chaine de caractère que vous voulez mettre en valeur ? ")
                #On travaille sur le fichier "Python code"
                with open("Python code.py", "a+") as file:
                    #Permet de concatoner toute la string
                    final_print = name + ' = ' + guillement + value + guillement
                    file.write('\n#Pour créer une variable de type string,vous devez mettre le nom de votre variable,puis un = et la valeur de votre variable entre guillemets\n')
                    #Mettre dans le code "Python Code" ce que l'utilsateur veut print
                    file.write(final_print)
                    print("Console: Vous venez de créer la variable " + name + " de valeur " + value)
                    file.close


            elif choice2 == 2:
                name = input("Quel est le nom de votre variable ? ")
                value = float(input("Quel est la valeur de votre variable (nombre/chiffre) "))
                #On travaille sur le fichier "Python code"
                with open("Python code.py", "a+") as file:
                    #Permet de concatoner toute la string
                    final_print = name + ' = ' + str(value)
                    file.write('\n#Pour créer7 une variable,vous devez mettre le nom de votre variable,puis un = et la valeur de votre variable\n')
                    #Mettre dans le code "Python Code" ce que l'utilsateur veut print
                    file.write(final_print)
                    print("Console: Vous venez de créer la variable " + name + " de valeur " + str(value))
                    file.close

            else:
                print("Console: Error 404 ")
                break

#-------------------------------------------------------------------------------4(Import module/fichier)-----------------------------------------------------------------

        elif choix == 4:
            name = input("Console: Quel est le nom du module/fichier que vous voulez importer ? ")
            with open("Python code.py", "a+") as file:
                file.write('\n#Pour importer un fichier/module, vous devais faire: from XXX import *' )
                file.write('\nfrom ' + name + ' import *\n' )
                #Mettre dans le code "Python Code" ce que l'utilsateur veut print
                print("Console: Vous venez d'importer le module/fichier " + name)
                file.close

#-------------------------------------------------------------------------------5(Aide)-----------------------------------------------------------------

        elif choix == 5:
            print("Si vous avez besoin d'aide en python,vous pouvez regarder cette vidéo très utile--> https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            with open("Python code.py", "a+") as file:
                file.write('#Cette vidéo peut aider pour les débutants en python ;) --> https://www.youtube.com/watch?v=dQw4w9WgXcQ\n')
                #Mettre dans le code "Python Code" ce que l'utilsateur veut print
                print("Console: Cette leçon vous aura servie ?")
                file.close

#-------------------------------------------------------------------------------6(exemple)-----------------------------------------------------------------
        elif choix == 6:
            print("Console: Voici un exemple regroupant pas mal de notions ;)")
            #Reset du code...(w+ permet d'effacer les données précedentes avec ce que l'on veut écrire)
            with open("Python code.py", "w+") as file:
                file.write("#Les imports: nous permettent d'importer des fichiers/modules (ils sont souvent places au debut...)\n")
                file.write("from math import *   #Ici,nous importons les modules de la librairies math\n")
                file.write("\n#Nous allons maintenant creer des variables et leur affecter des valeurs:\n")
                file.write("#Une chaine de caractere est affectee en mettant des guillement (tres souvent)\n")
                file.write("name = 'La console'\n")
                file.write("#Un age est un  nombre,donc on met juste sa valeur\n")
                file.write("age = 16\n")
                file.write("\n#Etudions les fonctions,les fonctions,une fois creer permettent d'etre appele et execute partout ! Et quand on veut\n")
                file.write("def ma_fonction(name, age):\n")
                file.write("    print('Bienvenue ' + name + ', vous avez maintenant ' + str(age)  + ' ans !')   #Print nous permet d'afficher des éléments dans le terminal\n")
                file.write("\n#Pour executer la fonction,nous avons juste a mettre son nom et les arguments qu'elle prend\n")
                file.write("ma_fonction(name, age)\n")
                file.close

                #Afficher dans le terminal que l'exemple a été généré avec succès
                print("L'exemple a été généré avec succès !")
                file.close
                break

#--------------------------------------------------------------------Choix 7 (input)------------------------------------------------------------------
        elif choix == 7:

            choice2 = int(input("Console: Quel est le type d'input que vous voulez créer ?\n1-Une chaine de caractère\n2-Un nombre(float)"))
            if choice2 == 1:
                name = input("Quel est le nombre de votre input ? ")
                value = input("Quel est le message de votre input ? ")
                #On travaille sur le fichier "Python code"
                with open("Python code.py", "a+") as file:
                    #Permet de concatoner toute la string
                    final_print = name + ' = ' + "input(" + guillement + value + guillement + ")"
                    file.write('\n#Pour créer un un input de chaine de caractère,on doit mettre: nom de la variable = input("message")\n')
                    #Mettre dans le code "Python Code" ce que l'utilsateur veut print
                    file.write(final_print)
                    print("Console: Vous venez de créer un input " + name + " avec pour message " + value)
                    file.close


            elif choice2 == 2:
                name = input("Quel est le nombre de votre input ? ")
                value = input("Quel est le message de votre input ? ")
                #On travaille sur le fichier "Python code"
                with open("Python code.py", "a+") as file:
                    #Permet de concatoner toute la string
                    final_print = name + ' = ' + "float (input(" + guillement + value + guillement + "))"
                    file.write('\n#Pour créer un un input de chiffre/nombre,on doit mettre: nom de la variable = int(input("message"))\n')
                    #Mettre dans le code "Python Code" ce que l'utilsateur veut print
                    file.write(final_print)
                    print("Console: Vous venez de créer un input " + name + " avec pour message " + value)
                    file.close

            else:
                print("Console: Error 404 ")
                break
#--------------------------------------------------------------------Choix ? (?)----------------------------------------------------------
        elif choix == 10:

            print("Console: Comment avez vous fait pour venir jusqu'ici ?\nVous êtes un maitre du code ?")
            choice3 = int(input("1-Oui\n2-Non"))
            if choice3 == 1:
                print("Console: Le python n'a plus de secret pour vous...Vous n'avez donc plus besoin de moi...Au revoir !")
                break
            elif choice3 == 2:
                print("Console: Alors comment êtes vous arrivé la ?")

            else:
                print("Console: Erreu.Errzur Syt..eteing:...Fin du système, la simulation est terminée.")
                break

        if (7 < choix and choix < 10) or choix > 10:
            print("Console: Veuillez choisir un chiffre valide...:/")

#--------------------------------------------------------------------Choix 0 (Si l'utilisateur quitte)------------------------------------------------------------------
    #Si l'utilisateur a fait 0 (quitte)
    print("Console: Vous avez quitté le terminal")





#Fonction d'apprentissage !
def learn():
    print("Console: Bienvenue dans l'interface de lesson !")
    choice = int(input("Console: Veuillez choisir votre lesson:\n1-Les imports\n2-Variables\n3-Afficher quelque chose\n4-Fonction"))


#-----------------------------------------------------------------------------Les imports---------------------------------------------------------
    if choice == 1:
        print("Console: Bienvenue dans cette première lesson,vous allez apprendre à importer des modules/fichiers !")
        print("Console: Pour importer des modules/fichiers,vous devez faire:")
        print("from XXX import *\n Cela va importer toutes les fonctions/variables que contient le fichier...")
        print("Console: Essayez,et si vous pensez que c'est bon,validez !")
        user_input = input("Veuillez importer tout ce que contien le fichier 'math' \n")
        verify = "from math import *"
        good = 0

        while good == 0:

            if user_input == verify:
                    print("Console: Félicitations ! Vous avez obtenu un badge !")
                    #Ouvrir le badge obtenu
                    img = Image.open("import.png")
                    img.show()
                    sortir de la boucle
                    good = 1
                    break

                
            else:
                print("Console: Ce n'est pas bon...Essayez encore")

    
        




#On exécute la fonction
learn()
