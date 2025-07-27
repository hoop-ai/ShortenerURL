from pydantic import BaseModel, HttpUrl, ConfigDict


class URLBase(BaseModel):
    original_url: HttpUrl


class URLInfo(BaseModel):
    short_url: str

    model_config = ConfigDict(from_attributes=True)
