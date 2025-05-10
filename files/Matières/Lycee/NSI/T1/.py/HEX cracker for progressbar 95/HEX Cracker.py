def pause():
    input("Press enter to continue...")


firstlist = []
listchecked = []
listdisplay = []
counter = {}
cont = "y"
while cont.lower() == "y":
    ask = input("Entrez 'n' pour quitter (ou dérouler le programme une fois les valeurs entrées), "
                "'o' pour ouvrir un fichier contenant une matrice ou un hexadécimal : ").strip().upper()

    if ask == "O":
        fto = input("Entrez le nom exact du fichier à ouvrir : ")
        try:
            with open(fto, "r", encoding="utf-8") as f:
                c = f.read()

            word = ""
            for char in c:
                if char in [" ", "\n"]:
                    if word:
                        firstlist.append(word)
                        word = ""
                else:
                    word += char
            if word:  # Catch the last word if not followed by space or newline
                firstlist.append(word)

            cont = "n"
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{fto}' est introuvable.")
        except Exception as e:
            print(f"Désolé, une erreur est survenue : {e}")
            print("Veuillez entrer les valeurs manuellement.")
    elif ask != "N":
        firstlist.append(ask)
    else:
        cont = "n"

# Affichage des entrées
print(f"Ce que vous avez entré est : {firstlist}")

# Comptage des occurrences
for item in firstlist:
    counter[item] = counter.get(item, 0) + 1
    if counter[item] > 1:
        print(f"{item} déjà présent dans firstlist.")

# Affichage des éléments apparaissant plus d'une fois
for item, count in counter.items():
    if count > 1:
        listdisplay.append(item)
    else:
        print(f"{item} est unique.")

# Résumé des doublons
print(f"Les {len(listdisplay)} itérations sont : {', '.join(listdisplay)}.")

# Élément apparaissant exactement 5 fois
print("L'élément apparaissant 5 fois est : ", end="")
found = False
for item, count in counter.items():
    if count == 5:
        print(f"'{item}'", end="")
        found = True
if not found:
    print("Aucun.", end="")
print(".")

pause()
pause()
pause()
pause()
