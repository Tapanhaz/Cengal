#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__all__ = ['S_OK', 'WH_CALLWNDPROC', 'WH_CALLWNDPROCRET', 'WCA_ACCENT_POLICY', 'WS_BORDER', 'WS_DLGFRAME', 'WS_OVERLAPPED', 'WS_THICKFRAME', 'WS_CAPTION', 'WS_SYSMENU', 'WS_MINIMIZEBOX', 'WS_MAXIMIZEBOX', 'WS_POPUP', 'WS_OVERLAPPEDWINDOW', 'SM_CXPADDEDBORDER', 'KnownfolderidConstants']


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"

from ctypes import c_int
from cengal.ctypes_tools.types import GUID
from uuid import UUID

S_OK = 0

WH_CALLWNDPROC = c_int(4)
WH_CALLWNDPROCRET = c_int(12)


WCA_ACCENT_POLICY = 19

WS_BORDER = 0x00800000
WS_DLGFRAME = 0x00400000
WS_OVERLAPPED = 0x00000000
WS_THICKFRAME = 0x00040000
WS_CAPTION = 0x00C00000  # WS_BORDER | WS_DLGFRAME
WS_SYSMENU = 0x00080000
WS_MINIMIZEBOX = 0x00020000
WS_MAXIMIZEBOX = 0x00010000
WS_POPUP = 0x80000000
WS_OVERLAPPEDWINDOW = WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX


SM_CXPADDEDBORDER = 92

# SW_MAXIMIZE: int = 3


# MONITOR_DEFAULTTONULL = 0x00000000


# WM_NCCREATE = 0x0081
# WM_NCCALCSIZE = 0x0083
# WM_NCHITTEST = 0x0084
# WM_NCACTIVATE = 0x0086
# WM_CLOSE = 0x0010
# WM_DESTROY = 0x0002
# WM_KEYDOWN = 0x0100
# WM_SYSKEYDOWN = 0x0104


# GWL_WNDPROC = -4

# CS_HREDRAW = 0x0002
# CS_VREDRAW = 0x0001


# CW_USEDEFAULT = 0x80000000


# VK_F8 = 0x77
# VK_F9 = 0x78
# VK_F10 = 0x79
# VK_F11 = 0x7A


