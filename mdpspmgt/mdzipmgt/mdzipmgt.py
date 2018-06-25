#!/usr/bin/env python
# -*- coding:Utf-8 -*-

"""
Management of zip packages.

Main module for managing Zip packages:
    - Identification
    - Opening
    - Reading

"""

__author__ = "Moussa DIENG"
__copyright__ = "Copyright 2018, Ingenico FR"
__credits__ = ["Moussa DIENG (Ingenico Partner)"]
__license__ = "Ingenico Internal Licence"
__version__ = "1.0.2"
__maintainer__ = "Moussa DIENG"
__email__ = "moussa.dieng@ingenico.com"
__status__ = "Development"

import zipfile as zf


"""
Tells whether or not a filename is a Zip file.
@:param filename: the file to test (name, path)
@:return boolean value (True|False)
"""
def is_zipfile(filename):
    return zf.is_zipfile(filename)


"""
Opens a Zip file in read only mode
@:param filename: the file to open (name, path)
@:return file buffer if exist or None
"""
def open_zipfile(filename):
    if is_zipfile(filename):
        return zf.ZipFile(filename, 'r')
    return None


"""
Reads a Zip file and returns a list of files in it or an empty list
@:param filename: the file to read (name, path)
@:return a list of filenames in the Zip file or an empty list 
"""
def read_zipfile(filename):
    the_file = open_zipfile(filename)

    if the_file is not None:
        return the_file.namelist()
    return []


"""
Read the content of a file in the Zip
@:param zip_name: the zip path
@:param file_name: the file to read into the zip
@:return file_name content
"""
def read_file_content(zip_name, file_name):
    the_zip = open_zipfile(zip_name)
    if the_zip is not None:
        return the_zip.open(file_name)
    return None


"""
Internal module test function 
"""
def test():
    print is_zipfile('CAL_20171012.zip')
    file_list = read_zipfile('CAL_20171012.zip')
    for f in file_list:
        print(f)
