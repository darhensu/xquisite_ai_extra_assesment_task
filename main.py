# file utama API

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud 
from database import engine, SessionLocal, Base

# inisialisasi database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Endpoint root (beranda)
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

# dependency untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE - Tambah kategori baru
@app.post("/categories/", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

# READ - List semua kategori
@app.get("/categories/", response_model=list[schemas.CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db=db)

# READ - Get kategori berdasarkan ID
@app.get("/categories/{category_id}", response_model=schemas.CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

# UPDATE - Perbarui kategori berdasarkan ID
@app.put("/categories/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.update_category(db=db, category_id=category_id, category=category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

# DELETE - Hapus kategori berdasarkan ID
@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.delete_category(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted"}
    
# CREATE
@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

# READ - list semua item
@app.get("/items/", response_model=list[schemas.ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db=db)

# READ - get item berdasarkan ID
@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# UPDATE
@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db=db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}

    # uvicorn main:app --reload
    # http://127.0.0.1:8000/docs
