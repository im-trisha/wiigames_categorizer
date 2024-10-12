from abc import ABC, abstractmethod
from wiigames_categorizer.models import WiiTDBGame, USBLoaderGX, DiscGame, Category


def _get_game_by_id(games: list[WiiTDBGame], game_id: str) -> WiiTDBGame | None:
    matching_games = [game for game in games if game.id == game_id]
    return matching_games[0] if matching_games else None


class Module(ABC):
    initialized = False

    wii_games: dict[str, WiiTDBGame]
    usbgx: USBLoaderGX

    @classmethod
    def initialize(
        cls,
        wii_games: list[WiiTDBGame],
        usbgx: USBLoaderGX,
        disc_games: list[DiscGame],
    ):
        if not cls.initialized:
            cls.usbgx = usbgx
            cls.wii_games = {
                game.id: _get_game_by_id(wii_games, game.id) for game in disc_games
            }

    @abstractmethod
    def init_categories(self) -> None:
        pass

    @abstractmethod
    def apply_category(self, game: DiscGame) -> list[Category]:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
