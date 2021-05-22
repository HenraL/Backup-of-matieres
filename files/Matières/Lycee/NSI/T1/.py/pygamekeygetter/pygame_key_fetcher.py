import pygame
pygame.init()
titre_fenetre="pygame key fetcher"
cote_fenetrex=691
cote_fenetrey=600

fenetre = pygame.display.set_mode((cote_fenetrex, cote_fenetrey))
#icone = pygame.image.load(image_icone)
#pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)
pygame.key.set_repeat(400, 30)
continueget=1
event = pygame.event.get()

while continueget:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer_accueil = 0
        elif event.type == KEYDOWN:
            #Lancement du niveau 1
            if event.key == K_SPACE:
                print("you have pressed the space key")
            elif event.key==K_a:
                print("You have pressed a")
        
