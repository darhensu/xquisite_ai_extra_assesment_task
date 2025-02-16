# model data
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=Tru, index=True)
    description = Column(String, nullable=True)

    # relation
    items = relationship("Item", back_populates="category")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories,id"))
    #price = Column(Integer)
    #quantity = Column(Integer, default=0)

    # relation to category
    category = relationship("Category", back_populates="items")