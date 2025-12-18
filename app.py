from flask import Flask, flash, render_template, request, redirect, url_for
from db.database import Base, engine, get_session, SessionLocal
from models.article import Article
from models.categorie import Categorie

app = Flask(__name__)
app.secret_key = "clé_secrète" # définie pour les messages flash

# Création des tables
Base.metadata.create_all(bind=engine)

# Accueil – liste des articles
@app.route('/')
def index():
    with next(get_session()) as session:
        articles = session.query(Article).all()
        return render_template("index.html", articles = articles)

# Ajouter un article
@app.route('/ajouter_article', methods=["GET", "POST"])
def ajouter_article():
    with next(get_session()) as session, session.begin():
        if request.method == "POST":
            description = request.form.get("description", "").strip()
            prix_str = request.form.get("prix", "").strip()

            if not description or not prix_str:
                return render_template(
                    "ajouter.html",
                    erreur="Tous les champs sont obligatoires."
                )

            try:
                prix = float(prix_str)
            except ValueError:
                return render_template(
                    "ajouter.html",
                    erreur="Le prix doit être un nombre valide."
                )
                
            if prix < 0:
                return render_template(
                    "ajouter.html",
                    erreur="Le prix ne peut pas être négatif."
            )
                       
            session.add(Article(description=description, prix=prix))
            flash("Article créé avec succès !", "success")
            return redirect(url_for('index'))
    return render_template('ajouter.html')

def modifier_article():
    pass

@app.route('/supprimer_article/<article_id>')
def supprimer_article(article_id):
    with next(get_session()) as session, session.begin():
        article = session.query(Article).get(article_id)
        if article:
            session.delete(article)
        else:
            flash("Aucun article trouvé.", "danger")
            return redirect(url_for('index'))
    flash("Article supprimé avec succès !", "success") 
    return redirect(url_for('index'))

if __name__ == "__main__":    
    app.run(debug=True)