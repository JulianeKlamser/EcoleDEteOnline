import random
import math
from matplotlib import pyplot as plt
import os

print "\n######################################################\n############## Le code commence ici ##################\n"

# creation des repertoires
ImagPath = "Figures/" # ignorez cette ligne
AniPath = "Animation/" # ignorez cette ligne
os.mkdir(ImagPath) # ignorez cette ligne
os.mkdir(AniPath) # ignorez cette ligne

L = 5.0 # Longueur de la boite
N = 2 # Nombre de particules
dt = 0.05 # pas de temps discrets
print "\n******************\nNous allons faire notre premiere animation maintenant ! Deux particules (N =", N, ") dans un carre de longueur d'arete L = ", L , "se deplaceront a une vitesse constante. Nous choisissons des positions initiales aleatoires et des orientations aleatoires de la direction du mouvement (de la vitesse).\n\nPour faire une simulation, nous devons deplacer les particules un tout petit peu, puis prendre une photo, puis deplacer un tout petit peu a nouveau, puis prendre une photo, puis deplacer un tout petit peu, puis... Nous disons, nous discreditons le temps. Dans un petit intervalle de temps dt = ", dt, ", une particule se deplace sur une distance dx = dt * v (si elle a une vitesse constante v).\n\nVotre tache consiste a modifier les lignes 36 et 37, de sorte que les deux particules se deplacent dans des conditions limites periodiques. L'operateur modulo vous sera utile ici !\nComparez avec la solution de Code07aSolution.py\nCette fois, vous devez supprimer les deux repertoires (Animation et Figures) si vous voulez relancer le code !\nUne fois que vous avez reussi, ecrivez un e-mail a Juliane pour savoir comment transformer les particules en oiseaux."

mot = raw_input("\nTappez ENTER pour continuer :\n")
print "Comme nous executons le code dans le navigateur, cela prendra un certain temps pour creer toutes les images. S'il vous plait, soyez un peu patient. Si le code est bloque, rechargez le site Web, copiez a nouveau votre code et redemarrez le code."

XPos = [ random.uniform( 0.0, L) for i in range( N ) ] # Coordonnees x de la position des particules
YPos = [ random.uniform( 0.0, L) for i in range( N ) ] # Coordonnees y de la position des particules
Angle = [ random.uniform( 0.0, 2. * math.pi ) for i in range( N ) ] # angle d'orientation (Direction du mouvement)
ParticleOrder = [ i for i in range(N) ] # cree un tableau [0 1 2 3 ... N]

NombreDImages = 100
fig = plt.figure( figsize=(7, 7) )
for imag in range( NombreDImages ):
    # Je calcule les nouvelles positions des particules.
    random.shuffle( ParticleOrder ) # reorganise l'ordre des nombres dans le tableau de facon aleatoire
    for pA in ParticleOrder: # la boucle passe par toutes les entrees du tableau
        xVel = math.cos( Angle[ pA ] ) # Vitesse dans la direction x
        yVel = math.sin( Angle[ pA ] ) # Vitesse dans la direction y
        # Notez que sart( xVel**2 + yVel**2 ) = 1. Les particules ont une vitesse constante (v = 1).
        
        XPos[ pA ] = ( XPos[ pA ] + dt * xVel ) % L # changez ici
        YPos[ pA ] = ( YPos[ pA ] + dt * yVel ) % L # changez ici

    # creation des images
    print "creation d'image", imag,"sur", NombreDImages
    ax = plt.axes( xlim=( 0, L), ylim=( 0, L))
    Titel = "Positions de " + str(N) + "\nparticules dans un carre de longueur de bord " + str(L)
    ax.set_title(Titel, fontsize  = 18)
    ax.set_xlabel('positions x', fontsize  = 20)
    ax.set_ylabel('positions y', fontsize  = 20)
    ax.plot(XPos, YPos, 'o', color='red', markersize = 10 ) # dessine les points de donnees
    FileName = ImagPath + "%04i.png" % imag
    plt.savefig(FileName)
    plt.clf()

plt.close()

print("Je cree une animation sous forme de gif. Laissez-moi un peu de temps ! Je vous le dirai quand je serai pret.")
os.system("convert -delay 1 -dispose Background +page " + ImagPath + "/*.png -loop 0 " + AniPath + "/animation.gif")
print("Maintenant, vous trouverez l'animation dans le dossier Animate. Il a besoin d'un certain temps pour se charger. Vous pouvez egalement telecharger l'animation. Vous devez supprimer les deux repertoires (Animation et Figures) si vous voulez relancer le code !")
