#EX 1: Q 3)b)
if v<n.v: #si v est plus petit que le noeud parent, on insère à gauche
	if n.ag!=None:
		n=n.ag
	else:
		n.ag=Noeud(v)
		est_insere=True
else: #si v est plus grand que le noeud parent, on insère à droite
	if n.ad!=None:
		n=n.ad
	else:
		n.ad=Noeud(v)
		est_insere=True

#___________________________________________________________________________________________________________________________________

#EX1:Q:4
def recherche(self, v):
    tree_content=self.v
	max_length=len(self.v)
	tree_index=0
	to_divide_by=2
	while tree_index<max_length:
		if v==tree_content[tree_index]:
			return True
		elif tree_index==max_length:
			return False
		elif v>tree_content[tree_index]:
			tree_index+=max_length/to_divide_by
			to_divide_by+=2
		elif v<tree_content[tree_index]:
			tree_index=max_length/to_divide_by
			to_divide_by+=2
		tree_index+=1
	return False


#___________________________________________________________________________________________________________________________________

#EX4:Q:3

def moitie_droite(L):
    e=len(L)//2
    r=len(L)
    f=[]
    for i in range(e,r):
        f.append(L[i])
    return f



#___________________________________________________________________________________________________________________________________

#EX4:Q:4

# Failed

