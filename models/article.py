from db.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Article(Base):
    """Classe de base servant de modèle pour la table articles"""    
    
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    prix = Column(Float, )
    categorie_id = Column(Integer, ForeignKey("categories.id"))
    
    categorie = relationship("Categorie", back_populates="articles")
    
    def __repr__(self):
        return f"{self.description} à {self.prix:.2}$"