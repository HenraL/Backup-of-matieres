import os, shutil
from tkinter import *
computer_drive=os.getenv("TMP")
computer_letter=computer_drive[0]
dest_drive=input("Enter the letter of the destination drive: ({computer_drive},D,E,F, ...")
restore_or_copy=input("r to restor {computer_drive} to copy:")
source_drive_letter=input("Enter the letter of the drive containing the files:")
User_name=os.getenv("username")
path_list_w_t_get=[
    "{computer_drive}:\ProgramData\Wondershare Filmora",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\Analystic",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\Captions",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\Default Effects",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\Filmora9StartTips",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\Installed Effects",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\LocalHtml",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\PerformanceData",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\Preset",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\Skin",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\StartTips",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\Trial Effects",
    "?{computer_drive}:\ProgramData\Wondershare Filmora\WondershareAnalystic",
    "?files in {computer_drive}:\ProgramData\Wondershare Filmora",
    "{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora",
    "{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Backup",
    "{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Fonts",
    "{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Installed Effects",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Output",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Projects",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Proxy",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Recorded",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Render",
    "{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Snapshot",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Temp",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Upload",
    "{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media\Device Import",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media\Downloaded Media",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media\Favourite",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media\VOBRepair",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Voiceover",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\WsveProjectBackup",
    "? files in {computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora",
    "{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Backup",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Fonts",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Installed Effects",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Output",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Projects",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Proxy",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Recorded",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Render",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Snapshot",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Temp",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Upload",
    "{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media\Device Import",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media\Downloaded Media",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media\Favourite",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media\VOBRepair",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Voiceover",
    "?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\WsveProjectBackup",
    "?files in {computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9"
    ]


#interesting paths:
#{computer_drive}:\ProgramData\Wondershare Filmora
#?{computer_drive}:\ProgramData\Wondershare Filmora\Analystic
#?{computer_drive}:\ProgramData\Wondershare Filmora\Captions
#?{computer_drive}:\ProgramData\Wondershare Filmora\Default Effects
#?{computer_drive}:\ProgramData\Wondershare Filmora\Filmora9StartTips
#?{computer_drive}:\ProgramData\Wondershare Filmora\Installed Effects
#?{computer_drive}:\ProgramData\Wondershare Filmora\LocalHtml
#?{computer_drive}:\ProgramData\Wondershare Filmora\PerformanceData
#?{computer_drive}:\ProgramData\Wondershare Filmora\Preset
#?{computer_drive}:\ProgramData\Wondershare Filmora\Skin
#?{computer_drive}:\ProgramData\Wondershare Filmora\StartTips
#?{computer_drive}:\ProgramData\Wondershare Filmora\Trial Effects
#?{computer_drive}:\ProgramData\Wondershare Filmora\WondershareAnalystic
#?files in {computer_drive}:\ProgramData\Wondershare Filmora
#{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora
#{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Backup
#{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Fonts
#{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Installed Effects
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Output
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Projects
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Proxy
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Recorded
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Render
#{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Snapshot
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Temp
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Upload
#{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media\Device Import
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media\Downloaded Media
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media\Favourite
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\User Media\VOBRepair
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\Voiceover
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora\WsveProjectBackup
#? files in {computer_drive}:\Users\{User_name}\Documents\Wondershare\Wondershare Filmora

#{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Backup
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Fonts
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Installed Effects
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Output
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Projects
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Proxy
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Recorded
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Render
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Snapshot
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Temp
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Upload
#{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media\Device Import
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media\Downloaded Media
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media\Favourite
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\User Media\VOBRepair
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\Voiceover
#?{computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9\WsveProjectBackup
#?files in {computer_drive}:\Users\{User_name}\Documents\Wondershare Filmora 9
