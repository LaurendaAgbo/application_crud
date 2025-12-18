from flask import Flask, render_template
from db.database import Base, engine, get_session, SessionLocal
from models.article import Article
from models.categorie import Categorie

app = Flask(__name__)

# Création des tables
Base.metadata.create_all(bind=engine)

@app.route('/')
def index():
    with next(get_session()) as session:
        articles = session.query(Article).all
        return render_template("index.html", articles = articles())

def ajouter_article():
    pass

def modifier_article():
    pass

def supprimer_article():
    pass

if __name__ == "__main__":    
    app.run(debug=True)