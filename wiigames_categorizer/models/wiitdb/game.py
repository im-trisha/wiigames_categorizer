from pydantic import BaseModel, Field
from typing import Union, Optional

class Locale(BaseModel):
    lang: str = Field(alias='@lang')
    title: str
    synopsis: Optional[str]

class Date(BaseModel):
    year: str = Field(alias='@year')
    month: str = Field(alias='@month')
    day: str = Field(alias='@day')

class Rating(BaseModel):
    type: str = Field(alias='@type')
    value: Optional[str] = Field(alias='@value', default='')

class WiFi(BaseModel):
    players: str = Field(alias='@players')

class Control(BaseModel):
    type: str = Field(alias='@type')
    required: bool = Field(alias='@required')

class Input(BaseModel):
    players: str = Field(alias='@players')
    control: Optional[Union[Control, list[Control]]] = Field(default=None)

class Rom(BaseModel):
    version: Optional[str] = Field(alias='@version')
    name: Optional[str] = Field(alias='@name', default='')
    size: Optional[str] = Field(alias='@size', default='')

class WiiTDBGame(BaseModel):
    name: str = Field(alias='@name')
    id: str
    type: Optional[str] = Field(default='')
    region: Optional[str] = Field(default='')
    languages: Optional[str] = Field(default='')
    locale: Optional[Union[Locale, list[Locale]]] = Field(default=None)
    developer: Optional[str] = Field(default='')
    publisher: Optional[str] = Field(default='')
    date: Date
    genre: Optional[str] = Field(default='')
    rating: Rating
    wi_fi: WiFi = Field(alias='wi-fi')
    input: Union[Input, list[Input]]
    rom: Union[Rom, list[Rom]]