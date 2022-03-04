from attr import assoc
import requete_personnes
import mysql.connector as mysql
import association_mail_personne



class Create:

    def create_trombinoscope(self, u, p, P):
        #rentrée des données dans la base


        liste_gens_mail = association_mail_personne.Asso()
        liste_prov = liste_gens_mail.recherche()

        listeDesPersonnes = []
        for i in liste_prov:
            j = tuple(i)
            listeDesPersonnes.append(j)



        #------------------------ requêtes sql -----------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------------------------------------------
        
        ports = int(P)
        connectionMysql = mysql.connect(
        host = "localhost",
        user = u,
        passwd = p,
        database = "sys",
        port = ports)
        cursor =  connectionMysql.cursor() 



            
            #fonction pour exécuter les requêtes sql 
        def requeteSql(maVariable):
            cursor = connectionMysql.cursor()
            cursor.execute(maVariable)
            connectionMysql.commit()
            
        #------------------  création de la base de données
        
        requeteSql("CREATE DATABASE IF NOT EXISTS trombinoscope")
            
        
        #------------------ création des tables
        sql = "CREATE TABLE IF NOT EXISTS trombinoscope.personnes2(id_personne INT PRIMARY KEY AUTO_INCREMENT,nom VARCHAR(50),prenom VARCHAR(50),photo VARCHAR(255),email VARCHAR(255))"
        requeteSql(sql)
        
        
        sql = "INSERT INTO trombinoscope.personnes2(nom,prenom,photo,email)VALUES(%s,%s,%s,%s) "

        cursor = connectionMysql.cursor()
        cursor.executemany(sql, listeDesPersonnes)
        connectionMysql.commit()


  


if __name__ == '__main__':

    crea = Create()
    crea.create_trombinoscope('erwan', 'root', 3306)