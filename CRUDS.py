
def estNumerique(ch: str) -> bool:
    if ch == "":
        return False
    chiffres = "0123456789."
    for i in range(0, len(ch), 1):
        existe = False
        for j in range(0, len(chiffres), 1):
            if(ch[i] == chiffres[j]):
                existe = True
                break
        if existe == False:
            return False
    return True

def afficherMenu() -> None:
    print("""
    ----------------------Gestion de stock---------------------
    **  1. Afficher tous les produits                        **
    **  2. Afficher les produits disponibles en stock        **
    **  3. Afficher les produits non disponibles en stock    **
    **  4. Recherche par référence                           **
    **  5. Recherche par désignation                         **
    **  6. Ajouter un produit                                **
    **  7. Modifier un produit                               **
    **  8. Supprimer un produit                              **
    **  9. Tri décroissant par Prix Unitaire                 **
    **  0. Quitter                                           **
    -----------------------------------------------------------
    """)

def afficherProduit(produit: dict) -> None:
    print("")
    print(f"Référence: {produit['reference']}")
    print(f"Désignation: {produit['designation']}")
    print(f"Prix unitaire: {produit['prixU']}DH")
    print(f"TVA: {produit['tva']}%")
    print(f"Disponiblité: {'Oui' if produit['disponibilite'] else 'Non'}")
    print("")

def afficherProduits(stock: list, nombreProduits: int) -> None:
    if nombreProduits == 0:
        print("\nAucun produit à afficher\n")
        return
    for i in range(0, nombreProduits, 1):
        afficherProduit(stock[i])

def ajouterProduit(stock: list) -> None:
    global nombreProduits
    global referenceMax
    if nombreProduits == NBR_MAX_PRODUITS:
        print("\nVous avez atteint la limite de votre stock\n")
        return
    produit = {}
    produit["designation"] = str(input("Désignation: "))
    produit["prixU"] = float(input("Prix unitaire (DH): "))
    produit["tva"] = int(input("TVA: "))
    produit["disponibilite"] = True
    stock[nombreProduits] = produit
    nombreProduits += 1
    referenceMax += 1
    produit["reference"] = referenceMax
    print("\nProduit bien ajouté au stock\n")

def afficherProduitsStock(stock: list, estEnStock: bool) -> None:
    global nombreProduits
    existe = False
    for i in range(0, nombreProduits, 1):
        if stock[i]["disponibilite"] == estEnStock :
            existe = True
            afficherProduit(stock[i])
    if existe == False :
        print("\nAcun produit à afficher\n") 

def rechercheParReference(stock: list, reference: int) -> dict:
    global nombreProduits
    for i in range(0, nombreProduits, 1):
        if stock[i]["reference"] == reference:
            return stock[i]
    return None

def rechercheParDesignation(stock: list, designation: str) -> None:
    global nombreProduits
    existe = False
    for i in range(0, nombreProduits, 1):
        if stock[i]["designation"] == designation:
            afficherProduit(stock[i])
            existe = True
    if existe == False:
        print("\nAucun produit à afficher\n")

def modifierProduit(stock: list, reference: int) -> dict:
    global nombreProduits
    for i in range(0, nombreProduits, 1):
        if stock[i]["reference"] == reference:
            designation = str(input("\nMerci de saisir la nouvelle désignation: "))
            if designation != "":
                stock[i]["designation"] = designation
            prixU = str(input("\nMerci de saisir le nouveau prix unitaire (DH): "))
            if(estNumerique(prixU) == True):
                stock[i]["prixU"] = float(prixU)
            tva = str(input("\nMerci de saisir le TVA (%): "))
            if(estNumerique(tva) == True):
                stock[i]["tva"] = int(tva)
            disponibilite = str(input("\nMerci de saisir la nouvelle disponibilité (o/n): "))
            if disponibilite == "o":
                stock[i]["disponibilite"] = True
            elif disponibilite == "n":
                stock[i]["disponibilite"] = False
            print(f"\nProduit avec référence = {reference} est bien modifié\n")         
            return stock[i]
    return None      

def supprimerProduit(stock: list, reference: int) -> None:
    global nombreProduits
    for i in range(0, nombreProduits, 1):
        if stock[i]["reference"] == reference:
            for j in range(i+1, nombreProduits, 1):
                stock[j-1] = stock[j]
            i -= 1
            nombreProduits -= 1
            print(f"\nProduit avec référence = {reference} est bien supprimé\n")
            return

def triPrixDecroissant(stock: list) -> None:
    global nombreProduits
    for i in range(0, nombreProduits - 1, 1):
        posMax = i + 1
        for j in range(i+1, nombreProduits, 1):
            if stock[j]["prixU"] > stock[posMax]["prixU"]:
                posMax = j
        if stock[posMax]["prixU"] > stock[i]["prixU"]:
            temp = stock[i]
            stock[i] = stock[posMax]
            stock[posMax] = temp

"""
    this is a constant
    don't set to it a new value!
    représente le nombre maximal de produits gérés par mon application
"""
NBR_MAX_PRODUITS = 100
stock = [{}] * NBR_MAX_PRODUITS
nombreProduits = 0
referenceMax = 0
produit = None
reference = 0
designation = ""
confirmation = "Non"

while True:
    afficherMenu()

    choix = int(input("Choisir une fonctionnalité: "))

    if choix == 1:
        afficherProduits(stock, nombreProduits)
    elif choix == 2:
        afficherProduitsStock(stock, True)
    elif choix == 3:
        afficherProduitsStock(stock, False)
    elif choix == 4:
        reference = int(input("\nMerci de saisir la référence du produit à chercher: "))
        produit = rechercheParReference(stock, reference)
        if produit == None:
            print(f"\nProduit avec référence = {reference} introuvable.\n")
        else:
            afficherProduit(produit)
    elif choix == 5:
        designation = str(input("\nMerci de saisir la désignation à chercher: "))
        rechercheParDesignation(stock, designation)
    elif choix == 6:
        ajouterProduit(stock)
    elif choix == 7:
        reference = int(input("\nMerci de saisir la référence du produit à modifier: "))
        produit = rechercheParReference(stock, reference)
        if produit == None:
            print(f"\nProduit avec référence = {reference} introuvable.\n")
        else:
            modifierProduit(stock, reference)
    elif choix == 8:
        reference = int(input("\nMerci de saisir la référence du produit à supprimer: "))
        produit = rechercheParReference(stock, reference)
        if produit == None:
            print(f"\nProduit avec référence = {reference} introuvable.\n")
        else:
            confirmation = str(input("\nVoulez-vous bien supprimer ce produit (Oui/Non)? "))
            if confirmation == "Oui":
                supprimerProduit(stock, reference)
            else:
                print("\nOpération abandonnée\n")
    elif choix == 9:
        triPrixDecroissant(stock)
        print("\nTRi effectué avec succès.\n")
    elif choix == 0:
        print("\nMerci. A Bientôt\n")
        break
    else:
        print("\nFonctionnalité non disponible\n")
