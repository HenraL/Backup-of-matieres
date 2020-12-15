from random import *
fichier = open('data_lists/le_rouge_et_le_noir_stendal.txt', 'r')
stendhal = fichier.read()
fichier.close()
print("len(stendhal)=",len(stendhal))
print("len(\"Julien trembla\")=",len("Julien trembla"))
print("stendhal.find('Julien trembla')=(line)",stendhal.find('Julien trembla'))
print("stendhal[161411:161445] + '...' =",stendhal[161411:161445] + '...' )
text=stendhal
def snip_shower(times):
    print("times=",times)
    for i in range(int(times)):
        e=randint(0,len(stendhal)-(len(stendhal)//2))
        z=e+34
        print(e,z)
        print("i={}".format(i))
        print("stendhal[{}:{}] + '...' ={}".format(e,z,stendhal[e:z]+'...'))

k="go"
while k=="go":
    g=input("Entrez un nombre:")
    if g.isnumeric()==True:
        g=int(g)
        k="stop"
        snip_shower(g)
    else:
        print("Vous n'avez pas rentré un nombre\nVous avez entré:{}".format(g))

print("stendhal.find('Joséphine')={}".format(stendhal.find('Joséphine')))

def nbOccurences(motif):
    compteur, i = 0, 0
    while True:
        occurrence = find(motif, i)
        # occurrence est l'index du sous-texte à partir de l'index i
        if occurrence == -1:
            return compteur
        else:
            compteur += 1
            i += occurrence + 1

print("nbOccurences('Julien')={}".format(nbOccurences('Julien')))
print("nbOccurences('amour')={}".format(nbOccurences('amour')))
print("nbOccurences('mort')={}".format(nbOccurences('mort')))

