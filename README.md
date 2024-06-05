## Settings Json Documentation

## General Info
- **Override Default Working Directory**: 
  - **Description**: Specifies if you want the folder that gets turned into paks to be in a specific place. Defaults to next to the exe/py.
  - **Value**: `false` (true/false)
- **Working Directory**:
  - **Description**: Directory for the override if used.
  - **Value**: `"C:/Users/Mythical/Downloads/Output"`
- **Window Title**:
  - **Description**: Title for the script window, useful for the auto move windows section.
  - **Value**: `"UnrealAutoMod Automation Script"`

## Engine Info
- **Unreal Engine Directory**:
  - **Description**: Path to the Unreal Engine installation directory.
  - **Value**: `"D:/unreal_engine_installs/UE_4.22"`
- **Unreal Project File**:
  - **Description**: Path to the Unreal project file (.uproject).
  - **Value**: `"C:/Users/Mythical/Documents/Github/InterposePrivate/unreal_project/Interpose/KevinSpel.uproject"`
- **Toggle Engine During Testing**:
  - **Description**: Whether to toggle the engine on and off during testing.
  - **Value**: `false` (true/false)
- **Resave Packages and Fix Up Redirectors Before Engine Open**:
  - **Description**: Whether to resave packages and fix up redirectors before opening the engine.
  - **Value**: `true` (true/false)
- **Engine Launch Args**:
  - **Description**: Additional arguments for engine launch.
  - **Value**: `[]`
- **Engine Cook and Packaging Args**:
  - **Description**: Additional arguments for cooking and packaging.
  - **Value**: `[]`
- **Use Unversioned Cooked Content**:
  - **Description**: Use unversioned cooked content.
  - **Value**: `true` (true/false)
- **Clear .uproject Saved Cooked Directory Before Tests**:
  - **Description**: Clear the saved cooked directory before tests.
  - **Value**: `false` (true/false)
- **Always Build Project**:
  - **Description**: Always build the project.
  - **Value**: `false` (true/false)
- **Override Automatic Version Finding**:
  - **Description**: Override the automatic version finding.
  - **Value**: `false` (true/false)
- **Unreal Engine Major Version**:
  - **Description**: Major version of the Unreal Engine.
  - **Value**: `"4"`
- **Unreal Engine Minor Version**:
  - **Description**: Minor version of the Unreal Engine.
  - **Value**: `"22"`

## Game Info
- **Game Executable Path**:
  - **Description**: Path to the game executable.
  - **Value**: `"D:/SteamLibrary/steamapps/common/Zedfest/KevinSpel/Binaries/Win64/Zedfest.exe"`
- **Launch Type**:
  - **Description**: `can be any of the GameLaunchType enums`
  - **Value**: `"steam"`
- **Override Automatic Launcher Executable Finding**:
  - **Description**: Override the automatic finding of the launcher executable.
  - **Value**: `false` (true/false)
- **Game Launcher Executable**:
  - **Description**: Path to the game launcher executable.
  - **Value**: `"C:/Program Files (x86)/Steam/steam.exe"`
- **Game ID**:
  - **Description**: Steam game ID.
  - **Value**: `1037080`
- **Skip Launching Game**:
  - **Description**: Skip launching the game.
  - **Value**: `false` (true/false)
- **Override Automatic Window Title Finding**:
  - **Description**: Override the automatic window title finding.
  - **Value**: `false` (true/false)
- **Window Title Override String**:
  - **Description**: String to override window title.
  - **Value**: `"Zedfest"`
- **Launch Params**:
  - **Description**: Additional launch parameters.
  - **Value**: `[
      "-fileopenlog",
      "-NOSPLASH"
    ]`

## Alternative .uproject Name in Game Directory
- **Use Alternative Method**:
  - **Description**: Use an alternative method for .uproject naming.
  - **Value**: `false` (true/false)
- **Name**:
  - **Description**: Alternative name for .uproject.
  - **Value**: `"Game"`

## Repak Info
- **Repak Path**:
  - **Description**: Path to the Repak executable.
  - **Value**: `"C:/modding/unreal_engine/repak/repak.exe"`
- **Override Automatic Version Finding**:
  - **Description**: Override automatic version finding.
  - **Value**: `false` (true/false)
- **Repak Version**:
  - **Description**: Version of Repak.
  - **Value**: `"V11"`

## Alternative Executable Methods
- **Example Entry**:
  - **Script State**: `pre_game_launch`: `can be any of the ScriptStateType enums`
  - **Alternative Executable Path**: `"C:/modding/unreal_engine/Umodel/umodel.exe"`
  - **Execution Mode**: `async`: `can be any of the UnrealModTreeType enums`
  - **Variable Args**: `[]`