class KnownfolderidConstants:
    FOLDERID_AccountPictures = GUID.from_uuid(UUID('{008ca0b1-55b4-4c56-b8a8-4de4b299d3be}'))
    FOLDERID_AddNewPrograms = GUID.from_uuid(UUID('{de61d971-5ebc-4f02-a3a9-6c82895e5c04}'))
    FOLDERID_AdminTools = GUID.from_uuid(UUID('{724EF170-A42D-4FEF-9F26-B60E846FBA4F}'))
    FOLDERID_ApplicationShortcuts = GUID.from_uuid(UUID('{A3918781-E5F2-4890-B3D9-A7E54332328C}'))
    FOLDERID_CDBurning = GUID.from_uuid(UUID('{9E52AB10-F80D-49DF-ACB8-4330F5687855}'))
    FOLDERID_CommonAdminTools = GUID.from_uuid(UUID('{D0384E7D-BAC3-4797-8F14-CBA229B392B5}'))
    FOLDERID_CommonAppData = GUID.from_uuid(UUID('{62AB5D82-FDC1-4DC3-A9DD-070D1D495D97}'))
    FOLDERID_CommonDesktopDirectory = GUID.from_uuid(UUID('{C4AA340D-F20F-4863-AFEF-F87EF2E6BA25}'))
    FOLDERID_CommonDocuments = GUID.from_uuid(UUID('{ED4824AF-DCE4-45A8-81E2-FC7965083634}'))
    FOLDERID_CommonDownloads = GUID.from_uuid(UUID('{f7ce2e13-8c90-4e1f-ba7e-1925aebd977c}'))
    FOLDERID_CommonMusic = GUID.from_uuid(UUID('{4BD8D571-6D19-48D3-BE97-422220080E43}'))
    FOLDERID_CommonOemLinks = GUID.from_uuid(UUID('{C1BAE2D0-10DF-4334-BEDD-7AA20B227A9D}'))
    FOLDERID_CommonPictures = GUID.from_uuid(UUID('{B6EBFB86-6907-413C-9AF7-4FC2ABF07CC5}'))
    FOLDERID_CommonPrograms = GUID.from_uuid(UUID('{0139D44E-6AFE-49F2-8690-3DAFCAE6FFB8}'))
    FOLDERID_CommonStartMenu = GUID.from_uuid(UUID('{A4115719-D62E-491D-AA7C-E74B8BE3B067}'))
    FOLDERID_CommonStartup = GUID.from_uuid(UUID('{82A5EA35-D9CD-47C5-9629-E15D2F714E6E}'))
    FOLDERID_CommonTemplates = GUID.from_uuid(UUID('{B94237E7-57AC-4347-9151-B08C6C32D1F7}'))
    FOLDERID_CommonVideos = GUID.from_uuid(UUID('{18989B1D-99B5-455B-841C-AB7C74E4DDFC}'))
    FOLDERID_ComputerFolder = GUID.from_uuid(UUID('{0AC0837C-BBF8-452A-850D-79D08E667CA7}'))
    FOLDERID_ConflictFolder = GUID.from_uuid(UUID('{4bfefb45-347d-4006-a5be-ac0cb0567192}'))
    FOLDERID_ConnectionsFolder = GUID.from_uuid(UUID('{6F0CD92B-2E97-45D1-88FF-B0D186B8DEDD}'))
    FOLDERID_Contacts = GUID.from_uuid(UUID('{56784854-C6CB-462b-8169-88E350ACB882}'))
    FOLDERID_ControlPanelFolder = GUID.from_uuid(UUID('{82A74AEB-AEB4-465C-A014-D097EE346D63}'))
    FOLDERID_Cookies = GUID.from_uuid(UUID('{2B0F765D-C0E9-4171-908E-08A611B84FF6}'))
    FOLDERID_Desktop = GUID.from_uuid(UUID('{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}'))
    FOLDERID_DeviceMetadataStore = GUID.from_uuid(UUID('{5CE4A5E9-E4EB-479D-B89F-130C02886155}'))
    FOLDERID_Documents = GUID.from_uuid(UUID('{FDD39AD0-238F-46AF-ADB4-6C85480369C7}'))
    FOLDERID_DocumentsLibrary = GUID.from_uuid(UUID('{7B0DB17D-9CD2-4A93-9733-46CC89022E7C}'))
    FOLDERID_Downloads = GUID.from_uuid(UUID('{374DE290-123F-4565-9164-39C4925E467B}'))
    FOLDERID_Favorites = GUID.from_uuid(UUID('{1777F761-68AD-4D8A-87BD-30B759FA33DD}'))
    FOLDERID_Fonts = GUID.from_uuid(UUID('{FD228CB7-AE11-4AE3-864C-16F3910AB8FE}'))
    FOLDERID_GameTasks = GUID.from_uuid(UUID('{054FAE61-4DD8-4787-80B6-090220C4B700}'))
    FOLDERID_History = GUID.from_uuid(UUID('{D9DC8A3B-B784-432E-A781-5A1130A75963}'))
    FOLDERID_HomeGroup = GUID.from_uuid(UUID('{52528A6B-B9E3-4ADD-B60D-588C2DBA842D}'))
    FOLDERID_HomeGroupCurrentUser = GUID.from_uuid(UUID('{9B74B6A3-0DFD-4f11-9E78-5F7800F2E772}'))
    FOLDERID_ImplicitAppShortcuts = GUID.from_uuid(UUID('{BCB5256F-79F6-4CEE-B725-DC34E402FD46}'))
    FOLDERID_InternetCache = GUID.from_uuid(UUID('{352481E8-33BE-4251-BA85-6007CAEDCF9D}'))
    FOLDERID_InternetFolder = GUID.from_uuid(UUID('{4D9F7874-4E0C-4904-967B-40B0D20C3E4B}'))
    FOLDERID_Libraries = GUID.from_uuid(UUID('{1B3EA5DC-B587-4786-B4EF-BD1DC332AEAE}'))
    FOLDERID_Links = GUID.from_uuid(UUID('{bfb9d5e0-c6a9-404c-b2b2-ae6db6af4968}'))
    FOLDERID_LocalAppData = GUID.from_uuid(UUID('{F1B32785-6FBA-4FCF-9D55-7B8E7F157091}'))
    FOLDERID_LocalAppDataLow = GUID.from_uuid(UUID('{A520A1A4-1780-4FF6-BD18-167343C5AF16}'))
    FOLDERID_LocalizedResourcesDir = GUID.from_uuid(UUID('{2A00375E-224C-49DE-B8D1-440DF7EF3DDC}'))
    FOLDERID_Music = GUID.from_uuid(UUID('{4BD8D571-6D19-48D3-BE97-422220080E43}'))
    FOLDERID_MusicLibrary = GUID.from_uuid(UUID('{2112AB0A-C86A-4FFE-A368-0DE96E47012E}'))
    FOLDERID_NetHood = GUID.from_uuid(UUID('{C5ABBF53-E17F-4121-8900-86626FC2C973}'))
    FOLDERID_NetworkFolder = GUID.from_uuid(UUID('{D20BEEC4-5CA8-4905-AE3B-BF251EA09B53}'))
    FOLDERID_OriginalImages = GUID.from_uuid(UUID('{2C36C0AA-5812-4b87-BFD0-4CD0DFB19B39}'))
    FOLDERID_PhotoAlbums = GUID.from_uuid(UUID('{69D2CF90-FC33-4FB7-9A0C-EBB0F0FCB43C}'))
    FOLDERID_Pictures = GUID.from_uuid(UUID('{33E28130-4E1E-4676-835A-98395C3BC3BB}'))
    FOLDERID_PicturesLibrary = GUID.from_uuid(UUID('{A990AE9F-A03B-4E80-94BC-9912D7504104}'))
    FOLDERID_Playlists = GUID.from_uuid(UUID('{DE92C1C7-837F-4F69-A3BB-86E631204A23}'))
    FOLDERID_PrintHood = GUID.from_uuid(UUID('{9274BD8D-CFD1-41C3-B35E-B13F55A758F4}'))
    FOLDERID_PrintersFolder = GUID.from_uuid(UUID('{76FC4E2D-D6AD-4519-A663-37BD56068185}'))
    FOLDERID_Profile = GUID.from_uuid(UUID('{5E6C858F-0E22-4760-9AFE-EA3317B67173}'))
    FOLDERID_ProgramData = GUID.from_uuid(UUID('{62AB5D82-FDC1-4DC3-A9DD-070D1D495D97}'))
    FOLDERID_ProgramFiles = GUID.from_uuid(UUID('{905e63b6-c1bf-494e-b29c-65b732d3d21a}'))
    FOLDERID_ProgramFilesX64 = GUID.from_uuid(UUID('{6D809377-6AF0-444b-8957-A3773F02200E}'))
    FOLDERID_ProgramFilesX86 = GUID.from_uuid(UUID('{7C5A40EF-A0FB-4BFC-874A-C0F2E0B9FA8E}'))
    FOLDERID_ProgramFilesCommon = GUID.from_uuid(UUID('{F7F1ED05-9F6D-47A2-AAAE-29D317C6F066}'))
    FOLDERID_ProgramFilesCommonX64 = GUID.from_uuid(UUID('{6365D5A7-0F0D-45E5-87F6-0DA56B6A4F7D}'))
    FOLDERID_ProgramFilesCommonX86 = GUID.from_uuid(UUID('{DE974D24-D9C6-4D3E-BF91-F4455120B917}'))
    FOLDERID_Programs = GUID.from_uuid(UUID('{A77F5D77-2E2B-44C3-A6A2-ABA601054A51}'))
    FOLDERID_Public = GUID.from_uuid(UUID('{DFDF76A2-C82A-4D63-906A-5644AC457385}'))
    FOLDERID_PublicDesktop = GUID.from_uuid(UUID('{C4AA340D-F20F-4863-AFEF-F87EF2E6BA25}'))
    FOLDERID_PublicDocuments = GUID.from_uuid(UUID('{ED4824AF-DCE4-45A8-81E2-FC7965083634}'))
    FOLDERID_PublicDownloads = GUID.from_uuid(UUID('{3D644C9B-1FB8-4f30-9B45-F670235F79C0}'))
    FOLDERID_PublicGameTasks = GUID.from_uuid(UUID('{DEBF2536-E1A8-4c59-B6A2-414586476AEA}'))
    FOLDERID_PublicLibraries = GUID.from_uuid(UUID('{48DAF80B-E6CF-4F4E-B800-0E69D84EE384}'))
    FOLDERID_PublicMusic = GUID.from_uuid(UUID('{3214FAB5-9757-4298-BB61-92A9DEAA44FF}'))
    FOLDERID_PublicPictures = GUID.from_uuid(UUID('{B6EBFB86-6907-413C-9AF7-4FC2ABF07CC5}'))
    FOLDERID_PublicRingtones = GUID.from_uuid(UUID('{E555AB60-153B-4D17-9F04-A5FE99FC15EC}'))
    FOLDERID_PublicUserTiles = GUID.from_uuid(UUID('{0482af6c-08f1-4c34-8c90-e17ec98b1e17}'))
    FOLDERID_PublicVideos = GUID.from_uuid(UUID('{2400183A-6185-49FB-A2D8-4A392A602BA3}'))
    FOLDERID_QuickLaunch = GUID.from_uuid(UUID('{52a4f021-7b75-48a9-9f6b-4b87a210bc8f}'))
    FOLDERID_Recent = GUID.from_uuid(UUID('{AE50C081-EBD2-438A-8655-8A092E34987A}'))
    FOLDERID_RecordedTVLibrary = GUID.from_uuid(UUID('{1A6FDBA2-F42D-4358-A798-B74D745926C5}'))
    FOLDERID_RecycleBinFolder = GUID.from_uuid(UUID('{B7534046-3ECB-4C18-BE4E-64CD4CB7D6AC}'))
    FOLDERID_ResourceDir = GUID.from_uuid(UUID('{8AD10C31-2ADB-4296-A8F7-E4701232C972}'))
    FOLDERID_Ringtones = GUID.from_uuid(UUID('{C870044B-F49E-4126-A9C3-B52A1FF411E8}'))
    FOLDERID_RoamingAppData = GUID.from_uuid(UUID('{3EB685DB-65F9-4CF6-A03A-E3EF65729F3D}'))
    FOLDERID_RoamedTileImages = GUID.from_uuid(UUID('{AAA8D5A5-F1D6-4259-BAA8-78E7EF60835E}'))
    FOLDERID_RoamingTiles = GUID.from_uuid(UUID('{00BCFC5A-ED94-4e48-96A1-3F6217F21990}'))
    FOLDERID_SampleMusic = GUID.from_uuid(UUID('{B250C668-F57D-4EE1-A63C-290EE7D1AA1F}'))
    FOLDERID_SamplePictures = GUID.from_uuid(UUID('{C4900540-2379-4C75-844B-64E6FAF8716B}'))
    FOLDERID_SamplePlaylists = GUID.from_uuid(UUID('{15CA69B3-30EE-49C1-ACE1-6B5EC372AFB5}'))
    FOLDERID_SampleVideos = GUID.from_uuid(UUID('{859EAD94-2E85-48AD-A71A-0969CB56A6CD}'))
    FOLDERID_SavedGames = GUID.from_uuid(UUID('{4C5C32FF-BB9D-43b0-B5B4-2D72E54EAAA4}'))
    FOLDERID_SavedPictures = GUID.from_uuid(UUID('{3B193882-D3AD-4eab-965A-69829D1FB59F}'))
    FOLDERID_SavedPicturesLibrary = GUID.from_uuid(UUID('{E25B5812-BE88-4bd9-94B0-29233477B6C3}'))
    FOLDERID_SavedSearches = GUID.from_uuid(UUID('{7d1d3a04-debb-4115-95cf-2f29da2920da}'))
    FOLDERID_Screenshots = GUID.from_uuid(UUID('{b7bede81-df94-4682-a7d8-57a52620b86f}'))
    FOLDERID_SearchHistory = GUID.from_uuid(UUID('{0D4C3DB6-03A3-462F-A0E6-08924C41B5D4}'))
    FOLDERID_SearchTemplates = GUID.from_uuid(UUID('{7E636BFE-DFA9-4D5E-B456-D7B39851D8A9}'))
    FOLDERID_SendTo = GUID.from_uuid(UUID('{8983036C-27C0-404B-8F08-102D10DCFD74}'))
    FOLDERID_SidebarDefaultParts = GUID.from_uuid(UUID('{7B396E54-9EC5-4300-BE0A-2482EBAE1A26}'))
    FOLDERID_SidebarParts = GUID.from_uuid(UUID('{A75D362E-50FC-4fb7-AC2C-A8BEAA314493}'))
    FOLDERID_SkyDrive = GUID.from_uuid(UUID('{A52BBA46-E9E1-435f-B3D9-28DAA648C0F6}'))
    FOLDERID_SkyDriveCameraRoll = GUID.from_uuid(UUID('{767E6811-49CB-4273-87C2-20F355E1085B}'))
    FOLDERID_SkyDriveDocuments = GUID.from_uuid(UUID('{24D89E24-2F19-4534-9DDE-6A6671FBB8FE}'))
    FOLDERID_SkyDriveMusic = GUID.from_uuid(UUID('{C3F2459E-80D6-45DC-BFEF-1F769F2BE730}'))
    FOLDERID_SkyDrivePictures = GUID.from_uuid(UUID('{339719B5-8C47-4894-94C2-D8F77ADD44A6}'))
    FOLDERID_StartMenu = GUID.from_uuid(UUID('{625B53C3-AB48-4EC1-BA1F-A1EF4146FC19}'))
    FOLDERID_Startup = GUID.from_uuid(UUID('{B97D20BB-F46A-4C97-BA10-5E3608430854}'))
    FOLDERID_SyncManagerFolder = GUID.from_uuid(UUID('{43668BF8-C14E-49B2-97C9-747784D784B7}'))
    FOLDERID_SyncResultsFolder = GUID.from_uuid(UUID('{289a9a43-be44-4057-a41b-587a76d7e7f9}'))
    FOLDERID_SyncSetupFolder = GUID.from_uuid(UUID('{0F214138-B1D3-4a90-BBA9-27CBC0C5389A}'))
    FOLDERID_System = GUID.from_uuid(UUID('{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}'))
    FOLDERID_SystemX86 = GUID.from_uuid(UUID('{D65231B0-B2F1-4857-A4CE-A8E7C6EA7D27}'))
    FOLDERID_Templates = GUID.from_uuid(UUID('{A63293E8-664E-48DB-A079-DF759E0509F7}'))
    FOLDERID_UserPinned = GUID.from_uuid(UUID('{9E3995AB-1F9C-4F13-B827-48B24B6C7174}'))
    FOLDERID_UserProfiles = GUID.from_uuid(UUID('{0762D272-C50A-4BB0-A382-697DCD729B80}'))
    FOLDERID_UserProgramFiles = GUID.from_uuid(UUID('{5CD7AEE2-2219-4A67-B85D-6C9CE15660CB}'))
    FOLDERID_UserProgramFilesCommon = GUID.from_uuid(UUID('{BCBD3057-CA5C-4622-B42D-BC56DB0AE516}'))
    FOLDERID_UsersFiles = GUID.from_uuid(UUID('{f3ce0f7c-4901-4acc-8648-d5d44b04ef8f}'))
    FOLDERID_UsersLibraries = GUID.from_uuid(UUID('{A302545D-DEFF-464b-ABE8-61C8648D939B}'))
    FOLDERID_Videos = GUID.from_uuid(UUID('{18989B1D-99B5-455B-841C-AB7C74E4DDFC}'))
    FOLDERID_VideosLibrary = GUID.from_uuid(UUID('{491E922F-5643-4AF4-A7EB-4E7A138D8174}'))
    FOLDERID_Windows = GUID.from_uuid(UUID('{F38BF404-1D43-42F2-9305-67DE0B28FC23}'))
