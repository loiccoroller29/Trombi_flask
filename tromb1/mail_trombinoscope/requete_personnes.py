import mysql.connector as mysqlpy

class Connexion:
    USER = 'root'
    PWD = 'root'
    HOST = 'localhost'
    PORT = '8081'
    DB = 'trombinoscope'
    cursor = None

    @classmethod
    def ouvrir_connexion(cls) :
       if cls.cursor == None :
            cls.bdd = mysqlpy.connect(user = cls.USER, password = cls.PWD, host = cls.HOST, port = cls.PORT, database = cls.DB)
            cls.cursor = cls.bdd.cursor()

#la def req sert avant le traitement des données dans la base
    @classmethod
    def req(cls):
        query = "SELECT nom,prenom,id_statut,id_genre,id_personne, photo  FROM personnes;"
        cls.cursor.execute(query)
        promo = []
        for res in cls.cursor:
            promo.append(res)

        return promo

# la def req_photos sert pour l'affichage avec les mails 
    @classmethod
    def req_photos(cls):
        query = "SELECT nom,prenom,photo, email FROM personnes2;"
        cls.cursor.execute(query)
        promo = []
        for res in cls.cursor:
            promo.append(res)

        return promo


    @classmethod
    def req2(cls):
        query = "SELECT id_personne, prenom, nom FROM trombinoscope.personnes;"
        cls.cursor.execute(query)
        promo = []
        for res in cls.cursor:
            promo.append(res)

        return promo

    @classmethod
    def fermer_connexion(cls):
        cls.cursor.close()
        cls.bdd.close()
        cls.cursor = None