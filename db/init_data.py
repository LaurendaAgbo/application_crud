from models.categorie import Categorie
from db.database import SessionLocal

CATEGORIES_PAR_DEFAUT = ["Beauté", "Épicerie", "Jouets", "Électroménager"]

# Persistance des catégories par défaut
def init_categories():
    with SessionLocal() as session, session.begin():
        for nom in CATEGORIES_PAR_DEFAUT:
            existe = session.query(Categorie).filter_by(nom=nom).first()
            if not existe:
                session.add(Categorie(nom=nom))