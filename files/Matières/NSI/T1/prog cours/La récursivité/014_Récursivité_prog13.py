def produit(n, p):
    """n et p sont deux entiers naturels
    Renvoie le produit de n par p"""
    if p==0:
        return 0
    else:
        return n+produit(n,p-1)
print(produit(4,3))

"""Ce program est la version d'un produit de deux nombre, tant que le deuxième élément donné,
 n'est pas égal a 0, le premier terme ajoute l'entrée au temre dans la boucle.
 par exemple:
  à la première boucle, p=3 et n=4
  à la deuxième boucle, p=2 et n=n+n(initial)=4+4
  à la troisième boucle p=1 et n=n+n(initial)=8+4
  à la quatrième boucle p=0 et on retourne n"""