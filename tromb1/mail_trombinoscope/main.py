from flask import Flask, render_template, request
import insertion
import requete_personnes
import mel

app = Flask(__name__)

#incrémentation du diaporama
i=0



@app.route('/', methods = ['GET','POST'])
def home():
    global i

    # incrémentation du diaporama
    if request.form:
        res = request.form
        if res['suivant'] == "0":   #bouton suivant
            if i==25:
                i=0
            i = i + 1 
        elif res['suivant'] == "1": #bouton précédent
            if i==0:
                i=25
            i = i - 1
        elif res['suivant'] == "2":  # bouton envoi mail
            email = res['email']
            envoi = mel.Mail()
            envoi.send(email,'information', 'Ce message est un test d\' envoi' )
        else:
            i = 0

    # # création de la base de données    
    # creation_bdd = insertion.Create()
    # creation_bdd.create_trombinoscope('erwan', 'root', 3306)
    
    # requête
    req = requete_personnes.Connexion()
    req.ouvrir_connexion()
    res = req.req_photos()
    req.fermer_connexion()

    # créer une variable pour les noms, prénoms et photos
    nom_image = res[i][2]
    nom_image = nom_image+".jpg"
    nom = res[i][0]
    prenom = res[i][1]
    email = res[i][3]



    return render_template('index.html', nom=nom,nom_image=nom_image,prenom = prenom,email=email,)




if __name__ == "__main__":
    app.run(debug=True)
