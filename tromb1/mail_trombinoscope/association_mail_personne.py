
*

import import_fichier
import requete_personnes


class Asso:


    
    def recherche(self): 

        conn = requete_personnes.Connexion()
        conn.ouvrir_connexion()
        requetePersonne = conn.req()
        conn.fermer_connexion()

        fichier = import_fichier.Importer()
        emails = fichier.traitement()
        


        emails_indices = []
        emails_adresses = []
        liste=[]

        for i in range(len(emails)):
            emails_indices.append(emails[i][0])
            emails_adresses.append(emails[i][1])
        
        for i in range(len(requetePersonne)):

            nom = requetePersonne[i][0]
            prenom = requetePersonne[i][1]
            id_statut = requetePersonne[i][2]
            id_genre = requetePersonne[i][3]
            id_personne = requetePersonne[i][4]
            photo = requetePersonne[i][5]

            

            if requetePersonne[i][4] in emails_indices:

                indice_id = emails_indices.index(requetePersonne[i][4])
                email = emails_adresses[indice_id]       
                ls = [nom, prenom,photo,  email]
                liste.append(ls) 
            # else:
            #     ls = [nom, prenom, 'none']
            #     liste.append(ls)   
            
        return liste


if __name__ == '__main__':

    ass = Asso()
    res = ass.recherche()

    print(len(res))
