from . import USBGXModel, Field

class Category(USBGXModel):
    id: str = Field(alias="@ID")
    name: str = Field(alias="@Name")

class Categories(USBGXModel):
    category: list[Category] = Field(alias="Category")
    