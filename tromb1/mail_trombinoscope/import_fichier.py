import os
import requete_personnes


class Importer:

    def __init__(self):
        self.rep = os.getcwd()
        self.path = os.path.join(self.rep, 'adresses.txt')        

    def traitement(self):
    
        global db
        global cursor    

        emails_import = open(self.path,'r')
        emails_import = emails_import.readlines()

        emails = []
        emails_split = []
        
        # remplacement des sauts de lignes
        for ligne in emails_import:
            a = ligne.replace('\n','')
            emails.append(a)

        # mise en forme : prénom, nom, mail
        for ligne in emails:
            # récupération nom prénom par split
            a = ligne.split('@')
            a = a[0].split('.')

            if a[0] == "younes":
                continue

            # récupération des nom, prénoms de la bdd
            requ_bdd = requete_personnes.Connexion()
            requ_bdd.ouvrir_connexion()
            reponse= requ_bdd.req2()
            requ_bdd.fermer_connexion()
            

            reponse_bdd = []
            for i in reponse:
                l = list(i)
                reponse_bdd.append(l)

            for entree in reponse_bdd:
                # retourne l'id enregistré dans la bdd
                id = 0

                # remplacer les caractères spéciaux de la bdd pour le traitement :
                if 'ï' in entree[1]:
                    entree[1] = entree[1].replace("ï", "i")
                if 'é' in entree[1]:
                    entree[1] = entree[1].replace("é", "e")

                # recherche dans la bdd (liste de listes)    
                # a[0] est le prénom du fichier texte
                # entree[1] le prénom dans la bdd
                if a[0] == entree[1]:
                    if a[0] == 'loic':

                        # gestion des loic
                        if a[1] == 'coroller' and entree[2] == 'coroller':
                            id = entree[0]
                            break
                        if a[1] == 'plessis' and entree[2] == 'plessis':
                            id = entree[0]
                            break
                    
                    else:
                        id = entree[0]
                        break



            b = (id, ligne)
            emails_split.append(b)

        return emails_split


if __name__ == '__main__':
    abc  = Importer()
    res = abc.traitement()
    print(res)