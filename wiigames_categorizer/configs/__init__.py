import xmltodict
import configparser
import pathlib
import logging
import os

from wiigames_categorizer.models import (
    settings,
    USBLoaderGX,
    WiiTDBGame,
    DiscGame,
    Categories,
    GameCategories,
)

OUTDIR = "./output"
ASSETS_DIR = "./assets"


def init_logger() -> None:
    logging.basicConfig(format=settings.LOGGING_FORMAT, level=logging.INFO)


def get_configs() -> tuple[list[WiiTDBGame], USBLoaderGX, list[DiscGame]]:
    wiitdb_path = pathlib.Path(ASSETS_DIR) / settings.WIITDB_NAME
    with open(wiitdb_path, "r", encoding="utf-8") as f:
        wiitdb = xmltodict.parse(f.read())
        games = [WiiTDBGame.model_validate(game) for game in wiitdb["datafile"]["game"]]

    usbloadergx = USBLoaderGX(
        revision="1281",
        categories=Categories(category=[]),
        game_categories=GameCategories(games=[]),
    )

    config = configparser.ConfigParser()
    config.read(pathlib.Path(ASSETS_DIR) / settings.DISCINFO_NAME)

    disc_config = {
        section: dict(config.items(section)) for section in config.sections()
    }
    disc_games = [
        DiscGame.model_validate({"id": id, **disc_config[id]}) for id in disc_config
    ]

    return games, usbloadergx, disc_games


def dump_categories(usbgx: USBLoaderGX) -> None:
    with_root = {"USBLoaderGX": usbgx.model_dump(by_alias=True)}
    usbgx_xml = xmltodict.unparse(with_root, pretty=True)

    os.makedirs(OUTDIR, exist_ok=True)
    output_path = pathlib.Path(OUTDIR) / "GXGameCategories.xml"
    with open(output_path, "w") as f:
        f.write(usbgx_xml)
