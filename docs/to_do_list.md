# UnrealAutoMod To-Do List

## Features

- [ ] Close game hotkey
- [ ] Run script again hotkey
- [ ] Bring Unreal Engine to front hotkey
- [ ] Bring game to front hotkey
- [ ] Close all hotkey (game, engine, and instances of UAM)
- [ ] Unversioned per mod instead of global
- [ ] Engine pak making compression variants (different types, in one run), defaults to compressed currently
- [ ] Switch to `pathlib` from strings
- [ ] Loose file copying / original game file tracker to alleviate loose modding issues
- [ ] Improve validation steps
- [ ] sometimes people will not have internet, account for this, example, with repak installer
- [ ] performance profiler
- [ ] use symlinks when possible to save time
- [ ] if people mess up in editor their setup for chunking, end no pak chunk num pak is genned, error occurs, account for this
- [ ] headless produces no logs, fix this (pyw)
- [ ] multithreaded/processing command queues
- [ ] documentation github pages styling

  cli help replies and such are not colorized
  create mod releases
  create mod releases all
  create mods
  create mods all

build script doesn't auto place all exes in the output dir only the main, not the background

# later
for install apps, optional bool flag to open after install
open uproject
generate project files
switch ue version inside of project

fix github pages stuff
script state cleanup, rename to hooks
update feature list in docs
toggle engine logic needs to be rethought, saves memory and time but make optional and work on more stuff
make tests/ways to test which combination of args and stuff for the uat running is fastest/best
multiple cleanup types:
full
cooked content dirs
cleanup build files
