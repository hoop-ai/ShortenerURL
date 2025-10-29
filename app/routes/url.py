from fastapi import APIRouter, Depends, HTTPException, Path, status
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


@router.post("/shorten", response_model=schemas.URLInfo, status_code=status.HTTP_200_OK)
def shorten_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    short_code = utils.generate_short_code()

    while db.query(models.URL).filter_by(short_code=short_code).first():
        short_code = utils.generate_short_code()

    new_url = models.URL(original_url=str(
        url.original_url), short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {"short_url": f"http://localhost:8000/r/{new_url.short_code}"}


@router.get(
    "/r/{short_code}",
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Short URL not found"},
        status.HTTP_307_TEMPORARY_REDIRECT: {"description": "Redirect to original URL"},
        status.HTTP_422_UNPROCESSABLE_CONTENT: {"description": "Invalid short code format"},
    },
)
def redirect_url(
    short_code: str = Path(
        ...,
        min_length=1,
        max_length=12,
        pattern=r"^[A-Za-z0-9]+$",
        description="Alphanumeric short code (1-12 chars)",
    ),
    db: Session = Depends(get_db),
):
    db_url = db.query(models.URL).filter_by(short_code=short_code).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    db_url.clicks += 1
    db.commit()
    return RedirectResponse(url=db_url.original_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
