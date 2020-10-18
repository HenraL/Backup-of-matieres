def accueil():
    #BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_F1:
					continuer_accueil = 0	#On quitte l'accueil
					choix = 'n1'		#On définit le niveau à charger
				#Lancement du niveau 2
				elif event.key == K_SPACE:
					continuer_accueil = 0
					choix = 'n2'
				elif event.key == K_ENTER:
					continuer_accueil = 0
					choix = 'n3'
				elif event.key == K_S:
					continuer_accueil = 0
					choix = 'n4'
				elif event.key == K_Q:
                    continuer_accueil = 0
                    continuer_jeu = 0
                    continuer = 0
                    #Variable de choix du niveau
                    choix = 0
    return continuer_accueil, continuer_jeu, continuer = 0, choix