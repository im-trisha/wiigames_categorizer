from . import Module
from wiigames_categorizer.models import DiscGame, Category


class DeveloperModule(Module):
    def __init__(self, developer: str) -> None:
        self.developer = developer

    def init_categories(self) -> None:
        last_category_id = len(self.usbgx.categories.category)
        self.categories = [Category(id=f"{last_category_id:02}", name=self.developer)]

        self.usbgx.categories.category.extend(self.categories)

    def apply_category(self, game: DiscGame) -> list[Category]:
        wii_game = self.wii_games[game.id]
        return self.categories if wii_game.developer == self.developer else []

    def __str__(self) -> str:
        return f"Developer {self.developer}"


class PublisherModule(Module):
    def __init__(self, publisher: str) -> None:
        self.publisher = publisher

    def init_categories(self) -> None:
        last_category_id = len(self.usbgx.categories.category)
        self.categories = [Category(id=f"{last_category_id:02}", name=self.publisher)]

        self.usbgx.categories.category.extend(self.categories)

    def apply_category(self, game: DiscGame) -> list[Category]:
        wii_game = self.wii_games[game.id]
        return self.categories if wii_game.publisher == self.publisher else []

    def __str__(self) -> str:
        return f"Publisher {self.publisher}"


class DeveloperAndPublisherModule(Module):
    def __init__(self, developer: str, publisher: str) -> None:
        self.developer = developer
        self.publisher = publisher

    def init_categories(self) -> None:
        last_category_id = len(self.usbgx.categories.category)

        name = (
            f"{self.developer}-{self.publisher}"
            if self.developer != self.publisher
            else self.publisher
        )

        self.categories = [Category(id=f"{last_category_id:02}", name=name)]

        self.usbgx.categories.category.extend(self.categories)

    def apply_category(self, game: DiscGame) -> list[Category]:
        wii_game = self.wii_games[game.id]
        is_correct = (
            wii_game.publisher == self.publisher or wii_game.developer == self.developer
        )
        return self.categories if is_correct else []

    def __str__(self) -> str:
        return f"Either developer {self.developer} or publisher {self.publisher}"
