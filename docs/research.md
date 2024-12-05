# Research


=====================================================================================
below is the log for packaging for iostore on 4.26


Commands.txt

-Output=C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\pakchunk0-WindowsNoEditor.utoc
-ContainerName=pakchunk0 
-ResponseFile="C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\PakListIoStore_pakchunk0.txt"
-Output=RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\pakchunk1-WindowsNoEditor.utoc
-ContainerName=pakchunk1 
-ResponseFile="PakListIoStore_pakchunk1.txt"




Running: 
UE4Editor-Cmd.exe 
RoboQuest.uproject 
-run=IoStore 
-CreateGlobalContainer=RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\global.utoc 
-CookedDirectory=RoboQuest\Saved\Cooked\WindowsNoEditor 
-Commands="C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\IoStoreCommands.txt" 
-patchpaddingalign=2048   
-cryptokeys=RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Metadata\Crypto.json  
-TargetPlatform=WindowsNoEditor 













Running: 
UE4Editor-Cmd.exe 
RoboQuest.uproject 
-run=IoStore 
-CreateGlobalContainer=RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\global.utoc 
-CookedDirectory=RoboQuest\Saved\Cooked\WindowsNoEditor 
-Commands="C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\IoStoreCommands.txt" 
-CookerOrder=C:\Users\Mythical\Documents\GitHub\RoboQuest\Build\WindowsNoEditor\FileOpenOrder\CookerOpenOrder.log 
-patchpaddingalign=2048   
-cryptokeys=RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Metadata\Crypto.json  
-TargetPlatform=WindowsNoEditor 
-abslog=D:\unreal_engine_installs\UE_4.26\Engine\Programs\AutomationTool\Saved\IoStore-2024.12.04-04.00.06.txt 
-stdout 
-CrashForUAT 
-unattended 
-NoLogTimes  
-UTF8Output









