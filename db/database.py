# Gestion de la connexion à la base de données et la session résultante de la connexion

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Création de l'engine (ici SQLite)
# engine : Gère la connexion à la base.
DATABASE_URL = "sqlite:///test.db"
engine = create_engine(DATABASE_URL, echo=True)

# Configuration de la session
# SessionLocal : Crée une session pour interagir avec la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base : Classe de base qui sert à déclarer tles modèles.
Base = declarative_base()

def get_session():
    """Créer une session pour les opérations sur la BD."""
    with SessionLocal() as session:
        yield session        