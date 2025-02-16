# operasi CRUD

from sqlalchemy.orm import Session
import models, schemas

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
    return db.qury(models.Item).filter(models.Item.id == item_id).first()

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