LogUObjectHash: Compacting FUObjectHashTables data took   0.43ms
LogSlate: Window 'Unsupported Platform' being destroyed
LogMainFrame: Project does not require temp target
LogLauncherProfile: Found promoted target with matching version at ../../../Engine/Binaries/Win64/UE4Game.target
UATHelper: Packaging (Windows (64-bit)): Running AutomationTool...
UATHelper: Packaging (Windows (64-bit)): Parsing command line: -ScriptsForProject=C:/Users/Mythical/Documents/GitHub/RoboQuest/RoboQuest.uproject BuildCookRun -nocompileeditor -installed -nop4 -project=C:/Users/Mythical/Documents/GitHub/RoboQuest/RoboQuest.uproject -cook -stage -archive -archivedirectory=C:/Users/Mythical/Downloads/Output -package -ue4exe=D:
\unreal_engine_installs\UE_4.26\Engine\Binaries\Win64\UE4Editor-Cmd.exe -ddc=InstalledDerivedDataBackendGraph -iostore -pak -iostore -prereqs -nodebuginfo -manifests -targetplatform=Win64 -clientconfig=Development -utf8output
UATHelper: Packaging (Windows (64-bit)): Setting up ProjectParams for C:\Users\Mythical\Documents\GitHub\RoboQuest\RoboQuest.uproject
UATHelper: Packaging (Windows (64-bit)): ********** COOK COMMAND STARTED **********
UATHelper: Packaging (Windows (64-bit)): Running UE4Editor Cook for project C:\Users\Mythical\Documents\GitHub\RoboQuest\RoboQuest.uproject
UATHelper: Packaging (Windows (64-bit)): Commandlet log file is D:\unreal_engine_installs\UE_4.26\Engine\Programs\AutomationTool\Saved\Cook-2024.12.04-03.59.55.txt
UATHelper: Packaging (Windows (64-bit)): Running: D:\unreal_engine_installs\UE_4.26\Engine\Binaries\Win64\UE4Editor-Cmd.exe C:\Users\Mythical\Documents\GitHub\RoboQuest\RoboQuest.uproject -run=Cook  -TargetPlatform=WindowsNoEditor -fileopenlog -ddc=InstalledDerivedDataBackendGraph -unversioned -manifests -abslog=D:\unreal_engine_installs\UE_4.26\Engine\Progr
ams\AutomationTool\Saved\Cook-2024.12.04-03.59.55.txt -stdout -CrashForUAT -unattended -NoLogTimes  -UTF8Output
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display: Running engine for game: RoboQuest
UATHelper: Packaging (Windows (64-bit)):   LogHAL: Display: Platform has ~ 16 GB [16866865152 / 17179869184 / 16], which maps to Larger [LargestMinGB=32, LargerMinGB=12, DefaultMinGB=8, SmallerMinGB=6, SmallestMinGB=0)
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'AllDesktop'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_ASTC'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_DXT'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_ETC2'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'AndroidClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_ASTCClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_DXTClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_ETC2Client'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_Multi'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_MultiClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'IOSClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'IOS'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Linux'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxNoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxServer'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxAArch64NoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxAArch64Client'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxAArch64Server'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Lumin'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LuminClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'MacNoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Mac'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'MacClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'MacServer'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'TVOSClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'TVOS'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'WindowsNoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Windows'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'WindowsClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'WindowsServer'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Building Assets For WindowsNoEditor
UATHelper: Packaging (Windows (64-bit)):   LogAudioDebug: Display: Lib vorbis DLL was dynamically loaded.
UATHelper: Packaging (Windows (64-bit)):   LogShaderCompilers: Display: Using Local Shader Compiler.
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Max Cache Size: 512 MB
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Loaded Boot cache: C:/Users/Mythical/AppData/Local/UnrealEngine/4.26/DerivedDataCache/Boot.ddc
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Pak cache opened for reading ../../../Engine/DerivedDataCache/Compressed.ddp.
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Performance to C:/Users/Mythical/AppData/Local/UnrealEngine/Common/DerivedDataCache: Latency=0.05ms. RandomReadSpeed=587.96MBs, RandomWriteSpeed=184.37MBs. Assigned SpeedClass 'Local'
UATHelper: Packaging (Windows (64-bit)):   LogAudioCaptureCore: Display: No Audio Capture implementations found. Audio input will be silent.
UATHelper: Packaging (Windows (64-bit)):   LogAudioCaptureCore: Display: No Audio Capture implementations found. Audio input will be silent.
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: CookSettings for Memory: MemoryMaxUsedVirtual 0MiB, MemoryMaxUsedPhysical 16384MiB, MemoryMinFreeVirtual 0MiB, MemoryMinFreePhysical 1024MiB
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Mobile HDR setting 1
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Creating asset registry
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Discovering localized assets for cultures: en
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Clearing all cooked content for platform WindowsNoEditor
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Sandbox cleanup took 0.048 seconds for platforms WindowsNoEditor
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Cooked packages 0 Packages Remain 47 Total 47
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Cook Diagnostics: OpenFileHandles=163, VirtualMemory=432MiB
UATHelper: Packaging (Windows (64-bit)):   LogSavePackage: Warning: A dependency 'PrimaryAssetLabel /Script/Engine.Default__PrimaryAssetLabel' of 'PrimaryAssetLabel /Game/Mods/TestMod/DA_TestMod.DA_TestMod' was filtered, but is mandatory. This indicates a problem with editor only stripping. We will keep the dependency anyway (1).
PackagingResults: Warning: A dependency 'PrimaryAssetLabel /Script/Engine.Default__PrimaryAssetLabel' of 'PrimaryAssetLabel /Game/Mods/TestMod/DA_TestMod.DA_TestMod' was filtered, but is mandatory. This indicates a problem with editor only stripping. We will keep the dependency anyway (1).
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Cooked packages 194 Packages Remain 0 Total 194
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Cook Diagnostics: OpenFileHandles=196, VirtualMemory=511MiB
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Finishing up...
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Saving BulkData manifest(s)...
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Done saving BulkData manifest(s)
UATHelper: Packaging (Windows (64-bit)):   LogBlueprintCodeGen: Display: Nativization Summary - AnimBP:
UATHelper: Packaging (Windows (64-bit)):   LogBlueprintCodeGen: Display: Name, Children, Non-empty Functions (Empty Functions), Variables, FunctionUsage, VariableUsage
UATHelper: Packaging (Windows (64-bit)):   LogBlueprintCodeGen: Display: Nativization Summary - Shared Variables From Graph: 0
UATHelper: Packaging (Windows (64-bit)):   LogAssetRegistryGenerator: Display: Looking for game openorder in dir C:/Users/Mythical/Documents/GitHub/RoboQuest/Build/WindowsNoEditor/FileOpenOrder/GameOpenOrder.log
UATHelper: Packaging (Windows (64-bit)):   LogAssetRegistryGenerator: Display: Saving asset registry.
UATHelper: Packaging (Windows (64-bit)):   LogAssetRegistryGenerator: Display: Generated asset registry num assets 191, size is 81.30kb
UATHelper: Packaging (Windows (64-bit)):   LogAssetRegistryGenerator: Display: Done saving asset registry.
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Cook by the book total time in tick 0.519514s total time 2.697528
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Peak Used virtual 556 MiB Peak Used physical 605 MiB
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Hierarchy Timer Information:
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:   Root: 0.000s (0)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:     CleanSandbox: 0.048s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       ProcessingAccessedStrings: 0.004s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:     CollectFilesToCook: 0.250s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       CookModificationDelegate: 0.000s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:     GenerateLongPackageName: 0.000s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:     TickCookOnTheSide: 0.520s (4)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       PostLoadPackageFixup: 0.001s (278)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       LoadPackageForCooking: 0.045s (194)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       SavingPackages: 0.472s (30)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:         BeginPackageCacheForCookedPlatformData: 0.000s (5)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:         PrecachePlatformDataForNextPackage: 0.214s (192)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:           BeginPackageCacheForCookedPlatformData: 0.214s (189)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:         SaveCookedPackage: 0.251s (194)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:           GEditorSavePackage: 0.247s (194)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:             ConvertingBlueprints: 0.002s (194)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:             VerifyCanCookPackage: 0.001s (191)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:         ClearAllCachedCookedPlatformData: 0.002s (194)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:     FinalizePackageStore: 0.001s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:     GeneratingBlueprintAssets: 0.001s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:     SavingCurrentIniSettings: 0.023s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       ProcessingAccessedStrings: 0.007s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:     SavingAssetRegistry: 0.032s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       BuildChunkManifest: 0.008s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       SaveManifests: 0.011s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       SaveRealAssetRegistry: 0.011s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display:       WriteCookerOpenOrder: 0.002s (1)
UATHelper: Packaging (Windows (64-bit)):   LogCook: Display: Done!
UATHelper: Packaging (Windows (64-bit)):   LogSavePackage: Display: Took 0.000635s to verify the EDL loading graph.
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Misc Cook Stats
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: ===============
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: NiagaraShader.Misc
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     ShadersCompiled=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: ShaderCompiler
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     BlockingTimeSec=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     AsyncCompileTimeSec=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     GlobalBeginCompileShaderTimeSec=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     GlobalBeginCompileShaderCalls=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     ProcessAsyncResultsTimeSec=0.000082
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: GlobalShader.Misc
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     ShadersCompiled=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: MeshMaterial.Misc
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     ShadersCompiled=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: MaterialShader.Misc
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     ShadersCompiled=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Package.Load
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     NumPreloadedDependencies=8
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     NumInlineLoads=4
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     NumPackagesLoaded=147
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     LoadPackageTimeSec=0.502649
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: CookOnTheFlyServer
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     PeakRequestQueueSize=28
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     PeakLoadQueueSize=161
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     PeakSaveQueueSize=153
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Package.Save
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     NumPackagesSaved=194
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     SavePackageTimeSec=0.241532
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     TagPackageExportsPresaveTimeSec=0.023739
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     TagPackageExportsTimeSec=0.006363
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     FullyLoadLoadersTimeSec=0.000100
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     ResetLoadersTimeSec=0.000699
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     TagPackageExportsGetObjectsWithOuter=0.000801
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     TagPackageExportsGetObjectsWithMarks=0.000122
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     SerializeImportsTimeSec=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     SortExportsSeekfreeInnerTimeSec=0.043655
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     SerializeExportsTimeSec=0.107508
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     SerializeBulkDataTimeSec=0.006905
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     AsyncWriteTimeSec=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     MBWritten=57.357307
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Package.DifferentPackagesSizeMBPerAsset
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Package.NumberOfDifferencesInPackagesPerAsset
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Package.PackageDifferencesSizeMBPerAsset
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Package.DiffTotal
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     NumberOfDifferentPackages=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     DifferentPackagesSizeMB=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     NumberOfDifferencesInPackages=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     PackageDifferencesSizeMB=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: UnversionedProperties
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     SavedStructs=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     SavedMB=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     EquivalentTaggedMB=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     CompressionRatio=-nan(ind)
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:     BitfieldWasteKB=0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Cook Profile
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: ============
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0.CookWallTimeSec=7.608357
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 0.StartupWallTimeSec=4.903430
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1.CookByTheBookTimeSec=2.703441
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 0.StartCookByTheBookTimeSec=2.091802
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 0. 0.GameCookModificationDelegateTimeSec=0.000039
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 1.TickCookOnTheSideTimeSec=0.609201
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 1. 0.TickCookOnTheSideLoadPackagesTimeSec=0.045304
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 1. 1.TickCookOnTheSideSaveCookedPackageTimeSec=0.251379
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 1. 1. 0.TickCookOnTheSideResolveRedirectorsTimeSec=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 1. 2.TickCookOnTheSideBeginPackageCacheForCookedPlatformDataTimeSec=0.214425
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 1. 3.TickCookOnTheSideFinishPackageCacheForCookedPlatformDataTimeSec=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 2.TickLoopGCTimeSec=0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 3.TickLoopRecompileShaderRequestsTimeSec=0.000009
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 4.TickLoopShaderProcessAsyncResultsTimeSec=0.000008
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 5.TickLoopProcessDeferredCommandsTimeSec=0.000012
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:  0. 1. 6.TickLoopTickCommandletStatsTimeSec=0.000002
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: DDC Summary Stats
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: =================
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: TotalGetHits    =       473
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: TotalGets       =       473
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: TotalGetHitPct  =  1.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: LocalGetHitPct  =  0.471459
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: SharedGetHitPct =  0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: OtherGetHitPct  =  0.528541
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: GetMissPct      =  0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: TotalPutHits    =         0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: TotalPuts       =         0
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: TotalPutHitPct  =  0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: PutMissPct      =  0.000000
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display:
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: DDC Resource Stats
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: =======================================================================================================
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Asset Type                          Total Time (Sec)  GameThread Time (Sec)  Assets Built  MB Processed
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: ----------------------------------  ----------------  ---------------------  ------------  ------------
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: MaterialShader                                  0.16                   0.16             0          4.78
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Texture (Streaming)                             0.05                   0.00             0          9.61
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: GlobalShader                                    0.01                   0.01             0          6.56
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: StaticMesh                                      0.01                   0.01             0          0.74
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: PhysX (BodySetup)                               0.00                   0.00             0          0.48
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: NavCollision                                    0.00                   0.00             0          0.02
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: Texture (Inline)                                0.00                   0.00             0         38.04
UATHelper: Packaging (Windows (64-bit)):   LogCookCommandlet: Display: DistanceField                                   0.00                   0.00             0          0.00
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display:
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display: Warning/Error Summary (Unique only)
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display: -----------------------------------
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display: LogSavePackage: Warning: A dependency 'PrimaryAssetLabel /Script/Engine.Default__PrimaryAssetLabel' of 'PrimaryAssetLabel /Game/Mods/TestMod/DA_TestMod.DA_TestMod' was filtered, but is mandatory. This indicates a problem with editor only stripping. We will keep the dependency anyway (1).
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display:
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display: Success - 0 error(s), 1 warning(s)
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display:
UATHelper: Packaging (Windows (64-bit)):   
UATHelper: Packaging (Windows (64-bit)):   Execution of commandlet took:  2.72 seconds
UATHelper: Packaging (Windows (64-bit)):   LogHttp: Display: cleaning up 0 outstanding Http requests.
UATHelper: Packaging (Windows (64-bit)):   LogContentStreaming: Display: There are 1 unreleased StreamingManagers
UATHelper: Packaging (Windows (64-bit)): Took 9.5981261s to run UE4Editor-Cmd.exe, ExitCode=0
UATHelper: Packaging (Windows (64-bit)): ********** COOK COMMAND COMPLETED **********
UATHelper: Packaging (Windows (64-bit)): ********** STAGE COMMAND STARTED **********
UATHelper: Packaging (Windows (64-bit)): Creating Staging Manifest...
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\BaseEditor.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\BaseEditorKeyBindings.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\BaseEditorPerProjectUserSettings.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\BaseEditorSettings.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\BaseLightmass.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\BasePakFileRules.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\Category.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\Editor.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\EditorTutorials.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\Engine.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\Keywords.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\PortableObjectExport.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\PortableObjectImport.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\PropertyNames.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\RepairData.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\ToolTips.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file D:\unreal_engine_installs\UE_4.26\Engine\Config\Localization\WordCount.ini
UATHelper: Packaging (Windows (64-bit)): Excluding config file C:\Users\Mythical\Documents\GitHub\RoboQuest\Config\DefaultEditor.ini
UATHelper: Packaging (Windows (64-bit)): Cleaning Stage Directory: C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor
UATHelper: Packaging (Windows (64-bit)): Creating pak using streaming install manifests.
UATHelper: Packaging (Windows (64-bit)): Reading chunk list file C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\TmpPackaging\WindowsNoEditor\pakchunklist.txt which contains 2 entries
UATHelper: Packaging (Windows (64-bit)): Reading chunk manifest C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\TmpPackaging\WindowsNoEditor\pakchunk0.txt which contains 188 entries
UATHelper: Packaging (Windows (64-bit)): Reading chunk manifest C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\TmpPackaging\WindowsNoEditor\pakchunk1.txt which contains 3 entries
UATHelper: Packaging (Windows (64-bit)): Creating Pak files utilizing 16 cores
UATHelper: Packaging (Windows (64-bit)): Executing 2 UnrealPak commands...
UATHelper: Packaging (Windows (64-bit)): Waiting for child processes to complete (2/2)
UATHelper: Packaging (Windows (64-bit)): Output from: C:\Users\Mythical\Documents\GitHub\RoboQuest\RoboQuest.uproject C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\pakchunk0-WindowsNoEditor.pak -create="C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26
\PakList_pakchunk0-WindowsNoEditor.txt" -cryptokeys=C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Metadata\Crypto.json -order=C:\Users\Mythical\Documents\GitHub\RoboQuest\Build\WindowsNoEditor\FileOpenOrder\CookerOpenOrder.log -patchpaddingalign=2048 -platform=Windows  -multiprocess -abslog="C:\Users\Mythical\AppData\Roa
ming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\UnrealPak-pakchunk0-WindowsNoEditor-2024.12.04-04.00.05.txt"
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Parsing crypto keys from a crypto key cache file
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Loading response file C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\PakList_pakchunk0-WindowsNoEditor.txt
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Added 1086 entries to add to pak file.
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Loading pak order file C:\Users\Mythical\Documents\GitHub\RoboQuest\Build\WindowsNoEditor\FileOpenOrder\CookerOpenOrder.log...
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Finished loading pak order file C:\Users\Mythical\Documents\GitHub\RoboQuest\Build\WindowsNoEditor\FileOpenOrder\CookerOpenOrder.log.
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Collecting files to add to pak file...
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Collected 1086 files in 0.01s.
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Creating pak C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\pakchunk0-WindowsNoEditor.pak.
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Pak cache opened for reading ../../../Engine/DerivedDataCache/Compressed.ddp.
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Performance to C:/Users/Mythical/AppData/Local/UnrealEngine/Common/DerivedDataCache: Latency=0.00ms. RandomReadSpeed=999.00MBs, RandomWriteSpeed=999.00MBs. Assigned SpeedClass 'Local'
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Added 1086 files, 24155835 bytes total, time 0.29s.
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: PrimaryIndex size: 13146 bytes
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: PathHashIndex size: 35227 bytes
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: FullDirectoryIndex size: 32072 bytes
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Encryption - DISABLED
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Unreal pak executed in 0.334152 seconds
UATHelper: Packaging (Windows (64-bit)): UnrealPak terminated with exit code 0
UATHelper: Packaging (Windows (64-bit)): Output from: C:\Users\Mythical\Documents\GitHub\RoboQuest\RoboQuest.uproject C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\pakchunk1-WindowsNoEditor.pak -create="C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26
\PakList_pakchunk1-WindowsNoEditor.txt" -cryptokeys=C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Metadata\Crypto.json -order=C:\Users\Mythical\Documents\GitHub\RoboQuest\Build\WindowsNoEditor\FileOpenOrder\CookerOpenOrder.log -patchpaddingalign=2048 -platform=Windows  -multiprocess -abslog="C:\Users\Mythical\AppData\Roa
ming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\UnrealPak-pakchunk1-WindowsNoEditor-2024.12.04-04.00.05.txt"
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Parsing crypto keys from a crypto key cache file
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Loading response file C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\PakList_pakchunk1-WindowsNoEditor.txt
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Added 0 entries to add to pak file.
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Loading pak order file C:\Users\Mythical\Documents\GitHub\RoboQuest\Build\WindowsNoEditor\FileOpenOrder\CookerOpenOrder.log...
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Finished loading pak order file C:\Users\Mythical\Documents\GitHub\RoboQuest\Build\WindowsNoEditor\FileOpenOrder\CookerOpenOrder.log.
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Collecting files to add to pak file...
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Collected 0 files in 0.00s.
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Creating pak C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\pakchunk1-WindowsNoEditor.pak.
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Pak cache opened for reading ../../../Engine/DerivedDataCache/Compressed.ddp.
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Performance to C:/Users/Mythical/AppData/Local/UnrealEngine/Common/DerivedDataCache: Latency=0.00ms. RandomReadSpeed=999.00MBs, RandomWriteSpeed=999.00MBs. Assigned SpeedClass 'Local'
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Added 0 files, 339 bytes total, time 0.03s.
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: PrimaryIndex size: 106 bytes
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: PathHashIndex size: 8 bytes
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: FullDirectoryIndex size: 4 bytes
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Encryption - DISABLED
UATHelper: Packaging (Windows (64-bit)):   LogPakFile: Display: Unreal pak executed in 0.038362 seconds
UATHelper: Packaging (Windows (64-bit)): UnrealPak terminated with exit code 0
UATHelper: Packaging (Windows (64-bit)): Running IoStore commandlet with arguments: -CreateGlobalContainer=C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\global.utoc -CookedDirectory=C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor -Commands="C:\Users\Mythical\AppData\Roaming\Un
real Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\IoStoreCommands.txt" -CookerOrder=C:\Users\Mythical\Documents\GitHub\RoboQuest\Build\WindowsNoEditor\FileOpenOrder\CookerOpenOrder.log -patchpaddingalign=2048   -cryptokeys=C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Metadata\Crypto.json  -TargetPlatform=
WindowsNoEditor
UATHelper: Packaging (Windows (64-bit)): Running UE4Editor IoStore for project C:\Users\Mythical\Documents\GitHub\RoboQuest\RoboQuest.uproject
UATHelper: Packaging (Windows (64-bit)): Commandlet log file is D:\unreal_engine_installs\UE_4.26\Engine\Programs\AutomationTool\Saved\IoStore-2024.12.04-04.00.06.txt
UATHelper: Packaging (Windows (64-bit)): Running: D:\unreal_engine_installs\UE_4.26\Engine\Binaries\Win64\UE4Editor-Cmd.exe C:\Users\Mythical\Documents\GitHub\RoboQuest\RoboQuest.uproject -run=IoStore -CreateGlobalContainer=C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor\RoboQuest\Content\Paks\global.utoc -CookedDirectory=C:\U
sers\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor -Commands="C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\IoStoreCommands.txt" -CookerOrder=C:\Users\Mythical\Documents\GitHub\RoboQuest\Build\WindowsNoEditor\FileOpenOrder\CookerOpenOrder.log -patchpaddingalign=2048   -cryptokeys=C:\Us
ers\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Metadata\Crypto.json  -TargetPlatform=WindowsNoEditor -abslog=D:\unreal_engine_installs\UE_4.26\Engine\Programs\AutomationTool\Saved\IoStore-2024.12.04-04.00.06.txt -stdout -CrashForUAT -unattended -NoLogTimes  -UTF8Output
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display: Running engine for game: RoboQuest
UATHelper: Packaging (Windows (64-bit)):   LogHAL: Display: Platform has ~ 16 GB [16866865152 / 17179869184 / 16], which maps to Larger [LargestMinGB=32, LargerMinGB=12, DefaultMinGB=8, SmallerMinGB=6, SmallestMinGB=0)
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'AllDesktop'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_ASTC'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_DXT'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_ETC2'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'AndroidClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_ASTCClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_DXTClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_ETC2Client'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_Multi'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Android_MultiClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'IOSClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'IOS'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Linux'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxNoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxServer'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxAArch64NoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxAArch64Client'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LinuxAArch64Server'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Lumin'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'LuminClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'MacNoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Mac'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'MacClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'MacServer'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'TVOSClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'TVOS'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'WindowsNoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'Windows'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'WindowsClient'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Loaded TargetPlatform 'WindowsServer'
UATHelper: Packaging (Windows (64-bit)):   LogTargetPlatformManager: Display: Building Assets For WindowsNoEditor
UATHelper: Packaging (Windows (64-bit)):   LogAudioDebug: Display: Lib vorbis DLL was dynamically loaded.
UATHelper: Packaging (Windows (64-bit)):   LogShaderCompilers: Display: Using Local Shader Compiler.
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Max Cache Size: 512 MB
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Loaded Boot cache: C:/Users/Mythical/AppData/Local/UnrealEngine/4.26/DerivedDataCache/Boot.ddc
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Pak cache opened for reading ../../../Engine/DerivedDataCache/Compressed.ddp.
UATHelper: Packaging (Windows (64-bit)):   LogDerivedDataCache: Display: Performance to C:/Users/Mythical/AppData/Local/UnrealEngine/Common/DerivedDataCache: Latency=0.04ms. RandomReadSpeed=1087.48MBs, RandomWriteSpeed=54.69MBs. Assigned SpeedClass 'Local'
UATHelper: Packaging (Windows (64-bit)):   LogAudioCaptureCore: Display: No Audio Capture implementations found. Audio input will be silent.
UATHelper: Packaging (Windows (64-bit)):   LogAudioCaptureCore: Display: No Audio Capture implementations found. Audio input will be silent.
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: ==================== IoStore Utils ====================
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Parsing crypto keys from a crypto key cache file 'C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Metadata\Crypto.json'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Parsed '0' crypto keys from 'C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor\RoboQuest\Metadata\Crypto.json'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Container signing - DISABLED
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Directory index - ENABLED
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Using memory mapping alignment '16384'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Using compression block size '65536'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Using compression block alignment '0'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Using command list file: 'C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_4.26\IoStoreCommands.txt'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Using target platform 'WindowsNoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Searching for cooked assets in folder 'C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Found '401' files
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Loaded Bulk Data manifest 'C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\Cooked\WindowsNoEditor/RoboQuest/Metadata/BulkDataInfo.ubulkmanifest'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Creating container targets...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Parsing packages...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Reading package assets...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Parsing package assets...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Parsing 0/191: 'C:/Users/Mythical/Documents/GitHub/RoboQuest/Saved/Cooked/WindowsNoEditor/Engine/Content/EngineResources/DefaultTextureCube.uasset'
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Creating global script objects...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Creating global imports and exports...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Converting export map import indices...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Conforming localized packages...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Adding localized import packages...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Conforming localized imports...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Adding preload dependencies...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Building bundles...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Finalizing name maps...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Finalizing package headers...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Calculating hashes
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Creating disk layout...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Ordered 0/191 packages using game open order
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Ordered 186/191 packages using cooker open order
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Ordered 5 packages using fallback bundle order
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk0: 0/207 modified entries (0.000000MB)
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk0: 207/207 added entries (52.765480MB)
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk1: 0/3 modified entries (0.000000MB)
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk1: 3/3 added entries (0.010768MB)
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Serializing container(s)...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Finalizing initial load...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Serializing global meta data
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Saving global name map to container file
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Calculating stats...
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: --------------------------------------------------- IoDispatcher --------------------------------------------------------
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Container                           Flags   TOC Size (KB)     TOC Entries       Size (MB)           Compressed (MB)
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: -------------------------------------------------------------------------------------------------------------------------
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: global                            -/-/-/-            0.49               3            1.00                         -
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk0-WindowsNoEditor         -/-/-/I           33.45             208           62.94                         -
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk1-WindowsNoEditor         -/-/-/I            0.60               4            0.25                         -
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: TOTAL                                               34.53             215           64.19                         -
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: ** Flags: (C)ompressed / (E)ncrypted / (S)igned) / (I)ndexed) **
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Compression block padding:     0.00 MB
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: -------------------------------------------- Container Directory Index --------------------------------------------------
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Container                            Size (KB)
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: global                                    0.00
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk0-WindowsNoEditor                10.33
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk1-WindowsNoEditor                 0.20
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: --------------------------------------------------- PackageStore (KB) ---------------------------------------------------
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Container                                Store Size             Packages            Localized
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: -------------------------------------------------------------------------------------------------------------------------
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk0                                         7                  188                    0
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk1                                         0                    3                    0
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: TOTAL                                             7                  191                    0
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: --------------------------------------------------- PackageHeader (KB) --------------------------------------------------
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Container                             Header       Summary         Graph     ImportMap     ExportMap       NameMap
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: -------------------------------------------------------------------------------------------------------------------------
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk0                                196            12             3             8            20           153
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: pakchunk1                                  6             0             0             0             1             4
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: TOTAL                                    201            12             3             8            21           157
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:     42.97 MB UExp
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:      0.24 MB UAsset
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:      0.04 MB FPackageFileSummary
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:       191 Packages
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:       125 Imported package entries
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:       134 Packages without imports
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:      6233 Name map entries
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:      1138 PreloadDependencies entries
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:      1058 ImportMap entries
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:       302 ExportMap entries
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Input:       227 Public exports
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display:
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Output:      193 Export bundles
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Output:      604 Export bundle entries
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Output:      125 Export bundle arcs
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Output:    15889 Public runtime script objects
UATHelper: Packaging (Windows (64-bit)):   LogIoStore: Display: Output:     0.96 MB InitialLoadData
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display:
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display: Success - 0 error(s), 0 warning(s)
UATHelper: Packaging (Windows (64-bit)):   LogInit: Display:
UATHelper: Packaging (Windows (64-bit)):   
UATHelper: Packaging (Windows (64-bit)):   Execution of commandlet took:  0.28 seconds
UATHelper: Packaging (Windows (64-bit)):   LogHttp: Display: cleaning up 0 outstanding Http requests.
UATHelper: Packaging (Windows (64-bit)):   LogContentStreaming: Display: There are 1 unreleased StreamingManagers
UATHelper: Packaging (Windows (64-bit)): Took 13.4992568s to run UE4Editor-Cmd.exe, ExitCode=0
UATHelper: Packaging (Windows (64-bit)): Copying NonUFSFiles to staging directory: C:\Users\Mythical\Documents\GitHub\RoboQuest\Saved\StagedBuilds\WindowsNoEditor
UATHelper: Packaging (Windows (64-bit)): ********** STAGE COMMAND COMPLETED **********
UATHelper: Packaging (Windows (64-bit)): ********** PACKAGE COMMAND STARTED **********
UATHelper: Packaging (Windows (64-bit)): ********** PACKAGE COMMAND COMPLETED **********
UATHelper: Packaging (Windows (64-bit)): ********** ARCHIVE COMMAND STARTED **********
UATHelper: Packaging (Windows (64-bit)): Archiving to C:/Users/Mythical/Downloads/Output
UATHelper: Packaging (Windows (64-bit)): ********** ARCHIVE COMMAND COMPLETED **********
UATHelper: Packaging (Windows (64-bit)): BUILD SUCCESSFUL
UATHelper: Packaging (Windows (64-bit)): AutomationTool exiting with ExitCode=0 (Success)



