from typing import Union, Optional
from . import USBGXModel, Field, Category

class Game(USBGXModel):
    id: str = Field(alias="@ID")
    title: str = Field(alias="@Title")
    categories: list[Category] = Field(alias="Category")

class GameCategories(USBGXModel):
    games: Optional[Union[Game, list[Game]]] = Field(alias="Game")
