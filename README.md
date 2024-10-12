# USB Loader GX categorizer

### Index
- [Installing](#installing)
- [Usage](#usage)
- [Configuration](#configuration)
- [Help](#help)
- [Contributing](#contributing)
- [Credits](#credits)
- [Disclaimer](#disclaimer)

### Installing
In order to install USB Loader GX categorizer, you just need to clone this repo, then rename the .env.example file to .env, if you are on linux just run `mv .env.example .env`

You can then do one of the following commands to run it:

- If you have docker installed:
```sh
docker compose up --build
```
- If you have poetry installed:
```
poetry install
poetry run python -m wiigames_categorizer
```
 
### Usage
Its fairly simple, at the moment there are the following category modules, and each one of them can be used as you please:
- AllModule: The default USB Loader GX category. Must always be used (as the first module, possibly)
- DeveloperModule: This will create a category for a certain game developer, e.g. `DeveloperModule("Nintendo")`
- PublisherModule: This will create a category for a certain game publisher, e.g. `PublisherModule("Nintendo")`
- DeveloperAndPublisherModule: This will create a category for either a game developer or publisher, e.g. `DeveloperAndPublisherModule("Nintendo", "Nintendo")`, this will match games with `Nintendo` as either a developer or publisher
- GenreModule: This will match a certain game genre, you can watch the entire list under assets/wiitdb.xml
- NameModule: This will match every game containing the input, e.g. `NameModule("Mario")` will match every `Mario` game
- PlayercountModule: This will create a category for Single/Two/Three/Four player games.
You can add as many as you'd like under `wiigames_categorizer/__main__.py` in the use_modules variable.

You then need to input a game list inside the assets folder, at the moment, the only possible format I know of is disc.info provided by [WiiBackupManager](https://wiibackupmanager.co.uk/). If you know any easier or better way to do it, please notice me. (A possibility could be the game list provided by USB Loader GX, but I'm still considering it)

After putting disc.info inside assets, delete the first line so that the first line contains a game id, e.g. `[SMNP01]`

You can now run the script using the commands in the [Usage section](#usage), then, head into the output directory, copy the `GXGameCategories.xml` file and paste it inside `SDDrive:/apps/usbloader_gx

### Configuration

There is nothing to configure, really, but if you want to output the `GXGameCategories.xml` file directly into the sd, you can customize the `OUTDIR` in the .env file.


### Help
Well, if you have any issue, please notice me in the issues section! I'll gladly help you

### Contributing
Feel free to contribute! I'll love some help, so make a PR or just open an issue asking for a feature! :)

### Credits
Well, thanks for gametdb for the database! I took it from my SD, kindly downloaded by USB Loader GX. I don't know if there is any way to download it and I've already used too much time of my life to write this README honestly. I'm probably gonna be the only one using, touching or ever seeing this code. Love y'all!

### Disclaimer
TL;DR: I dont really care for anything that happens to you or your Wii, Dont pirate games, you must own them and I don't know Nintendo in any way.

All the games installed in your Homebrew channel and then loaded using USB Loader GX must be owned. I do not take any responsibility for your actions and no contributor of this repository is liable for damage you may cause to your Wii/Homebrew.

Im not in any way affiliated with Nintendo®

This should be everything, I guess.