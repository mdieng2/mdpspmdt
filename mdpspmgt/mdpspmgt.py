"""
Management of frames widgets and application behaviour calling.

Main module for managing:
    - Graphic components (Frames, widgets, menus...)
    - Application mainloop (idle)
    - Main function
    - Component's type (System, Manager, Application, Certificats SSL)

"""

__author__ = "Moussa DIENG"
__copyright__ = "Copyright 2018, Ingenico FR"
__credits__ = ["Moussa DIENG"]
__license__ = "Ingenico Internal Licence"
__version__ = "1.0.2"
__maintainer__ = "Moussa DIENG"
__email__ = "moussa.dieng@ingenico.com"
__status__ = "Development"

import Tkinter as Tk
import mdpspgui.mdpspgui as appUI
#import mdpspgui.testMyNotebook as appUI
import mdzipmgt.mdzipmgt as Zip
import mdpspcomponent.mdpspcomponent as Cpnent


def main(self=None):
    appUI.runAppUI(self=None)

    """
    file_list = Zip.read_zipfile('CAL_20171012.zip')
    #for f in file_list:
    #    print(f)
    print "======================================================================================="
    print "|{:.^6}|{:.^6}|{:.^50}|{:.^20}|".format('Name', 'Number', 'File Name', 'Full Name')
    print "======================================================================================="
    for f in file_list:
        cpnent = Cpnent.app_component_present(f)
        print "|{:.<6}|{:.<6}|{:.<50}|{:.<20}|".format(cpnent[1], cpnent[0], f, cpnent[2])
    """

if __name__ == "__main__":
    main(self=None)