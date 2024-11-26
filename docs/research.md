# Research

Below this is just a bunch of information, not very well organized for checking out at a later time

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


Microsoft Windows [Version 10.0.19045.5131]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Mythical>D:\unreal_engine_installs\UE_4.22\Engine\Binaries\Win64\UnrealFrontend.exe -help

C:\Users\Mythical>D:\unreal_engine_installs\UE_4.22\Engine\Binaries\Win64\BuildPatchTool.exe -help
LogBuildPatchTool: Display: -help can be added with any mode selection to get extended information.
LogBuildPatchTool: Display: Supported modes are:
LogBuildPatchTool: Display:   -mode=PatchGeneration      Mode that generates patch data for the a new build.
LogBuildPatchTool: Display:   -mode=ChunkDeltaOptimise   Mode that produces a more optimal chunked patch between two specific builds.
LogBuildPatchTool: Display:   -mode=Compactify           Mode that can clean up unneeded patch data from a given cloud directory with redundant data.
LogBuildPatchTool: Display:   -mode=Enumeration          Mode that outputs the paths to referenced patch data given a single manifest.
LogBuildPatchTool: Display:   -mode=MergeManifests       Mode that can combine two manifest files to create a new one, primarily used to create hotfixes.
LogBuildPatchTool: Display:   -mode=DiffManifests        Mode that can diff two manifests and outputs what chunks would need to be downloaded and some stats.
LogBuildPatchTool: Display:   -mode=PackageChunks        Mode that packages data required for an installation into larger files which can be used as local sources for build patch installers.
LogBuildPatchTool: Display:   -mode=VerifyChunks         Mode that allows you to verify the integrity of patch data. It will load chunk or chunkdb files to verify they are not corrupt.

ResavePluginDescriptors
ResaveProjectDescriptors

HAS NO HELP MESSAGE:
Build
BuildDerivedDataCache

------------------------------------------------------------------------------------------------