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
Mean = 0

print "\n*****\nNos", N , "nombres aleatoires sont :"
for i in range(N):
    C = random.randint( A, B )
    Mean += C # (c'est l'equivalent a : Mean = Mean + C)
    print C

Mean /= float(N) # (c'est l'equivalent a : Mean = Mean / float(N))
print "\n****\nLa valeur moyenne de", N ,"nombres aleatoires est", Mean
