# operasi CRUD

from sqlalchemy.orm import Session
import models, schemas

# CATEGORY
# CREATE - Menambahkan category baru
def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# READ - Mendapatkan semua category
def get_categories(db:Session):
    return db.query(models.Category).all()

# READ - Mendapatkan category berdasarkan ID
def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

# UPDATE - Mengupdate category berdasarkan ID
def update_category(db: Session, category_id: int, category: schemas.CategoryCreate):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db_category.name = category.name
        db_category.description = category.description
        db.commit()
        db.refresh(db_category)
    return db_category

# DELETE - Menghapus category berdasarkan ID
def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

# ITEMS
# Fungsi untuk membuat item baru dalam database
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Fungsi untuk mengambil semua item dari database
def get_items(db:Session):
    return db.query(models.Item).all()

# Fungsi untuk mengambil satu item berdasarkan ID
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

# Fungsi untuk memperbarui data item berdasarkan ID
def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db_item.name = item.name
        db_item.description = item.description
        db.commit()
        db.refresh(db_item)
    return db_item

# Fungsi untuk menghapus item berdasarkan ID
def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item