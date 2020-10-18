#Définition de la classe voiture
class voiture:
    #constructeur
    def __init__(self): #self déisgne l'instance de la classe
        #initialisation des attributs d'instance
        self.couleur="rouge"
        self.puissance="150ch"
        self.moteur="Diesel"
        self.prix="50000€"
        self.niveau_carburant=50
        self.compteur_km=0
    
    #definition des méthodes
    def avance(self):
        self.niveau_carburant=self.niveau_carburant-0.1
        self.compteur_km=self.compteur_km+1
        print("Avance broom broom ...")

#Je créé 3 instances (objet) de la classe voiture:

voiture1=voiture()
voiture2=voiture()
voiture3=voiture()

print("couleur voiture1 : {}".format(voiture1.couleur))
print("puissance voiture1: {}".format(voiture1.puissance))

print("couleur voiture 2: {}".format(voiture2.couleur))
print("puissance voiture 2: {}".format(voiture2.puissance))

print()
print("Niveau carburant voiture1: {}".format(voiture1.niveau_carburant))
print("Kilomètres parcourus voiture1: {}".format(voiture1.compteur_km))

voiture1.avance() #appelle de la méthode avance, ne pas oublier les parenthèses

print("Niveau carburant voiture 1: {}".format(voiture1.niveau_carburant))
print("Kilomètre parcourus voiture1 : {}".format(voiture1.compteur_km))