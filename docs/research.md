# Research

Below this is just a bunch of information, not very well organized for checking out at a later time


https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Projects/FModuleDescriptor
https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Projects/FProjectDescriptor
https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Projects/FPluginDescriptor
https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-build-tool-target-reference
https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-automation-tool-for-unreal-engine
https://dev.epicgames.com/documentation/en-us/unreal-engine/buildgraph-script-tasks-reference-for-unreal-engine#pakfile
https://dev.epicgames.com/documentation/en-us/unreal-engine/create-an-automation-project-in-unreal-engine#addcodetoanautomationscript




 	TArray< FModuleDescriptor > 	Modules 	List of all modules associated with this project
Public variable 	TArray< FPluginReferenceDescriptor >


 	

FModuleDescriptor ( const FName InName,
EHostType::Type InType,
ELoadingPhase::Type InLoadingPhase
)

	namespace EHostType  
	{  
	    enum Type  
	    {  
	        Runtime,  
	        RuntimeNoCommandlet,  
	        RuntimeAndProgram,  
	        CookedOnly,  
	        UncookedOnly,  
	        Developer,  
	        DeveloperTool,  
	        Editor,  
	        EditorNoCommandlet,  
	        EditorAndProgram,  
	        Program,  
	        ServerOnly,  
	        ClientOnly,  
	        ClientOnlyNoCommandlet,  
	        Max,  
	    }  
	}  

 		namespace ELoadingPhase  
	{  
	    enum Type  
	    {  
	        EarliestPossible,  
	        PostConfigInit,  
	        PostSplashScreen,  
	        PreEarlyLoadingScreen,  
	        PreLoadingScreen,  
	        PreDefault,  
	        Default,  
	        PostDefault,  
	        PostEngineInit,  
	        None,  
	        Max,  
	    }  
	}  

FPluginReferenceDescriptor ( const FString& InName,
bool bInEnabled
)




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
plugins need uplugin
plugins need icon file

	{
	    "FileVersion" : 3,
	    "Version" : 1,
	    "VersionName" : "1.0",
	    "FriendlyName" : "UObject Example Plugin",
	    "Description" : "An example of a plugin which declares its own UObject type.  This can be used as a starting point when creating your own plugin.",
	    "Category" : "Examples",
	    "CreatedBy" : "Epic Games, Inc.",
	    "CreatedByURL" : "http://epicgames.com",
	    "DocsURL" : "",
	    "MarketplaceURL" : "",
	    "SupportURL" : "",
	    "EnabledByDefault" : true,
	    "CanContainContent" : false,
	    "IsBetaVersion" : false,
	    "Installed" : false,
	    "Modules" :
	    [
	        {
	            "Name" : "UObjectPlugin",
	            "Type" : "Developer",
	            "LoadingPhase" : "Default"
	        }
	    ]
	}

    The descriptor file is a JSON-formatted list of variables from the FPluginDescriptor type. There is one additional field, "FileVersion", which is the only required field in the structure. "FileVersion" gives the version of the Plugin descriptor file, and should usually set to the highest version that is allowed by the Engine (currently, this is "3"). Because this version applies to the format of the Plugin Descriptor File, and not the Plugin itself, we do not expect that it will change very frequently, and it should not change with subsequent releases of your Plugin. For maximum compatibility with older versions of the Engine, you can use an older version number, but this is not recommended.

    https://dev.epicgames.com/documentation/en-us/unreal-engine/plugins-in-unreal-engine


Engine:
    [Unreal Engine Root Directory]/Engine/Plugins/[Plugin Name]/

Uproject:
    [Project Root Directory]/Plugins/[Plugin Name]/

"You can also organize Plugins into subdirectories under the base Plugins folder. The engine will scan all of your sub-folders under the base Plugins folder for Plugins to load, but it will never scan subdirectories beneath a Plugin that has already been found."

"Plugins that do not have a Source folder are ignored by the project generator and will not appear in your C++ project files, but they will still be loaded at start-up as long as binary files exist."

"At present, Plugin configuration files are not packaged with projects. This may be supported in the future, but currently requires manually copying the files to the project's Config folder."


For Plugins that contain code, the "Modules" field in the descriptor file will contain at least one entry. An example entry follows:

{
    "Name" : "UObjectPlugin",
    "Type" : "Developer"
    "LoadingPhase" : "Default"
}

Each entry requires the "Name" and "Type" fields. "Name" is the unique name of the Plugin Module that will be loaded with the Plugin. At runtime, the Engine will expect appropriate Plugin binaries to exist in the Plugin's "Binaries" folder with the specified Module name. For Modules that have a Source directory, a matching ".Build.cs" file much exist within the Module's subfolder tree. "Type" sets the type of Module. Valid options are Runtime, RuntimeNoCommandlet, Developer, Editor, EditorNoCommandlet, and Program. This type determines which types of applications can load the Module. For example, some plugins may include modules that should only load when the Editor is running. Runtime modules will be loaded in all cases, even in shipped games. Developer modules will only be loaded in development runtime or Editor builds, but never in shipping builds. Editor modules will only be loaded when the editor is starting up. Your Plugin can use a combination of modules of different types.

Along with the descriptor file, Plugins need an icon to display in the Editor's Plugin Browser. The image should be a 128x128 .png file called "Icon128.png" and kept in the Plugin's "/Resources/" directory.


