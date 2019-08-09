import sys
import matplotlib.pyplot as plt
import random

print "\n######################################################\n############## Le code commence ici ##################\n"

print "\n****\nNous faisons notre premier dessin.\nPour cela, nous creons des nombres flottants (float) distribues uniformement dans l'intervalle a <= x <= b avec random.uniform( a, b). Nous voulons distribuer les nombres dans l'intervalle a = 0 a b = L. Nous voulons creer N nombres aleatoires et nous voulons les stocker dans une tableau.\n"
mot = raw_input("Tappez ENTER pour continuer :")

L = 5.0 # Longueur de la boite
N = 3 # Nombre de particules
print "\n****\nNous choisissons L =", L, "et N =", N,". Nous pouvons interpreter\nN comme le nombre de particules et\nL comme la longueur du bord d'un carre dans lequel se trouvent les particules.\n"
mot = raw_input("Tappez ENTER pour continuer :")

# positions x et y aleatoires des particules dans l'intervalle 0...L
X = [ random.uniform( 0.0 , L ) for i in range(N) ]
Y = [ random.uniform( 0.0 , L ) for i in range(N) ]
print "\n****\nNous generons des positions aleatoires pour les particules avec random.uniform( 0.0 , L ). Nous obtenons:"
print "positions x aleatoires = ", X
print "positions y aleatoires = ", Y
mot = raw_input("Tappez ENTER pour continuer :")

mot = raw_input("\n****\nAttention, apres avoir tape ENTER, une image sera creee et enregistree sous le nom Figure.png. Regardez vers le panneau le plus a gauche maintenant. Il n'y a que main.py. Apres avoir appuye sur ENTER, il y aura aussi Figure.png. Vous pouvez changer le nom de la figure a la ligne 38 du code. Important : avant de reexecuter le code, vous devez supprimer l'image. Pour cela, allez avec le curseur sur Figure.png sur le panneau de gauche. Trois points apparaissent sur la droite. Cliquez sur les trois points et selectionnez delete. Si vous ne supprimez pas l'image avant d'executer le code a nouveau, le code ne fonctionnera plus.\nVeuillez executer ce code a nouveau pour verifier que les positions des particules changent. Ensuite, executez directement Code05b.py ! Tapez ENTER maintenant ! ")


TailleImage = 7 # l'image a une longueur de bord de TailleImage pouces
fig = plt.figure( figsize=(TailleImage, TailleImage) )
ax = plt.axes( xlim=( 0, L), ylim=( 0, L)) # Intervalle des axes x et y

TaillePoints = 10.
ax.plot(X, Y, 'o', color='red', markersize = TaillePoints ) # dessine les points de donnees

Titel = "Positions aleatoires de " + str(N) + "\nparticules dans un carre de longueur de bord " + str(L)
ax.set_title(Titel, fontsize  = 18)
ax.set_xlabel('positions x', fontsize  = 20)
ax.set_ylabel('positions y', fontsize  = 20)

plt.savefig("Figure.png")
