# UnrealAutoMod To-Do List


## Current To Do: 

Things to fix:
Kismet Analyzer Installer
Repak Installer


## To Do:
- [ ] make a list of things to test for, so no need to worry about 1 change breaking any features
- [ ] unit/project tests
- [ ] Close game hotkey
- [ ] Run script again hotkey
- [ ] Bring Unreal Engine to front hotkey
- [ ] Bring game to front hotkey
- [ ] Close all hotkey (game, engine, and instances of UAM)
- [ ] Engine pak making compression variants (different types, in one run), defaults to compressed currently
- [ ] Switch to `pathlib` from strings
- [ ] Improve validation steps
- [ ] sometimes people will not have internet, account for this, example, with repak installer
- [ ] performance profiler
- [ ] if people mess up in editor their setup for chunking, end no pak chunk num pak is genned, error occurs, account for this
- [ ] multithreaded/processing command queues
- [ ] cli help replies and such are not colorized like the rest of the program
- [ ] rethink toggle engine logic
- [ ] validate settings json, json values, and input values better
- [ ] more error handling and print outs
- [ ] clean up hook states and add any missing states
- [ ] non engine iostore


## Commands:
- [ ] change_uproject_name
- [ ] diff game and file list, and backup diff, so later on can cleanup game list and restore from backup
- [ ] generic file list/cleanup tree commands
- [ ] full run command or something, maybe test_mods_all/test_mods alias with slight rework
- [ ] switch_uproject_engine_version
- [ ] create plugin command
- [ ] remove plugin command
- [ ] enable plugin command
- [ ] disable plugin command
- [ ] generate project files for uproject
- [ ] Mod Conflict Checker


## Maybes:
- [ ] UE4SS Installer
- [ ] Loose File Loader Installer
- [ ] unpack/repack game/mods
- [ ] get game engine version command
- [ ] list game/mod contents


## Documentation:
- [ ] update documentation
- [ ] add bug reports section
- [ ] add contributions section
- [ ] add suggestions/feature requests section
- [ ] add socials section like discords
- [ ] documentation github pages styling
- [ ] update feature list in docs
