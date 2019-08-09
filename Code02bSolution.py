import sys

print "\n######################################################\n############## Le code commence ici ##################\n"

mot = raw_input("\nVeuillez entrer un nombre entier positif entre 1 et 5 (appuyez sur enter apres) :")
nombre = int( mot )

print "\n*****\nLes nombres entre 0 et ", nombre, " sont:"
# Debut de la boucle for
for i in range( nombre ):
    print i #L'espace vide avant print doit etre cree avec la touche Tab !!!!
# Fin de la boucle for

print "\n*****\nEt la somme et le produit sont calculee ici:"
total = 0
produit = 1
for i in range( nombre ):
    total = total + i
    print "Calcul du produit produit = produit * i =", produit, "*", i
    produit = produit * i
    print i, " ;la somme est ",  total, " ;le produit est ",  produit, "\n"

print "\n******\nLe resultat de la multiplication par zero est toujours egal a zero. Dans la premiere iteration, i est egal a zero. Par consequent, le produit devient zero. Tous les calculs suivants sont donc la multiplication par zero. Une facon d'eviter ce resultat est d'utiliser a la place\nproduit = produit * ( i + 1)\nEssayez-le !\nContinuez avec Code02c.py !\n"
