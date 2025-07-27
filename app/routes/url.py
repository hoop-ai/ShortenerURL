from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from .. import models, schemas, utils, database

router = APIRouter()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/shorten", response_model=schemas.URLInfo)
def shorten_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    short_code = utils.generate_short_code()

    while db.query(models.URL).filter_by(short_code=short_code).first():
        short_code = utils.generate_short_code()

    new_url = models.URL(original_url=str(
        url.original_url), short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {"short_url": f"http://localhost:8000/{new_url.short_code}"}


@router.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter_by(short_code=short_code).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    db_url.clicks += 1
    db.commit()
    return RedirectResponse(url=db_url.original_url)
