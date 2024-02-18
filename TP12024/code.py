def identite(s : str) -> str :
    """ Renvoie la chaine s telle quelle """
    return s

assert identite("LU1IN011") == "LU1IN011"
assert identite("") == ""

def identite_texte(nom : str) -> None :
    """ Precondition : <nom>.txt est un fichier existant
    recopie le contenu du fichier <nom>.txt dans <nom>-copie.txt """
    with open(nom + ".txt", "r") as source :
        with open(nom + "-copie.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(identite(ligne))
