from . import Module
from enum import Enum
from wiigames_categorizer.models import DiscGame, Category


class PlayerCategories(Enum):
    ONE = "Single player"
    TWO = "Two players"
    THREE = "Three players"
    FOUR = "Four players"


class PlayercountModule(Module):
    def init_categories(self) -> None:
        enums = list(PlayerCategories)
        last_category_id = len(self.usbgx.categories.category)
        self.categories = [
            Category(id=f"{last_category_id + i:02}", name=enums[i]) for i in range(4)
        ]

        self.usbgx.categories.category.extend(self.categories)

    def apply_category(self, game: DiscGame) -> list[Category]:
        wii_game = self.wii_games[game.id]
        players = int(wii_game.input.players) if int(wii_game.input.players) < 5 else 4

        return [self.categories[players - 1]]

    def __str__(self) -> str:
        return "Player count category. Single/Two/Three/Four players"
