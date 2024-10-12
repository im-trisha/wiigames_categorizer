from . import Module
from wiigames_categorizer.models import DiscGame, Category


class GenreModule(Module):
    def __init__(self, genres: list[str]) -> None:
        assert len(genres) > 0
        self.genres = genres
        self.genres_names = "-".join([genre.capitalize() for genre in self.genres])

    def init_categories(self) -> None:
        last_category_id = len(self.usbgx.categories.category)
        self.categories = [
            Category(id=f"{last_category_id:02}", name=self.genres_names)
        ]

        self.usbgx.categories.category.extend(self.categories)

    def apply_category(self, game: DiscGame) -> list[Category]:
        wii_game = self.wii_games[game.id]

        game_genres = [genre.strip() for genre in wii_game.genre.split(",")]
        has_any = len(set(self.genres).intersection(game_genres)) > 0

        return self.categories if has_any else []

    def __str__(self) -> str:
        return f"With the genres: {self.genres_names}"
