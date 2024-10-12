from typing import Optional
from . import USBGXModel, Categories, GameCategories, Field


class USBLoaderGX(USBGXModel):
    revision: str = Field(alias="Revision")
    categories: Categories = Field(alias="Categories")
    game_categories: Optional[GameCategories] = Field(alias="GameCategories")
