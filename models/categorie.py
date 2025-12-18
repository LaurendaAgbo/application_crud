from db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Categorie(Base):
    """Classe de base servant de modèle pour la table categories"""    
    
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True, nullable=False)
    
    articles = relationship("Article", back_populates="categorie")
    
    def __repr__(self):
        return f"{self.nom}"
    