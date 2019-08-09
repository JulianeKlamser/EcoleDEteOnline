import sys
import random

print "\n######################################################\n############## Le code commence ici ##################\n"

S = 10
random.seed( a = S )

print "\n******\nNotre but est maintenant de remplacer le voisin par un generateur de nombres aleatoires.\nNous allons maintenant generer 10 nombres aleatoires avec une boucle for. Le nombre aleatoire R satisfera la relation : A <= R <= B et R est distribue uniformement dans cet intervalle.\nPour commencer, nous choisissons A = -10 et B = 10."
mot = raw_input("Appuyez sur ENTER pour continuer !")

A = -10
B = 10
N = 10

print "\n*****\nNos", N , "nombres aleatoires sont :"
for i in range(N):
    C = random.randint( A, B )
    print C

mot = raw_input("Appuyez sur ENTER pour continuer !")
print "\n*****\nFaites un exercice a la fois ! Respectez l'ordre des exercices !\nExercice 1 : Executez a nouveau le code ! Les nombres aleatoires ont-ils change ?\nExercice 2 : Sur ligne 6, remplacer 'S = 10' par 'S = None'. Executez le code a nouveau. Les nombres ont-ils change maintenant ? Regardez cette video pour comprendre le resultat. https://www.youtube.com/watch?v=tcbq1aRJQrA\nExercice 3 : Calculez la valeur moyenne des nombres aleatoires. Imprimer la valeur moyenne apres la boucle for. (Rappelez-vous le comportement different des nombres entiers et des nombres flottants pour la division !)\nExercice 4 : Augmentez N (par example N = 10000) a la ligne 14 et verifiez que la valeur moyenne est egale a zero.\nApres avoir reussi, executez Code03c.py\n\nVous trouverez la solution de l'exercice 3 dans Code03bSolution.py"
