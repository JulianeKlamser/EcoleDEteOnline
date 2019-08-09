import random
import matplotlib.pyplot as plt
import math

print "\n######################################################\n############## Le code commence ici ##################\n"

L = 5.0 # Longueur de la boite
N = 2 # Nombre de particules
print "\n****\nL =", L, "et N =", N

# positions x et y aleatoires des particules dans l'intervalle 0...L
X = [ random.uniform(0,L) for i in range(N) ]
Y = [ random.uniform(0,L) for i in range(N) ]
print "positions x aleatoires = ", X
print "positions y aleatoires = ", Y

print "\nExercise : Calculez la distance la plus courte entre deux particules qui se trouvent dans cette boite etrange (voir l'image Figure7.png). Nous dirions habituellement que les conditions aux bordures sont periodiques. Attention, contrairement au cas precedent, les coordonnees (x et y) sont differentes maintenant. Vous savez comment calculer la distance la plus courte en direction x et en direction y. Une fois que vous avez ces distances, vous n'avez plus qu'a utiliser le theoreme de Pythagore !!!!!\nVous pouvez calculer la racine carree d'un nombre avec math.sqrt( x ).\nVous pouvez calculer le carre d'un nombre avec x**2 (ou simplement x * x).\nAttention ! Avant de commencer votre calcul, faites un schema avec les deux particules pres de la limite. Les coordonnees x et y sont differentes ! Dessinez la distance la plus courte a l'interieur des limites periodiques et verifiez avec Juliane si votre schema est correct (Envoyez une photo par email ou whats app ;-) )!\nEssayez d'ecrire la fonction d'abord vous-meme, avant de consulter la solution (Code06dSolution.py). Il n'est pas necessaire de representer la connexion la plus courte entre les particules dans l'image (Figure7.png). \nContinuez ensuite avec Code7a.py"

TailleImage = 7 # l'image a une longueur de bord de TailleImage pouces
fig = plt.figure( figsize=(TailleImage, TailleImage) )
ax = plt.axes( xlim=( 0, L), ylim=( 0, L)) # Intervalle des axes x et y

TaillePoints = 10.
ax.plot(X, Y, 'o', color='red', markersize = TaillePoints ) # dessine les points de donnees

Titel = "Positions de " + str(N) + "\nparticules dans un carre de longueur de bord " + str(L)
ax.set_title(Titel, fontsize  = 18)
ax.set_xlabel('positions x', fontsize  = 20)
ax.set_ylabel('positions y', fontsize  = 20)

ImageName = "Figure7.png"
print "L'image est enregistree sous le nom", ImageName ,". Vous devez supprimer cette image avant d'executer a nouveau le code."
plt.savefig(ImageName)
