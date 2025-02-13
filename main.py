# file utama API

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud 
from database import engine, SessionLocal, Base

# inisialisasi database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield fb
    finally:
        db.close()


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
def read_item(otem_id: int, db: Session = Depends(get_db)):
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