=====================================================================================


Below this is just a bunch of information, not very well organized for checking out at a later time

?-WriteBackMetadataToAssetRegistry=Disabled? maybe why iostore broken with scanning in new asset reg

iostore packing commands used when packaging the engine via the editor buttons

UATHelper: Packaging (Windows): Running UnrealPak with arguments: -CreateGlobalContainer=C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\Saved\StagedBuilds\Windows\MythForce\Content\Paks\global.utoc -CookedDirectory=C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\Saved\Cooked\Windows -PackageStoreManifest=C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\Saved\Cooked\Windows\MythForce\Metadata\packagestore.manifest -Commands="C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_5.1\IoStoreCommands.txt" -ScriptObjects=C:\Users\Mythical\
Documents\GitHub\MythForce_Mythical\Saved\Cooked\Windows\MythForce\Metadata\scriptobjects.bin -patchpaddingalign=2048 -compressionformats=Oodle -compressmethod=Kraken -compresslevel=4   -cryptokeys=C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\Saved\Cooked\Windows\MythForce\Metadata\Crypto.json -compressionMinBytesSaved=1024 -compressionMinPercentSaved=5 -WriteBackMetadataToAssetRegistry=Disabled
UATHelper: Packaging (Windows): Running: D:\unreal_engine_installs\UE_5.1\Engine\Binaries\Win64\UnrealPak.exe -CreateGlobalContainer=C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\Saved\StagedBuilds\Windows\MythForce\Content\Paks\global.utoc -CookedDirectory=C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\Saved\Cooked\Windows -PackageStoreManifest=C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\Saved\Cooked\Windows\MythForce\Metadata\packagestore.manifest -Commands="C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_5.1\IoStoreCom
mands.txt" -ScriptObjects=C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\Saved\Cooked\Windows\MythForce\Metadata\scriptobjects.bin -patchpaddingalign=2048 -compressionformats=Oodle -compressmethod=Kraken -compresslevel=4   -cryptokeys=C:\Users\Mythi




