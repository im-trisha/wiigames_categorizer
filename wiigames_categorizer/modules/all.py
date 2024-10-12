from . import Module
from wiigames_categorizer.models import DiscGame, Category

_ALL_CATEGORY_NAME = "All"


class AllModule(Module):
    def init_categories(self) -> None:
        last_category_id = len(self.usbgx.categories.category)
        self.categories = [
            Category(id=f"{last_category_id:02}", name=_ALL_CATEGORY_NAME)
        ]

        self.usbgx.categories.category.extend(self.categories)

    def apply_category(self, game: DiscGame) -> list[Category]:
        return self.categories

    def __str__(self) -> str:
        return f"All games"
