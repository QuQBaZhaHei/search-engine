# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Spyder Project Contributors

# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)
# -----------------------------------------------------------------------------
"""
Text encoding utilities, text file I/O.

Functions 'get_coding', 'decode', 'encode' and 'to_unicode' come from Eric4
source code (Utilities/__init___.py) Copyright © 2003-2009 Detlev Offenbach
"""

# yapf: disable


# Standard library imports
import locale
import sys

# Local imports
from navigator_updater.utils.py3compat import (is_binary_string, is_string,
                                               is_unicode, to_text_string)

# yapf: enable

PREFERRED_ENCODING = locale.getpreferredencoding()


def transcode(text, input=PREFERRED_ENCODING, output=PREFERRED_ENCODING):
    """Transcode a text string"""
    try:
        return text.decode("cp437").encode("cp1252")
    except UnicodeError:
        try:
            return text.decode("cp437").encode(output)
        except UnicodeError:
            return text


# -----------------------------------------------------------------------------
#  Functions for encoding and decoding bytes that come from
#  the *file system*.
# -----------------------------------------------------------------------------


# The default encoding for file paths and environment variables should be set
# to match the default encoding that the OS is using.
def getfilesystemencoding():
    """
    Query the filesystem for the encoding used to encode filenames and envvars.
    """
    encoding = sys.getfilesystemencoding()
    if encoding is None:
        # Must be Linux or Unix and nl_langinfo(CODESET) failed.
        encoding = PREFERRED_ENCODING
    return encoding


FS_ENCODING = getfilesystemencoding()


def to_unicode_from_fs(string):
    """
    Return a unicode version of string decoded using the file system encoding.
    """
    if not is_string(string):  # string is a QString
        string = to_text_string(string.toUtf8(), 'utf-8')
    else:
        if is_binary_string(string):
            try:
                unic = string.decode(FS_ENCODING)
            except (UnicodeError, TypeError):
                pass
            else:
                return unic
    return string


def to_fs_from_unicode(unic):
    """
    Return a byte string version of unc encoded using the file system encoding.
    """
    if is_unicode(unic):
        try:
            string = unic.encode(FS_ENCODING)
        except (UnicodeError, TypeError):
            pass
        else:
            return string
    return unic