UATHelper: Packaging (Windows): Running: D:\unreal_engine_installs\UE_5.1\Engine\Binaries\Win64\UnrealPak.exe C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\MythForce.uproject  -cryptokeys=C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\Saved\Cooked\Windows\MythForce\Metadata\Crypto.json -patchpaddingalign=2048 -compressionformats=Oodle -compressmethod=Kraken -compresslevel=4  -platform=Windows  -CreateMultiple="C:\Users\Mythical\AppData\Roaming\Unreal Engine\AutomationTool\Logs\D+unreal_engine_installs+UE_5.1\PakCommands.txt"


LogTurnkeySupport: Project does not require temp target
LogLauncherProfile: Found promoted target with matching version at ../../../Engine/Binaries/Win64/UnrealGame.target
LogMonitoredProcess: Running Serialized UAT: [ cmd.exe /c ""D:/unreal_engine_installs/UE_5.1/Engine/Build/BatchFiles/RunUAT.bat"  -ScriptsForProject="C:/Users/Mythical/Documents/GitHub/MythForce_Mythical/MythForce.uproject" Turnkey -command=VerifySdk -platform=Win64 -UpdateIfNeeded -EditorIO -EditorIOPort=52301  -project="C:/Users/Mythical/Documents/GitHub/MythForce_Mythical/MythForce.uproject" BuildCookRun -nop4 -utf8output -nocompileeditor -skipbuildeditor -cook  -project="C:/Users/Mythical/Documents/GitHub/MythForce_Mythical/MythForce.uproject"  -unrealexe="D:\unreal_engine_installs\UE_5.1\
Engine\Binaries\Win64\UnrealEditor-Cmd.exe" -platform=Win64 -installed -stage -archive -package -pak -iostore -compressed -prereqs -archivedirectory="C:/Users/Mythical/Downloads/Output" -manifests" -nocompile -nocompileuat ]
UATHelper: Packaging (Windows): Running AutomationTool...


UATHelper: Packaging (Windows): Commandlet log file is D:\unreal_engine_installs\UE_5.1\Engine\Programs\AutomationTool\Saved\Cook-2024.12.03-20.56.48.txt
UATHelper: Packaging (Windows): Running: D:\unreal_engine_installs\UE_5.1\Engine\Binaries\Win64\UnrealEditor-Cmd.exe C:\Users\Mythical\Documents\GitHub\MythForce_Mythical\MythForce.uproject -run=Cook  -TargetPlatform=Windows  -unversioned -fileopenlog -manifests -abslog=D:\unreal_engine_installs\UE_5.1\Engine\Programs\AutomationTool\Saved\Cook-2024.12.03-20.56.48.txt -stdout -CrashForUAT -unattended -NoLogTimes  -UTF8Output



























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


