from enum import Enum


class WindowAction(Enum):
    NONE = 'none'
    MIN = 'min'
    MAX = 'max'
    MOVE = 'move'
    MOVE_MIN = 'move_min'
    MOVE_MAX = 'move_max'
    CLOSE = 'close'


class PackingType(Enum):
    ENGINE = 'engine'
    UNREAL_PAK = 'unreal_pak'
    REPAK = 'repak'
    LOOSE = 'loose'
    ALT_EXE = 'alt_exe'
    NONE = 'none'


class GameLaunchType(Enum):
    EXE = 'exe'
    STEAM = 'steam'
    EPIC = 'epic'
    ITCH_IO = 'itch_io'
    BATTLE_NET = 'battle_net'
    ORIGIN = 'origin'
    UBISOFT = 'ubisoft'
    
    
class ScriptStateType(Enum):
    All = 'all'
    NONE = 'none'
    INIT = 'init'
    POST_INIT = 'post_init'
    CONSTANT = 'constant'
    PRE_PACKAGING = 'pre_packaging'
    POST_PACKAGING = 'post_packaging'
    PRE_PAK_CREATION = 'pre_pak_creation'
    POST_PAK_CREATION = 'post_pak_creation'
    PRE_PAK_MOVING = 'pre_pak_moving'
    POST_PAK_MOVING = 'post_pak_moving'
    PRE_GAME_LAUNCH = 'pre_game_launch'
    POST_GAME_LAUNCH = 'post_game_launch'
    POST_GAME_CLOSE = 'post_game_close'
    

class ExecutionMode(Enum):
    SYNC = 'sync'
    ASYNC = 'async'


class PackagingDirType(Enum):
    WINDOWS = 'windows'
    WINDOWS_NO_EDITOR = 'windows_no_editor'


class ScriptArg(Enum):
    TEST_MODS_ALL = 'test_mods_all'
    TEST_MODS = 'test_mods'


class RepakCompressionType(Enum):
    NONE =  'None'
    ZLIB =  'Zlib'
    GZIP = 'Gzip'
    OODLE = 'Oodle'
    ZSTD = 'Zstd'


class RepakVersionType(Enum):
    v1 = None
    v2 = '2' # 4.0-4.2
    v3 = '3' # 4.3-4.15
    v4 = '4' # 4.16-4.19
    v5 = '5' # 4.20
    v6 =  None
    v7 = '7' # 4.21
    v8a = '8A' # 4.22
    v8b = '8B' # 4.23-4.24
    v9 = '9' # 4.25
    v10 = None
    v11 = '11' # 4.26-5.3


class UnrealModTreeType(Enum):
    CUSTOM_CONTENT = 'custom_content' # "Content/CustomContent/ModName"
    MODS = 'mods' # "Content/Mods/ModName"


class FileInclusionType(Enum):
    ASSET_PATH = 'asset_path' # Takes the path and gets all files regardless of extension and includes them
    TREE = 'tree' # Takes supplied dir, and traverses it all, including every file
