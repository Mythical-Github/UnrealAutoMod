<h1 id="title" align="left">UnrealAutoMod</h1>

Easy To Use Modding Utility For Unreal Engine Games

<h2>Project Example:</h2>

<img src="https://github.com/Mythical-Github/UnrealAutoMod/assets/67753356/54364be3-08fc-4fa3-ae6a-bd771c417182" alt="project-screenshot">

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

*   Choose a game preset name and a preset name, this will be passed to the program later on
*   Copy and paste the template "UnrealAutoMod/assets/templates/settings.json" to "UnrealAutoMod/presets/your_game_name/your_preset_name/settings.json" 
*   Setup your game's settings.json for modding using these two pages as reference
*   [Settings Json Reference](https://github.com/Mythical-Github/UnrealAutoMod/blob/dev/docs/settings_json.md)
*   [Enums Reference](https://github.com/Mythical-Github/UnrealAutoMod/blob/dev/docs/enums.md)

<h2>🏃 Running Steps:</h2>

```
UnrealAutoModCLI.exe default default test_mods_all
UnrealAutoModCLI.exe default default test_mods <mod_name> [<mod_name> ...]
```
```
__main__.py default default test_mods_all
__main__.py default default test_mods <mod_name> [<mod_name> ...]
```

<h2>💻 Built with</h2>

*   Python

<h2>🛡️ License:</h2>

[![license](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](LICENSE)
