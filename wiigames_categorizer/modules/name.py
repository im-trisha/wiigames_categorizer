from . import Module
from wiigames_categorizer.models import DiscGame, Category

_CATEGORY_NAME = "{name} Games"


class NameModule(Module):
    def __init__(self, contains: str) -> None:
        self.contains = contains

    def init_categories(self) -> None:
        last_category_id = len(self.usbgx.categories.category)

        name = self.contains if self.contains else self.exact
        self.categories = [
            Category(id=f"{last_category_id:02}", name=_CATEGORY_NAME.format(name=name))
        ]

        self.usbgx.categories.category.extend(self.categories)

    def apply_category(self, game: DiscGame) -> list[Category]:
        return self.categories if self.contains.lower() in game.title.lower() else []

    def __str__(self) -> str:
        return f"Containing the word '{self.contains}'"
