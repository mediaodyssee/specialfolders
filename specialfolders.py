#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A cross-platform library to retrieve the current user's special folders (like
Images, Documents, Videos etc.).
"""

import sys
import locale

VERSION = '0.1.0'
__encoding__ = locale.getdefaultlocale()[1]

if sys.platform.startswith("win"):
    from win32com.shell import shell, shellcon
    __mapping__ = {
        'DESKTOP': 'CSIDL_DESKTOP',
        'DOCUMENTS': 'CSIDL_PERSONAL',
        'PICTURES': 'CSIDL_MYPICTURES',
        'MUSIC': 'CSIDL_MYMUSIC',
        'VIDEOS': 'CSIDL_MYVIDEO',  # None on XP
        # TODO: "downloads" folder on windows ?
    }

    def _get_folder(typ):
        """
        Windows implementation.
        """
        try:
            typ = __mapping__[typ]
            return shell.SHGetFolderPath(0, getattr(shellcon, typ), None, 0)
        except:
            return None
elif sys.platform.startswith("darwin"):
    import AppKit
    __mapping__ = {
        'DESKTOP': 'NSDesktopDirectory',
        'DOCUMENTS': 'NSDocumentDirectory',
        'PICTURES': 'NSPicturesDirectory',
        'MUSIC': 'NSMusicDirectory',
        'VIDEOS': 'NSMoviesDirectory',
        'DOWNLOAD': 'NSDownloadsDirectory',
    }

    def _get_folder(typ):
        """
        MacOSX implementation.
        """
        try:
            typ = __mapping__[typ]
            return unicode(
                AppKit.NSSearchPathForDirectoriesInDomains(
                    getattr(AppKit, typ),
                    AppKit.NSUserDomainMask,
                    True
                )[0],
                __encoding__
            )
        except:
            return None
else:
    import subprocess

    def _get_folder(typ):
        """
        Unices implementation.
        """
        try:
            proc = subprocess.Popen(
                ['xdg-user-dir', typ],
                stdout=subprocess.PIPE
            )
            return unicode(proc.communicate()[0].strip(), __encoding__)
        except:
            return None


def get_desktop_folder():
    """
    Returns the "Desktop" folder path.
    """
    return _get_folder('DESKTOP')


def get_documents_folder():
    """
    Returns the "Documents" folder path.
    """
    return _get_folder('DOCUMENTS')


def get_pictures_folder():
    """
    Returns the "Pictures" folder path.
    """
    return _get_folder('PICTURES')


def get_music_folder():
    """
    Returns the "Music" folder path.
    """
    return _get_folder('MUSIC')


def get_videos_folder():
    """
    Returns the "Music" folder path.
    """
    return _get_folder('VIDEOS')


def get_downloads_folder():
    """
    Returns the "Downloads" folder path.
    """
    return _get_folder('DOWNLOAD')


def get_all_special_folders():
    """
    Returns all special folders in a dictionary.
    """
    return {
        'desktop': get_desktop_folder(),
        'documents': get_documents_folder(),
        'pictures': get_pictures_folder(),
        'music': get_music_folder(),
        'videos': get_videos_folder(),
        'downloads': get_downloads_folder(),
    }


if __name__ == '__main__':
    print 'Special folders on platform', sys.platform
    print 'Desktop folder', get_desktop_folder()
    print 'Documents folder', get_documents_folder()
    print 'Pictures folder', get_pictures_folder()
    print 'Music folder', get_music_folder()
    print 'Videos folder', get_videos_folder()
    print 'Downloads folder', get_downloads_folder()
    print 'All folders', get_all_special_folders()