## Process Kill Info
- **Auto Close Game**:
  - **Description**: Automatically close the game.
  - **Value**: `true` (true/false)
- **Processes to Kill**:
  - **Process Name**: `"Fmodel.exe"`
  - **Use Substring Check**: `false` (true/false)
  - **Script State**: `all`: `can be any of the ScriptStateType enums`

## Auto Move Windows
- **Window Name**: `"UE4SS"`
  - **Use Substring Check**: `true` (true/false)
  - **Window Behaviour**: `move`: `can be any of the WindowAction enums`
  - **Script State**: `post_game_launch`: `can be any of the ScriptStateType enums`
  - **Monitor**: `1`
  - **Resolution**:
    - **X**: `1525`
    - **Y**: `850`

## Mod Pak Info
- **Mod Name**: `"EnginePakExample_P"`
  - **Pak Directory Structure**: `"LogicMods"`
  - **Mod Name Directory Type**: `"Mods"`: `can be any of the UnrealModTreeType enums`
  - **Use Mod Name Directory Name Override**: `false` (true/false)
  - **Mod Name Directory Name Override**: `null`
  - **Pak Chunk Number**: `1`
  - **Packing Type**: `"engine"`: `can be any of the PackingType enums`
  - **Compression Type**: `"None"`: `can be any of the CompressionType enums`
  - **Is Enabled**: `false` (true/false)
  - **Manually Specified Assets**:
    - **Asset Paths**: `[]`
    - **Tree Paths**: `[]`

## Enums Documentation

### WindowAction
Enum for handling window actions.
- **NONE**: 'none'
- **MIN**: 'min'
- **MAX**: 'max'
- **MOVE**: 'move'
- **CLOSE**: 'close'

### PackingType
Enum for how to pack mods.
- **ENGINE**: 'engine'
- **UNREAL_PAK**: 'unreal_pak'
- **REPAK**: 'repak'
- **LOOSE**: 'loose'

### GameLaunchType
Enum for how to launch the game.
- **EXE**: 'exe'
- **STEAM**: 'steam'
- **EPIC**: 'epic'
- **ITCH_IO**: 'itch_io'
- **BATTLE_NET**: 'battle_net'
- **ORIGIN**: 'origin'
- **UBISOFT**: 'ubisoft'
- **OTHER**: 'other'

### ScriptStateType
Enum for the various script states, used to fire off other functions at specific times.
- **NONE**: 'none'
- **PRE_ALL**: 'pre_all'
- **POST_ALL**: 'post_all'
- **CONSTANT**: 'constant'
- **PRE_INIT**: 'pre_init'
- **INIT**: 'init'
- **POST_INIT**: 'post_init'
- **PRE_COOKING**: 'pre_cooking'
- **POST_COOKING**: 'post_cooking'
- **PRE_MODS_UNINSTALL**: 'pre_mods_uninstall'
- **POST_MODS_UNINSTALL**: 'post_mods_uninstall'
- **PRE_PAK_DIR_SETUP**: 'pre_pak_dir_setup'
- **POST_PAK_DIR_SETUP**: 'post_pak_dir_setup'
- **PRE_MODS_INSTALL**: 'pre_mods_install'
- **POST_MODS_INSTALL**: 'post_mods_install'
- **PRE_GAME_LAUNCH**: 'pre_game_launch'
- **POST_GAME_LAUNCH**: 'post_game_launch'
- **PRE_GAME_CLOSE**: 'pre_game_close'
- **POST_GAME_CLOSE**: 'post_game_close'
- **PRE_ENGINE_OPEN**: 'pre_engine_open'
- **POST_ENGINE_OPEN**: 'post_engine_open'
- **PRE_ENGINE_CLOSE**: 'pre_engine_close'
- **POST_ENGINE_CLOSE**: 'post_engine_close'

### ExecutionMode
Enum for how to execute various processes.
- **SYNC**: 'sync'
- **ASYNC**: 'async'

### CompressionType
Enum for the types of mod pak compression.
- **NONE**: 'None'
- **ZLIB**: 'Zlib'
- **GZIP**: 'Gzip'
- **OODLE**: 'Oodle'
- **ZSTD**: 'Zstd'
- **LZ4**: 'Lz4'
- **LZMA**: 'Lzma'

### UnrealModTreeType
Enum for the mod dir type in the Unreal file system.
There are two main conventions used by communities.
- **CUSTOM_CONTENT**: 'CustomContent'  // "Content/CustomContent/ModName"
- **MODS**: 'Mods'  // "Content/Mods/ModName"
