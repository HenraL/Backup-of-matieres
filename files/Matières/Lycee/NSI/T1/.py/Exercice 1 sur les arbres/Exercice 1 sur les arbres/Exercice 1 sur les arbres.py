class Bim:
    def __init__(self,nature,surface,prix_moy):
        self.nt=nature          #nature du bien: appartement, maison, bureau, commerces, ...
        self.sf=float(surface)  #surface du bien.
        self.pm=float(prix_moy) #prix moyen au m² en fonction de l'emplacement
    def estim_prix(self):
        return self.sf*self.pm
    def estim_prix_raf(self):
        if self.nt=="maison":
            return self.sf*self.pm*1.1
        elif self.nt=="bureau":
            return self.sf*self.pm*0.8
        else:
            return self.sf*self.pm

b1=Bim("maison",70.0,2000.0)
print(b1.estim_prix())

b1=Bim("maison",70.0,2000.0)
print(b1.estim_prix_raf())


lst=["maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison","bureau","hôtel","appart","maison"]
def nb_maison(lst):
    nb_maison=0
    for i in range(len(lst)):
        if lst[i]=="maison":
            nb_maison+=1
    return nb_maison
print(nb_maison(lst))
print("Henry Letellier T1")
print("Created by Henry Letellier")
