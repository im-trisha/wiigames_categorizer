import logging
import itertools
import time
from wiigames_categorizer.modules import *
from wiigames_categorizer.models import Game
from wiigames_categorizer.configs import get_configs, dump_categories, init_logger

use_modules: list[Module] = [
    AllModule(),
    PlayercountModule(),
    DeveloperAndPublisherModule("Nintendo", "Nintendo"),
    PublisherModule("Namco Bandai Games"),
    NameModule("Mario"),
    GenreModule(["music", "rhythm"]),
    GenreModule(["strategy"]),
    GenreModule(["action"]),
]

init_logger()
logger = logging.getLogger(__loader__.name)


def main() -> None:
    logger.info("Loading configurations...")

    start = time.time()
    wii_games, usbgx, disc_games = get_configs()
    end = time.time()

    logger.info(f"Configurations loaded, took {end - start:.2f}s.")

    logger.info("Initializing modules...")
    Module.initialize(wii_games, usbgx, disc_games)

    for module in use_modules:
        module.init_categories()
    logger.info("Modules initialized.")

    logger.info("Applying categories to games...")
    for game in disc_games:
        if not Module.wii_games[game.id]:
            logging.warning(f"Game {game.id} was not found on WiiTDB. Skipping...")

        categories = [module.apply_category(game) for module in use_modules]
        usbgx.game_categories.games.append(
            Game(
                id=game.id,
                title=game.title,
                categories=list(itertools.chain.from_iterable(categories)),
            )
        )
    logger.info("Categories applied.")

    logger.info("Dumping categories to output dir...")

    dump_categories(usbgx)
    logger.info("Categories dumped.")


if __name__ == "__main__":
    logger.info("Welcome to the Wii games categorizer. Here are the current modules:")

    logger.info("")
    for module in use_modules:
        logger.info(module)
    logger.info("")

    main()
    logger.info("Bye bye!")
