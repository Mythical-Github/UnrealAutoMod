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
- [ ] multithreaded/processing command queues
- [ ] documentation github pages styling


  create mods
  create mods all
  create mod releases
  create mod releases all

build script doesn't auto place all exes in the output dir only the main, not the background

# later
for install apps, optional bool flag to open after install
open uproject
generate project files
switch ue version inside of uproject json

fix github pages stuff
hook state cleanup
update feature list in docs
toggle engine logic needs to be rethought, saves memory and time but make optional and work on more stuff
make tests/ways to test which combination of args and stuff for the uat running is fastest/best
cli help replies and such are not colorized




Automation Help:

Executes scripted commands

AutomationTool.exe [-verbose] [-compileonly] [-p4] Command0 [-Arg0 -Arg1 -Arg2 ...] Command1 [-Arg0 -Arg1 ...] Command2 [-Arg0 ...] Commandn ... [EnvVar0=MyValue0 ... EnvVarn=MyValuen]

Parameters:

    -verbose                Enables verbose logging
    -nop4                   Disables Perforce functionality (default if not run on a build machine)
    -p4                     Enables Perforce functionality (default if run on a build machine)
    -compileonly            Does not run any commands, only compiles them
    -compile                Dynamically compiles all commands (otherwise assumes they are already built)
    -help                   Displays help
    -list                   Lists all available commands
    -submit                 Allows UAT command to submit changes
    -nosubmit               Prevents any submit attempts
    -nokill                 Does not kill any spawned processes on exit
    -ignorejunk             Prevents UBT from cleaning junk files
    -UseLocalBuildStorage   Allows you to use local storage for your root build storage dir (default of P:\Builds (on PC) is changed to Engine\Saved\LocalBuilds). Used for local testing.
AutomationTool exiting with ExitCode=0 (Success)


BuildPlugin Help:

Builds a plugin, and packages it for distribution

Parameters:

    -Plugin                 Specify the path to the descriptor file for the plugin that should be packaged
    -NoHostPlatform         Prevent compiling for the editor platform on the host
    -TargetPlatforms        Specify a list of target platforms to build, separated by '+' characters (eg. -TargetPlatforms=Win32+Win64). Default is all the Rocket target platforms.
    -Package                The path which the build artifacts should be packaged to, ready for distribution.
    -StrictIncludes         Disables precompiled headers and unity build in order to check all source files have self-contained headers.
    -Unversioned            Do not embed the current engine version into the descriptor
AutomationTool exiting with ExitCode=0 (Success)

C:\Users\Mythical>


ResavePackages
ResavePluginDescriptors
ResaveProjectDescriptors


HAS NO HELP MESSAGE:
Build
BuildDerivedDataCache



symlink main method