<h1 id="title" align="left">UnrealAutoMod</h1>

Easy To Use Modding Utility For Unreal Engine Games

<h2>Project Example:</h2>

[![Project Screenshot](https://github.com/Mythical-Github/UnrealAutoMod/assets/67753356/d36ab78e-af8d-4086-8ad9-fd6f39bba453.png)](https://github.com/Mythical-Github/UnrealAutoMod/assets/67753356/d36ab78e-af8d-4086-8ad9-fd6f39bba453.mp4)

<h2>💪 Features</h2>

*   supports unreal game versions 4.0-5.4
*   supports loose file modding
*   supports iostore pak modding
*   automatic mod creation
*   automatic cooking/packaging
*   automatic process management
*   automatic window management
*   automatic game launching
*   automatic editor launching
*   automatic exe launching
*   script state system, for various automatic utilities
*   supports games with alternative packing dir structures (example game: Kingdom Hearts 3)
*   supports packing manually edited files, through the persistent directory
*   supports various packing type enums, for easily specifying which files end up in mods
*   supports unreal_pak, repak, engine made paks, and loose file mod creation
*   parameter loading for various functions (engine launch, engine cook, etc...)


<h2>🛠️ Installation Steps:</h2>

*   Download and unzip the latest [release](https://github.com/Mythical-Github/UnrealAutoMod/releases)
*   Setup your game's settings.json for modding using these two pages as reference, you can edit manually or through cli args
*   [Settings Json Reference](https://github.com/Mythical-Github/UnrealAutoMod/blob/main/assets/docs/settings_json.md)
*   [Enums Reference](https://github.com/Mythical-Github/UnrealAutoMod/blob/main/assets/docs/enums.md)

<h2>🏃 Running Steps:</h2>

```
UnrealAutoModCLI.exe -h
```
```
UnrealAutoModCLI.exe command -h
```
```
UnrealAutoModCLI.exe test_mods_all settings.json
```
```
UnrealAutoModCLI.exe test_mods settings.json <mod_name> [<mod_name> ...]
```
```
__main__.py -h
```
```
__main__.py command -h
```
```
__main__.py test_mods_all settings.json
```
```
__main__.py test_mods settings.json <mod_name> [<mod_name> ...]
```

<h2>💻 Built with</h2>

*   Python

<h2>🛡️ License:</h2>

[![license](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](LICENSE)
