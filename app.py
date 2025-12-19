from flask import Flask, flash, render_template, request, redirect, url_for
from db.database import Base, engine, get_session
from db.init_data import init_categories
from models.article import Article
from models.categorie import Categorie

app = Flask(__name__)
app.secret_key = "clé_secrète" # définie pour les messages flash

# Création des tables
@app.before_request
def init_app():
    Base.metadata.create_all(bind=engine)
    init_categories()

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
        categories = session.query(Categorie).order_by(Categorie.nom).all()
        
        if request.method == "POST":
            description = request.form.get("description", "").strip()
            prix_str = request.form.get("prix", "").strip()
            categorie_id = request.form.get("categorie_id")

            if not prix_str:
                prix = 0.00
            prix = float(prix_str)
                
            if prix < 0:
                return render_template(
                    "ajouter.html",
                    erreur="Le prix ne peut pas être négatif.",
                    categories = categories
            )
            
            if not categorie_id:
                categorie = None
            else:
                categorie = session.query(Categorie).get(categorie_id)
                       
            session.add(Article(description=description, prix=prix, categorie=categorie))
            flash("Article créé avec succès !", "success")
            return redirect(url_for('index'))
        return render_template('ajouter.html', categories = categories)

@app.route('/modifier_article/<article_id>', methods=["GET", "POST"])
def modifier_article(article_id):    
    with next(get_session()) as session, session.begin():
        article = session.query(Article).get(article_id)
        categories = session.query(Categorie).order_by(Categorie.nom).all()
        if not article:
            flash("Aucun article trouvé.", "danger")
            return redirect(url_for('index'))
        
        if request.method == "POST":
            description = request.form.get("description", "").strip()
            prix_str = request.form.get("prix", "").strip()
            prix = float(prix_str)
            categorie_id = request.form.get("categorie_id")
                
            if prix < 0:
                flash("Le prix ne peut pas être négatif.", "danger")
                return redirect(url_for('modifier_article', article_id=article_id))
            
            categorie = session.query(Categorie).get(categorie_id)
                    
            article.description = description
            article.prix = prix
            article.categorie = categorie
            flash("Article créé avec succès !", "success")
            return redirect(url_for('index'))
        
        return render_template('modifier.html', article = article, categories = categories)

# Supprimer un article
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