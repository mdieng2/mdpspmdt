#!/usr/bin/env python
# -*- coding:Utf-8 -*-

"""

"""

__author__ = "Moussa DIENG"
__copyright__ = "Copyright 2018, Ingenico FR"
__credits__ = ["Moussa DIENG (Ingenico Partner)"]
__license__ = "2IL - Ingenico Internal Licence"
__name__ = "Depackager"
__version__ = "01.00.02"
__maintainer__ = "Moussa DIENG"
__email__ = "moussa.dieng@ingenico.com"
__status__ = "Development"

import ttk as Ttk
import Tkinter as Tk
import Tkconstants, tkFileDialog
import mdzipmgt.mdzipmgt as Zip
import mdpspcomponent.mdpspcomponent as cpnmgt
import os, sys
import mdpsplogger.mdpsplogger as logPack
import ntpath
import xlsxwriter
from difflib import ndiff
import re

dict_tag_to_fgcolor = {
    'used': '#98FB99',  # 'pale green'
    'unused': '#FFFFFF',  # 'white'
    'unknown': '#BFEFFF',  # 'pale green'
    '+': '#98FB99',  # 'pale green'
    '-': '#F08080',  # 'light coral'
    ' ': '#FFFFFF',  # white
    # 'unused' : '#F08080', # 'light coral'
}


class AppUI(Ttk.Notebook):
    default_package = {
        'general': {
            'pack_name': '',
            'catalog_name': '',
            'catalog_list': [],
            'file_number': 0,
            'system_version': 'XX.XX',
            'manager_version': 'YY.YY',
            'sdk_version': 'XX.YY.ZZ',
            'terminal_addressed': '',
            'ads_par': 0,
            'manager_par': 0,
            'c3config_t': 0,
            'security_components': []
        },
        'application': [],
        'system': [],
        'manager': [],
        'parameter': [],
        'ads_param': [],
        'unknown': []
    }

    def __init__(self, master=None, **kw):
        Ttk.Notebook.__init__(self, master, **kw)
        self.logger = logPack.init_logger()
        logPack.log_info(self.logger, "####  INTO __init__  ###")
        self.master = master
        self.loaded_package = self.default_package
        master.title("%s : : : %s" % (__name__, __version__))
        master.resizable(False, False)
        # master.wm_iconbitmap('mdpspicon/depackager.ico')

        # Create menu
        menubar = Tk.Menu(master)

        # File menu
        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="Load package", accelerator='Ctrl+O', command=self._load_package)
        menu.add_command(label="Load Catalog", accelerator='Ctrl+G', command=self._load_catalog_file)
        menu.add_command(label="Load LST", accelerator='Ctrl+L', command=self._load_lst_file)
        menu.add_command(label="Load CSV Pack", accelerator='Ctrl+C', command=self._load_csv_file)
        menu.add_command(label="Filter", accelerator='Ctrl+F', command=self._filter_pack_content, state="disabled")
        menu.add_command(label="Export", accelerator='Ctrl+S', command=self._save_as)
        menu.add_command(label="Quit", accelerator='Ctrl+Q', command=master.quit)

        # Edit menu
        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Compare", menu=menu)
        menu.add_command(label="Compare LST", accelerator='Alt+Ctrl+L', command=self._compare_lst)
        menu.add_command(label="Compare CSV", accelerator='Alt+Ctrl+C', command=self._compare_csv)
        menu.add_command(label="Compare Catalogs", accelerator='Alt+Ctrl+G', command=self._compare_catalog)
        menu.add_command(label="Compare Mixed Files", accelerator='Alt+Ctrl+X', command=self._compare_mixed_pack)

        # Edit menu
        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=menu)
        menu.add_command(label="Select All", accelerator='Ctrl+A', command=self._select_all, state="disabled")
        menu.add_command(label="Copy", accelerator='Ctrl+C', command=self._copy_selection, state="disabled")
        menu.add_command(label="Bufferize", accelerator='Ctrl+B', command=self._copy_in_clipboard, state="disabled")

        # Help menu
        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=menu)
        menu.add_command(label="About", accelerator='Ctrl+H', command=self._app_credentials)

        try:
            master.config(menu=menubar)
        except AttributeError:
            # master is the top-level window
            master.tk.call(master, "config", "-menu", menubar)

        # Create Notebook frames
        gen_frame = Tk.Frame(master, width=400, height=200, name="general")
        app_frame = Tk.Frame(master, width=910, height=600, name="application")
        sys_frame = Tk.Frame(master, width=400, height=100, name="system")
        man_frame = Tk.Frame(master, width=400, height=100, name="manager")
        par_frame = Tk.Frame(master, width=910, height=600, name="parameter")
        ads_frame = Tk.Frame(master, width=910, height=600, name="adspar")
        unk_frame = Tk.Frame(master, width=400, height=100, name="unknown")

        self.gen_frame = gen_frame
        self.app_frame = app_frame
        self.sys_frame = sys_frame
        self.man_frame = man_frame
        self.par_frame = par_frame
        self.ads_frame = ads_frame
        self.unk_frame = unk_frame

        # Add frames to Notebook
        self.add(gen_frame, text="General")
        self.add(app_frame, text="Application")
        self.add(sys_frame, text="System")
        self.add(man_frame, text="Manager")
        self.add(par_frame, text="C3Config")
        self.add(ads_frame, text="ADS")
        self.add(unk_frame, text="Unknown")

        # Binding Keys with menu
        self.bind("<<NotebookTabChanged>>", self._on_tab_changed)
        master.bind('<Control-O>', self._load_package)
        master.bind('<Control-o>', self._load_package)
        master.bind('<Control-G>', self._load_catalog_file)
        master.bind('<Control-g>', self._load_catalog_file)
        master.bind('<Control-L>', self._load_lst_file)
        master.bind('<Control-l>', self._load_lst_file)
        master.bind('<Control-C>', self._load_csv_file)
        master.bind('<Control-c>', self._load_csv_file)
        master.bind('<Alt-Control-L>', self._compare_lst)
        master.bind('<Alt-Control-l>', self._compare_lst)
        master.bind('<Alt-Control-C>', self._compare_csv)
        master.bind('<Alt-Control-c>', self._compare_csv)
        master.bind('<Alt-Control-G>', self._compare_catalog)
        master.bind('<Alt-Control-g>', self._compare_catalog)
        master.bind('<Alt-Control-X>', self._compare_mixed_pack)
        master.bind('<Alt-Control-x>', self._compare_mixed_pack)
        master.bind('<Control-F>', self._filter_pack_content)
        master.bind('<Control-f>', self._filter_pack_content)
        master.bind('<Control-S>', self._save_as)
        master.bind('<Control-s>', self._save_as)
        master.bind('<Control-H>', self._app_credentials)
        master.bind('<Control-h>', self._app_credentials)
        master.bind('<Control-Q>', self._exit_app)
        master.bind('<Control-q>', self._exit_app)
        """
        master.bind('<Control-C>', self._select_all)
        master.bind('<Control-c>', self._select_all)
        master.bind('<Control-B>', self._copy_selection)
        master.bind('<Control-b>', self._copy_selection)
        master.bind('<Control-H>', self._copy_in_clipboard)
        master.bind('<Control-h>', self._copy_in_clipboard)
        """

        self.init_gen_treeview(master)
        self.init_app_treeview(master)
        self.init_sys_treeview(master)
        self.init_man_treeview(master)
        self.init_par_treeview(master)
        self.init_ads_treeview(master)
        self.init_unk_treeview(master)

    def _on_tab_changed(self, event):
        event.widget.update_idletasks()

        tab = event.widget.nametowidget(event.widget.select())
        event.widget.configure(height=tab.winfo_reqheight())

        tab_name = self.select()
        logPack.log_info(self.logger, "Selected Tab ==> %s" % tab_name)

        if tab_name == ".general":
            logPack.log_debug(self.logger, "Nothing to do")
        if tab_name == ".application":
            self.scroll_tab(self.app_tree)
        if tab_name == ".system":
            self.scroll_tab(self.sys_tree)
        if tab_name == ".manager":
            self.scroll_tab(self.man_tree)
        if tab_name == ".parameter":
            self.scroll_tab(self.par_tree)
        if tab_name == ".ads":
            self.scroll_tab(self.ads_tree)
        if tab_name == ".unknown":
            self.scroll_tab(self.unk_tree)

    def scroll_tab(self, tab_tree):
        self.main_scroll.config(command=tab_tree.yview)
        tab_tree.configure(yscrollcommand=self.main_scroll.set)

    def _exit_app(self, root=None):
        logPack.log_info(self.logger, "exit_app")
        self.master.quit()

    def _load_package(self, root=None):
        logPack.log_info(self.logger, "Enter load_package")
        if root is None:
            root = self.master
        root.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select package zip file",
                                                     filetypes=(("zip files", "*.zip"), ("all files", "*.zip")))
        logPack.log_debug(self.logger, root.filename)

        if root.filename in (None, ""):
            logPack.log_debug(self.logger, "User Cancellation => No file chosen")
            logPack.log_info(self.logger, "Exit load_package")
            return

        self._display_package_content(root)
        logPack.log_info(self.logger, "Exit load_package")

    def _load_catalog_file(self, root=None):
        logPack.log_info(self.logger, "Enter _load_catalog_file")
        if root is None:
            root = self.master
        root.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select Catalog file",
                                                     filetypes=(("prp files", "*.prp"), ("mxx files", "*.m**")))
        logPack.log_debug(self.logger, root.filename)

        if root.filename in (None, ""):
            logPack.log_debug(self.logger, "User Cancellation => No catalog file chosen")
            logPack.log_info(self.logger, "Exit _load_catalog_file")
            return

        # self.check_catalog(root, root.filename)
        self._display_catalog_content(root)
        logPack.log_info(self.logger, "Exit _load_catalog_file")

    def _load_lst_file(self, root=None):
        logPack.log_info(self.logger, "Enter _load_lst_file")
        if root is None:
            root = self.master
        root.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select RUNNING.LST file",
                                                     filetypes=(("lst files", "*.lst"), ("all files", "*.lst")))
        logPack.log_debug(self.logger, root.filename)

        if root.filename in (None, ""):
            logPack.log_debug(self.logger, "User Cancellation => No file chosen")
            logPack.log_info(self.logger, "Exit _load_lst_file")
            return

        self._display_lst_content(root)
        logPack.log_info(self.logger, "Exit _load_lst_file")

    def _load_csv_file(self, root=None):
        logPack.log_info(self.logger, "Enter _load_csv_file")
        if root is None:
            root = self.master
        root.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select PACKAGES.CSV file",
                                                     filetypes=(("csv files", "*.csv"), ("all files", "*.lst")))
        logPack.log_debug(self.logger, root.filename)

        if root.filename in (None, ""):
            logPack.log_debug(self.logger, "User Cancellation => No file chosen")
            logPack.log_info(self.logger, "Exit _load_csv_file")
            return

        self._display_csv_content(root)
        logPack.log_info(self.logger, "Exit _load_csv_file")

    def _filter_pack_content(self, root=None):
        logPack.log_info(self.logger, "Enter _filter_pack_content")
        print "_filter_pack_content"

        findUI = Tk.Toplevel(self)
        findUI.wm_geometry("700x150")
        findUI.title("Filter Content")
        findUI.lift()
        findUI.focus_force()
        findUI.grab_set()
        findUI.resizable(False, False)

        filter_text = Tk.Entry(findUI, width=50)
        filter_text.pack()

        filter_button = Tk.Button(findUI, text="Filter")
        filter_button.pack()

        logPack.log_info(self.logger, "Exit _filter_pack_content")

    def _save_as(self, root=None):
        logPack.log_info(self.logger, "Enter Save_as")

        #############################
        # Save as option
        options = {}
        options['defaultextension'] = "xlsx"
        options['filetypes'] = (("Excel files", "*.xlsx"), ("All Files", "*.*"))
        options['initialdir'] = "C:"
        options['initialfile'] = "depackager_export"
        options['title'] = "Depacker - Export results as..."

        # Ask for name and path
        filename = tkFileDialog.asksaveasfilename(**options)
        if filename in (None, ""):  # Manage cancellation
            return

        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook(filename)

        self._export_general(workbook)
        self._export_application(workbook)
        self._export_system(workbook)
        self._export_manager(workbook)
        self._export_c3config(workbook)
        self._export_ads(workbook)
        self._export_unknown(workbook)

        # close workbook
        workbook.close()
        logPack.log_info(self.logger, "Exit Save_as")

    def _export_general(self, workbook):
        # Create General purpose sheet
        gensheet = workbook.add_worksheet(name='General')

        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})

        # Defining header
        gensheet.merge_range('A1:B2', 'Depackager 1.0 - Results export', header_format)
        gensheet.write('A3', 'Package Name', header_format)
        gensheet.write('A4', 'Number Of Files', header_format)
        gensheet.write('A5', 'Catalog Name', header_format)
        gensheet.write('A6', 'SDK Version', header_format)
        gensheet.write('A7', 'System Version', header_format)
        gensheet.write('A8', 'Manager Version', header_format)

        pack_name = ntpath.basename(self.loaded_package['general'].get('pack_name'))
        pack_name, _ = os.path.splitext(pack_name)
        gensheet.write(2, 1, pack_name)

        gensheet.write(3, 1, self.loaded_package['general'].get('file_number'))
        gensheet.write(4, 1, self.loaded_package['general'].get('catalog_name'))
        gensheet.write(5, 1, self.loaded_package['general'].get('sdk_version'))
        gensheet.write(6, 1, self.loaded_package['general'].get('system_version'))
        gensheet.write(7, 1, self.loaded_package['general'].get('manager_version'))

    def _export_application(self, workbook):
        logPack.log_info(self.logger, "Enter _export_application")
        # Create Application sheet
        appsheet = workbook.add_worksheet(name='Application')

        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})

        # Defining header
        appsheet.merge_range('A1:F1', 'Application Components', header_format)
        appsheet.write('A2', 'Trigram', header_format)
        appsheet.write('B2', 'Number', header_format)
        appsheet.write('C2', 'Version', header_format)
        appsheet.write('D2', 'File Name', header_format)
        appsheet.write('E2', 'Full Name', header_format)
        appsheet.write('F2', 'Type', header_format)

        # populating sheet cells
        number = 1
        for tree_row in self.app_tree.get_children():
            number = number + 1

            fg_color = dict_tag_to_fgcolor.get(' ')
            if len(self.app_tree.item(tree_row)['tags']):
                fg_color = dict_tag_to_fgcolor.get(self.app_tree.item(tree_row)['tags'][0])

            line_format = workbook.add_format({
                'valign': 'vcenter',
                'fg_color': fg_color})

            appsheet.write(number, 0, self.app_tree.item(tree_row)['values'][0], line_format)
            appsheet.write(number, 1, self.app_tree.item(tree_row)['values'][1], line_format)
            appsheet.write(number, 2, self.app_tree.item(tree_row)['values'][2], line_format)
            appsheet.write(number, 3, self.app_tree.item(tree_row)['values'][3], line_format)
            appsheet.write(number, 4, self.app_tree.item(tree_row)['values'][4], line_format)
            appsheet.write(number, 5, self.app_tree.item(tree_row)['values'][5], line_format)

        logPack.log_info(self.logger, "Exit _export_application")

    def _export_system(self, workbook):
        logPack.log_info(self.logger, "Enter _export_system")
        # Create Manager sheet
        syssheet = workbook.add_worksheet(name='System')

        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})

        # Defining header
        syssheet.merge_range('A1:E1', 'System Components', header_format)

        syssheet.write('A2', 'Number', header_format)
        syssheet.write('B2', 'Version', header_format)
        syssheet.write('C2', 'File Name', header_format)
        syssheet.write('D2', 'Full Name', header_format)
        syssheet.write('E2', 'Type', header_format)

        # populating sheet cells
        number = 1
        for tree_row in self.sys_tree.get_children():
            number = number + 1

            fg_color = dict_tag_to_fgcolor.get(' ')
            if len(self.sys_tree.item(tree_row)['tags']):
                fg_color = dict_tag_to_fgcolor.get(self.sys_tree.item(tree_row)['tags'][0])

            line_format = workbook.add_format({
                'valign': 'vcenter',
                'fg_color': fg_color})

            syssheet.write(number, 0, self.sys_tree.item(tree_row)['values'][0], line_format)
            syssheet.write(number, 1, self.sys_tree.item(tree_row)['values'][1], line_format)
            syssheet.write(number, 2, self.sys_tree.item(tree_row)['values'][2], line_format)
            syssheet.write(number, 3, self.sys_tree.item(tree_row)['values'][3], line_format)
            syssheet.write(number, 4, self.sys_tree.item(tree_row)['values'][4], line_format)

        logPack.log_info(self.logger, "Exit _export_system")

    def _export_manager(self, workbook):
        logPack.log_info(self.logger, "Enter _export_manager")
        # Create Manager sheet
        mansheet = workbook.add_worksheet(name='Manager')

        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})

        # Defining header
        mansheet.merge_range('A1:E1', 'Manager Components', header_format)

        mansheet.write('A2', 'Number', header_format)
        mansheet.write('B2', 'Version', header_format)
        mansheet.write('C2', 'File Name', header_format)
        mansheet.write('D2', 'Full Name', header_format)
        mansheet.write('E2', 'Type', header_format)

        # populating sheet cells
        number = 1
        for tree_row in self.man_tree.get_children():
            number = number + 1

            fg_color = dict_tag_to_fgcolor.get(' ')
            if len(self.man_tree.item(tree_row)['tags']):
                fg_color = dict_tag_to_fgcolor.get(self.man_tree.item(tree_row)['tags'][0])

            line_format = workbook.add_format({
                'valign': 'vcenter',
                'fg_color': fg_color})

            mansheet.write(number, 0, self.man_tree.item(tree_row)['values'][0], line_format)
            mansheet.write(number, 1, self.man_tree.item(tree_row)['values'][1], line_format)
            mansheet.write(number, 2, self.man_tree.item(tree_row)['values'][2], line_format)
            mansheet.write(number, 3, self.man_tree.item(tree_row)['values'][3], line_format)
            mansheet.write(number, 4, self.man_tree.item(tree_row)['values'][4], line_format)

        logPack.log_info(self.logger, "Exit _export_manager")

    def _export_c3config(self, workbook):
        logPack.log_info(self.logger, "Enter _export_c3config")
        # Create C3Config sheet
        c3csheet = workbook.add_worksheet(name='C3Config')

        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})

        # Defining header
        c3csheet.merge_range('A1:C1', 'C3Config Parameters Used', header_format)

        c3csheet.write('A2', 'Parameter Name', header_format)
        c3csheet.write('B2', 'Parameter Value', header_format)
        c3csheet.write('C2', 'Comments', header_format)

        # populating sheet cells
        number = 1
        for tree_row in self.par_tree.get_children():
            # if self.par_tree.item(tree_row)['tags'][0] == 'used':
            number = number + 1

            fg_color = dict_tag_to_fgcolor.get(' ')
            if len(self.par_tree.item(tree_row)['tags']):
                fg_color = dict_tag_to_fgcolor.get(self.par_tree.item(tree_row)['tags'][0])

            line_format = workbook.add_format({
                'valign': 'vcenter',
                'fg_color': fg_color})

            c3csheet.write(number, 0, self.par_tree.item(tree_row)['values'][0], line_format)
            c3csheet.write(number, 1, self.par_tree.item(tree_row)['values'][1], line_format)
            c3csheet.write(number, 2, self.par_tree.item(tree_row)['values'][2], line_format)

        logPack.log_info(self.logger, "Exit _export_c3config")

    def _export_ads(self, workbook):
        logPack.log_info(self.logger, "Enter _export_ads")
        # Create ADS sheet
        adssheet = workbook.add_worksheet(name='ADS')

        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})

        # Defining header
        adssheet.merge_range('A1:C1', 'ADS Parameters Used', header_format)

        adssheet.write('A2', 'Parameter Name', header_format)
        adssheet.write('B2', 'Parameter Value', header_format)
        adssheet.write('C2', 'Comments', header_format)

        # populating sheet cells
        number = 1
        for tree_row in self.ads_tree.get_children():
            # if self.ads_tree.item(tree_row)['tags'][0] == 'used':
            number = number + 1

            fg_color = dict_tag_to_fgcolor.get(' ')
            if len(self.ads_tree.item(tree_row)['tags']):
                fg_color = dict_tag_to_fgcolor.get(self.ads_tree.item(tree_row)['tags'][0])

            line_format = workbook.add_format({
                'valign': 'vcenter',
                'fg_color': fg_color})

            adssheet.write(number, 0, self.ads_tree.item(tree_row)['values'][0], line_format)
            adssheet.write(number, 1, self.ads_tree.item(tree_row)['values'][1], line_format)
            adssheet.write(number, 2, self.ads_tree.item(tree_row)['values'][2], line_format)

        logPack.log_info(self.logger, "Exit _export_ads")

    def _export_unknown(self, workbook):
        logPack.log_info(self.logger, "Enter _export_unknown")
        # Create Unknown sheet
        unksheet = workbook.add_worksheet(name='Unknown')

        header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})

        # Defining header
        unksheet.merge_range('A1:B1', 'Unknown Components', header_format)

        unksheet.write('A2', 'File Name', header_format)
        unksheet.write('B2', 'File Type', header_format)

        # populating sheet cells
        number = 1
        for tree_row in self.unk_tree.get_children():
            number = number + 1

            fg_color = dict_tag_to_fgcolor.get(' ')
            if len(self.unk_tree.item(tree_row)['tags']):
                fg_color = dict_tag_to_fgcolor.get(self.unk_tree.item(tree_row)['tags'][0])

            line_format = workbook.add_format({
                'valign': 'vcenter',
                'fg_color': fg_color})

            unksheet.write(number, 0, self.unk_tree.item(tree_row)['values'][0], line_format)
            unksheet.write(number, 1, self.unk_tree.item(tree_row)['values'][1], line_format)
        logPack.log_info(self.logger, "Exit _export_unknown")

    def _app_credentials(self, root=None):
        logPack.log_info(self.logger, "Enter _app_credentials")
        about_ui = Tk.Toplevel(self)
        about_ui.wm_geometry("500x150")
        about_ui.title("De-Packager Credentials")
        about_ui.lift()
        about_ui.focus_force()
        about_ui.grab_set()
        about_ui.resizable(False, False)

        about_title = Tk.Label(about_ui, text="De-Packager Credentials", fg="black",
                               anchor=Tkconstants.W, font=("Helvetica", 12))
        about_title.grid_bbox(row=1, column=0)
        about_title.pack()

        about_company = Tk.Label(about_ui, text="Copyright Ⓒ 2018 - Ingenico - Beyond Payment", fg="black",
                                 anchor=Tkconstants.W, font=("Helvetica", 8))
        about_company.grid(row=3, column=0)
        about_company.pack()

        about_right = Tk.Label(about_ui, text="All rights reserved", fg="black",
                               anchor=Tkconstants.W, font=("Helvetica", 8))
        about_right.grid(row=5, column=0)
        about_right.pack()

        about_version = Tk.Label(about_ui, text="Version De-Packager " + __version__, fg="black",
                                 anchor=Tkconstants.W, font=("Helvetica", 8))
        about_version.grid(row=7, column=0)
        about_version.pack()

        logPack.log_info(self.logger, "Exit _app_credentials")

    def _select_all(self, root=None):
        logPack.log_info(self.logger, "select_all")

    def _copy_selection(self, root=None):
        logPack.log_info(self.logger, "copy_selection")

    def _copy_in_clipboard(self, root=None):
        logPack.log_info(self.logger, "copy_in_clipboard")

    def _display_catalog_content(self, root=None):
        logPack.log_info(self.logger, "Enter _display_catalog_content")
        logPack.log_debug(self.logger, root.filename)

        # Init loaded_package
        self.loaded_package = AppUI.default_package
        self.init_loaded_package(root)

        cat_content = self._get_cat_content(root.filename)

        file_path, file_name = os.path.split(root.filename)
        self.loaded_package['general']['catalog_name'] = file_name
        self._populate_pack_infos(cat_content, root)

        logPack.log_info(self.logger, "Exit _display_catalog_content")

    def _display_csv_content(self, root=None):
        logPack.log_info(self.logger, "Enter _display_csv_content")
        logPack.log_debug(self.logger, root.filename)

        # Init loaded_package
        self.loaded_package = AppUI.default_package
        self.init_loaded_package(root)

        csv_content = self._get_csv_content(root.filename)

        file_path, file_name = os.path.split(root.filename)
        self.loaded_package['general']['catalog_name'] = file_name
        self._populate_pack_infos(csv_content, root)

        logPack.log_info(self.logger, "Exit _display_csv_content")

    def _display_lst_content(self, root=None):
        logPack.log_info(self.logger, "Enter _display_lst_content")
        logPack.log_debug(self.logger, root.filename)

        # Init loaded_package
        self.loaded_package = AppUI.default_package
        self.init_loaded_package(root)

        lst_content = self._get_lst_content(root.filename)

        file_path, file_name = os.path.split(root.filename)
        self.loaded_package['general']['catalog_name'] = file_name
        self._populate_pack_infos(lst_content, root)

        logPack.log_info(self.logger, "Exit _display_lst_content")

    def _display_package_content(self, root=None):
        logPack.log_info(self.logger, "Enter _display_package_content")
        logPack.log_debug(self.logger, root.filename)

        # Init loaded_package
        self.loaded_package = AppUI.default_package
        self.init_loaded_package(root)

        file_list = Zip.read_zipfile(root.filename)
        self._populate_pack_infos(file_list, root)
        logPack.log_info(self.logger, "Exit _display_package_content")

    def _populate_pack_infos(self, file_list, root=None):
        logPack.log_info(self.logger, "Enter _populate_pack_infos")
        file_number = 0

        for f in file_list:
            file_number += 1
            if len(self.loaded_package['general']['catalog_name']) == 0:
                self.check_catalog(root, f)

            if len(self.loaded_package['parameter']) == 0:
                self.check_parameter(root, f)

            if len(self.loaded_package['ads_param']) == 0:
                self.check_ads_parameter(root, f)

            if self.loaded_package['general']['sdk_version'].upper().startswith("XX.YY."):
                self.check_t3_sdk_version(f)

            cpn_app = cpnmgt.app_component_present(f)
            if cpn_app != cpnmgt.unknown_component:
                tmp_list = list(cpn_app)
                tmp_list = tmp_list + [f]

                tmp_comp = tmp_list[4]
                tmp_list[3] = cpnmgt.dict_file_types.get(tmp_comp[-3:].upper())
                index = tmp_comp.find(tmp_list[0]) + len(tmp_list[0])
                comp_version = tmp_comp[index:index + 4]

                if comp_version.isdigit():
                    tmp_list = tmp_list + [comp_version[:2] + "." + comp_version[2:]]
                else:
                    tmp_list = tmp_list + [" "]

                tmp_tuple = tuple(tmp_list)
                self.loaded_package['application'].append(tmp_tuple)

            cpn_sys = cpnmgt.sys_component_present(f)
            if cpn_sys != cpnmgt.unknown_component:
                tmp_list = list(cpn_sys)
                tmp_list = tmp_list + [f]

                tmp_comp = tmp_list[3]
                tmp_list[2] = cpnmgt.dict_file_types.get(tmp_comp[-3:].upper())
                index = tmp_comp.find(tmp_list[0]) + len(tmp_list[0])
                comp_version = tmp_comp[index:index + 4]

                if comp_version.isdigit():
                    sversion = comp_version[:2] + "." + comp_version[2:]
                    tmp_list = tmp_list + [sversion]
                    if cpnmgt.check_system_pack(cpn_sys[0]):
                        self.loaded_package['general']['system_version'] = sversion
                else:
                    tmp_list = tmp_list + [" "]

                tmp_tuple = tuple(tmp_list)
                self.loaded_package['system'].append(tmp_tuple)

            cpn_man = cpnmgt.man_component_present(f)
            if cpn_man != cpnmgt.unknown_component:
                tmp_list = list(cpn_man)
                tmp_list = tmp_list + [f]

                tmp_comp = tmp_list[3]
                tmp_list[2] = cpnmgt.dict_file_types.get(tmp_comp[-3:].upper())
                index = tmp_comp.find(tmp_list[0]) + len(tmp_list[0])
                comp_version = tmp_comp[index:index + 4]

                if comp_version.isdigit():
                    sversion = "%s.%s" % (comp_version[:2], comp_version[2:])
                    tmp_list = tmp_list + [sversion]
                    if cpnmgt.check_manager_pack(cpn_man[0]):
                        self.loaded_package['general']['manager_version'] = sversion
                else:
                    tmp_list = tmp_list + [" "]

                tmp_tuple = tuple(tmp_list)
                self.loaded_package['manager'].append(tmp_tuple)

            if cpn_app == cpn_sys and cpn_app == cpn_man:
                tmp_list = list(cpn_man)
                tmp_list = tmp_list + [f]

                tmp_tuple = tuple(tmp_list)
                self.loaded_package['unknown'].append(tmp_tuple)

        if self.loaded_package['general']['sdk_version'].upper().startswith("XX.YY."):
            self.loaded_package['general']['sdk_version'] = cpnmgt.get_sdk_version(
                self.loaded_package['general'].get('system_version'),
                self.loaded_package['general'].get('manager_version')
            )
        self.loaded_package['general']['file_number'] = file_number
        self._populate_gui()
        logPack.log_info(self.logger, "Exit _populate_pack_infos")

    def _populate_gui(self):
        logPack.log_info(self.logger, "Enter _populate_gui")
        self._populate_gen_frame()
        self._populate_app_frame()
        self._populate_sys_frame()
        self._populate_man_frame()
        self._populate_unk_frame()

        if self.loaded_package['general'].get('catalog_name') != cpnmgt.ndiff_catalog_name:
            self._populate_par_frame()
            self._populate_ads_frame()

        logPack.log_info(self.logger, "Exit _populate_gui")

    def _populate_gen_frame(self):
        logPack.log_info(self.logger, "Enter _populate_gen_frame")
        gen_components = self.loaded_package['general']

        pack_name = ntpath.basename(self.loaded_package['general'].get('pack_name'))
        pack_name, _ = os.path.splitext(pack_name)

        w = Tk.Label(self.gen_frame, text="Pack Name: ", width=12, fg="black",
                     anchor=Tkconstants.E, font=("Helvetica", 10))
        w.grid(row=0, column=0)
        wl = Tk.Label(self.gen_frame, text=pack_name, width=30, fg="blue",
                      anchor=Tkconstants.W, font=("Helvetica", 10))
        wl.grid(row=0, column=1)

        w2 = Tk.Label(self.gen_frame, text="N° of files: ", width=12,
                      fg="black", anchor=Tkconstants.E, font=("Helvetica", 10))
        w2.grid(row=0, column=2)
        wl2 = Tk.Label(self.gen_frame, text=self.loaded_package['general'].get('file_number'),
                       width=10, fg="blue", anchor=Tkconstants.W, font=("Helvetica", 10))
        wl2.grid(row=0, column=3)

        w3 = Tk.Label(self.gen_frame, text="Catalog: ", width=12,
                      fg="black", anchor=Tkconstants.E, font=("Helvetica", 10))
        w3.grid(row=0, column=4)
        w3l = Tk.Label(self.gen_frame, text=self.loaded_package['general'].get('catalog_name'),
                       width=22, fg="blue", anchor=Tkconstants.W, font=("Helvetica", 10))
        w3l.grid(row=0, column=5)

        # w2 = Tk.Label(self.gen_frame, text="Terminal: ", relief=Tkconstants.RIDGE, width=22, fg="blue", anchor=Tkconstants.E, font=("Helvetica", 10))
        # w2.grid(row=0, column=6)

        w4 = Tk.Label(self.gen_frame, text="SDK Version: ", width=12, fg="black",
                      anchor=Tkconstants.E, font=("Helvetica", 10))
        w4.grid(row=1, column=0)
        w4l = Tk.Label(self.gen_frame, text=self.loaded_package['general'].get('sdk_version'),
                       width=30, fg="blue", anchor=Tkconstants.W, font=("Helvetica", 10))
        w4l.grid(row=1, column=1)

        w5 = Tk.Label(self.gen_frame, text="System: ", width=12, fg="black", anchor=Tkconstants.E,
                      font=("Helvetica", 10))
        w5.grid(row=1, column=2)
        w5l = Tk.Label(self.gen_frame, text=self.loaded_package['general'].get('system_version'),
                       width=10, fg="blue", anchor=Tkconstants.W, font=("Helvetica", 10))
        w5l.grid(row=1, column=3)

        w6 = Tk.Label(self.gen_frame, text="Manager: ", width=12, fg="black", anchor=Tkconstants.E,
                      font=("Helvetica", 10))
        w6.grid(row=1, column=4)
        w6l = Tk.Label(self.gen_frame, text=self.loaded_package['general'].get('manager_version'),
                       width=22, fg="blue", anchor=Tkconstants.W, font=("Helvetica", 10))
        w6l.grid(row=1, column=5)

        for cpn in gen_components:
            logPack.log_debug(self.logger, cpn)
        logPack.log_info(self.logger, "Exit _populate_gen_frame")

    def _populate_app_frame(self):
        logPack.log_info(self.logger, "Enter _populate_app_frame")
        app_components = self.loaded_package['application']
        app_tree = self.app_tree

        # Empty TreeView
        items = app_tree.get_children()
        for item in items:
            app_tree.delete(item)

        # Populate TreeView
        for app in app_components:
            if len(app) == 7:
                app_tree.insert('', 'end', values=(app[1], app[0], app[5], app[4], app[2], app[3]),
                                tags=(app[6]), )
            else:
                app_tree.insert('', 'end', values=(app[1], app[0], app[5], app[4], app[2], app[3]),
                                tags=(self.in_catalog(app[0]),))

        self.app_tree = app_tree
        logPack.log_info(self.logger, "Exit _populate_app_frame")

    def _populate_sys_frame(self):
        logPack.log_info(self.logger, "Enter _populate_sys_frame")
        sys_components = self.loaded_package['system']
        sys_tree = self.sys_tree

        # Empty TreeView
        items = sys_tree.get_children()
        for item in items:
            sys_tree.delete(item)

        # Populate TreeView
        for app in sys_components:
            if len(app) == 6:
                sys_tree.insert('', 'end', values=(app[0], app[4], app[3], app[1], app[2]),
                                tags=(app[5],))
            else:
                sys_tree.insert('', 'end', values=(app[0], app[4], app[3], app[1], app[2]),
                                tags=(self.in_catalog(app[0]),))

        self.sys_tree = sys_tree
        logPack.log_info(self.logger, "Exit _populate_sys_frame")

    def _populate_man_frame(self):
        logPack.log_info(self.logger, "Enter _populate_man_frame")
        man_components = self.loaded_package['manager']
        man_tree = self.man_tree

        # Empty TreeView
        items = man_tree.get_children()
        for item in items:
            man_tree.delete(item)

        # Populate TreeView
        for app in man_components:
            if len(app) == 6:
                man_tree.insert('', 'end', values=(app[0], app[4], app[3], app[1], app[2]),
                                tags=(app[5],))
            else:
                man_tree.insert('', 'end', values=(app[0], app[4], app[3], app[1], app[2]),
                                tags=(self.in_catalog(app[0]),))

        self.man_tree = man_tree
        logPack.log_info(self.logger, "Exit _populate_man_frame")

    def _populate_par_frame(self):
        logPack.log_info(self.logger, "Enter _populate_par_frame")
        # par_components = self.loaded_package['parameter']
        par_tree = self.par_tree

        # Empty TreeView
        items = par_tree.get_children()
        for item in items:
            par_tree.delete(item)

        # Populate TreeView
        for (par_name, par_desc) in cpnmgt.c3config_params:
            par_tag, par_value = self.param_is_used(par_name)
            par_tree.insert('', 'end', values=(par_name, par_value, par_desc), tags=(par_tag,))

        self.par_tree = par_tree
        logPack.log_info(self.logger, "Exit _populate_par_frame")

    def _populate_ads_frame(self):
        logPack.log_info(self.logger, "Enter _populate_ads_frame")
        # ads_components = self.loaded_package['ads_param']
        ads_tree = self.ads_tree

        # Empty TreeView
        items = ads_tree.get_children()
        for item in items:
            ads_tree.delete(item)

        # Populate TreeView
        for (par_name, par_desc) in cpnmgt.ads_params:
            par_tag, par_value = self.param_ads_is_used(par_name)
            ads_tree.insert('', 'end', values=(par_name, par_value.replace("'", "\'"), par_desc), tags=(par_tag,))

        self.ads_tree = ads_tree
        logPack.log_info(self.logger, "Exit _populate_ads_frame")

    def param_is_used(self, par_name):
        logPack.log_info(self.logger, "Enter param_is_used")
        par_components = self.loaded_package['parameter']
        if len(par_components) == 0:
            return "unknown", " "
        for par_cpn in par_components:
            if par_cpn.startswith(par_name):
                par_value = par_cpn[par_cpn.find("=") + 1:]
                return "used", par_value.lstrip(" ")
        logPack.log_info(self.logger, "Exit param_is_used")
        return "unused", " "

    def param_ads_is_used(self, par_name):
        logPack.log_info(self.logger, "Enter param_ads_is_used")
        par_components = self.loaded_package['ads_param']
        if len(par_components) == 0:
            return "unknown", " "
        for par_cpn in par_components:
            if par_cpn.startswith(par_name):
                par_value = par_cpn[par_cpn.find("=") + 1:]
                comment_index = par_value.find("#")
                if comment_index != 0:
                    par_value = par_value[:comment_index]
                return "used", par_value.lstrip(" ")
        logPack.log_info(self.logger, "Exit param_ads_is_used")
        return "unused", " "

    def _populate_unk_frame(self, root=None):
        logPack.log_info(self.logger, "Enter _populate_unk_frame")
        unk_components = self.loaded_package['unknown']
        unk_tree = self.unk_tree

        # Empty TreeView
        items = unk_tree.get_children()
        for item in items:
            unk_tree.delete(item)

        # Populate TreeView
        for app in unk_components:
            if len(app) == 5:
                unk_tree.insert('', 'end', values=(str(app[3]), '-'), tags=(app[4],))
            else:
                unk_tree.insert('', 'end', values=(app[3], '-'), tags=(self.in_catalog(app[3]),))

        logPack.log_info(self.logger, "Exit _populate_unk_frame")

    def check_t3_sdk_version(self, the_file):
        logPack.log_info(self.logger, "Enter check_t3_sdk_version")
        file_name, file_ext = os.path.splitext(the_file)
        if file_name[:8] in cpnmgt.t3_sdk_pack and file_name.find("SDK") > 0 and file_ext.upper() == ".P3P":
            logPack.log_debug(self.logger, "SDK version file found : %s.%s" % (file_name, file_ext))
            sdk_version = cpnmgt.get_t3_sdk_version(file_name)
            sdk_version = sdk_version[:2] + "." + sdk_version[2:4] + "." + sdk_version[4:]
            actual_sdk_version = self.loaded_package['general']['sdk_version'].upper()

            if actual_sdk_version.startswith("XX.YY"):
                self.loaded_package['general']['sdk_version'] = sdk_version
            else:
                self.loaded_package['general']['sdk_version'] = actual_sdk_version + " vs " + sdk_version

            logPack.log_debug(self.logger, "SDK Version: " + self.loaded_package['general']['sdk_version'])
            logPack.log_debug(self.logger, self.loaded_package['parameter'])
        logPack.log_info(self.logger, "Exit check_t3_sdk_version")

    def check_parameter(self, root, the_file):
        logPack.log_info(self.logger, "Enter check_parameter")
        file_name, file_ext = os.path.splitext(the_file)
        if file_name.upper() == "C3CONFIG":
            logPack.log_debug(self.logger, "c3config found : %s.%s" % (file_name, file_ext))
            self.update_parameter(root, the_file)
            logPack.log_debug(self.logger, self.loaded_package['parameter'])
        logPack.log_info(self.logger, "Exit check_parameter")

    def check_ads_parameter(self, root, the_file):
        logPack.log_info(self.logger, "Enter check_ads_parameter")
        file_name, file_ext = os.path.splitext(the_file)
        if file_name.upper().startswith("ADS") and file_ext.upper() == ".PAR":
            logPack.log_debug(self.logger, "ads.par found : %s.%s" % (file_name, file_ext))
            self.update_ads_param(root, the_file)
            logPack.log_debug(self.logger, self.loaded_package['ads_param'])
        logPack.log_info(self.logger, "Exit check_ads_parameter")

    def update_parameter(self, root, param_file):
        logPack.log_info(self.logger, "Enter update_parameter")
        param_content = Zip.read_file_content(root.filename, param_file)
        logPack.log_debug(self.logger, "Parameter file is %s" % param_file)
        # Update Parameter_List
        for line in param_content.readlines():
            if not (line.startswith("#") or line == "\r\n"):
                self.loaded_package['parameter'].append(line.rstrip("\r\n"))
        logPack.log_info(self.logger, "Exit update_parameter")

    def update_ads_param(self, root, param_file):
        logPack.log_info(self.logger, "Enter update_ads_param")
        try:
            param_content = Zip.read_file_content(root.filename, param_file)
            logPack.log_debug(self.logger, "ADS.PAR file is %s" % param_file)
        except AttributeError:
            logPack.log_error(self.logger, "Not a zip file => No filename")
            logPack.log_info(self.logger, "Exit update_ads_param")
            return

        if param_content is None:
            logPack.log_info(self.logger, "No ADS File Found")
            logPack.log_info(self.logger, "Exit update_ads_param")
            return
        # Update Parameter_List
        for line in param_content.readlines():
            if not (line.startswith("#") or line == "\r\n"):
                self.loaded_package['ads_param'].append(line.rstrip("\r\n"))
        logPack.log_info(self.logger, "Exit update_ads_param")

    def check_catalog(self, root, the_file):
        logPack.log_info(self.logger, "Enter check_catalog")
        file_name, file_ext = os.path.splitext(the_file)

        if file_ext.upper() in cpnmgt.catalog_list:
            logPack.log_debug(self.logger,
                              "Catalog found\n Catalog Name : %s\n Catalog Ext. : %s" % (file_name, file_ext))
            self.update_llt_catalog(root, the_file)
            self.loaded_package['general']['catalog_name'] = file_name

        elif file_ext.upper() == ".PRP":
            logPack.log_debug(self.logger,
                              "Catalog found\n Catalog Name : %s\n Catalog Ext. : %s" % (file_name, file_ext))
            self.update_cal_catalog(root, the_file)
            self.loaded_package['general']['catalog_name'] = file_name
        logPack.log_info(self.logger, "Exit check_catalog")

    def update_llt_catalog(self, root, catal_file):
        logPack.log_info(self.logger, "Enter update_catalog")
        catal_content = Zip.read_file_content(root.filename, catal_file)
        logPack.log_debug(self.logger, "Catalog file is %s" % catal_file)
        # Update Catalog_List
        for line in catal_content.readlines():
            if not line.startswith(";"):
                self.loaded_package['general']['catalog_list'].append(line)
        logPack.log_info(self.logger, "Exit update_catalog")

    def update_cal_catalog(self, root, catal_file):
        logPack.log_info(self.logger, "Enter update_catalog")
        catal_content = Zip.read_file_content(root.filename, catal_file)
        logPack.log_debug(self.logger, "Catalog file is %s" % catal_file)
        # Update Catalog_List
        for line in catal_content.readlines():
            if not line.startswith("#"):
                self.loaded_package['general']['catalog_list'].append(line[line.find('=') + 1:])
        logPack.log_info(self.logger, "Exit update_catalog")

    def in_catalog(self, comp_name):
        logPack.log_info(self.logger, "Enter in_catalog")
        the_catalog = self.loaded_package['general']['catalog_list']
        if len(the_catalog) == 0:
            return "unknown"
        for comp in the_catalog:
            if comp.lower().startswith(comp_name.lower()):
                return "used"
        logPack.log_info(self.logger, "Exit in_catalog")
        return "unused"

    def init_loaded_package(self, root):
        logPack.log_info(self.logger, "Enter init_loaded_package")
        try:
            self.loaded_package['general']['security_components'] = []
            self.loaded_package['application'] = []
            self.loaded_package['system'] = []
            self.loaded_package['manager'] = []
            self.loaded_package['parameter'] = []
            self.loaded_package['ads_param'] = []
            self.loaded_package['unknown'] = []

            self.loaded_package['general']['catalog_name'] = ''
            self.loaded_package['general']['catalog_list'] = []
            self.loaded_package['general']['file_number'] = 0
            self.loaded_package['general']['system_version'] = 'XX.XX'
            self.loaded_package['general']['manager_version'] = 'YY.YY'
            self.loaded_package['general']['sdk_version'] = 'XX.YY.ZZ'
            self.loaded_package['general']['terminal_addressed'] = ''
            self.loaded_package['general']['ads_par'] = 0
            self.loaded_package['general']['manager_par'] = 0
            self.loaded_package['general']['c3config_t'] = 0
            self.loaded_package['general']['pack_name'] = root.filename
        except AttributeError:
            return
        logPack.log_info(self.logger, "Exit init_loaded_package")

    def init_gen_treeview(self, master):
        logPack.log_info(self.logger, "Enter init_gen_treeview")

        self.gen_tree = Ttk.Treeview(self.gen_frame, columns=(1, 2, 3, 4), height=40, selectmode="extended",
                                     show="headings")
        self.gen_tree.pack()

        self.gen_tree.heading(1, text="Trigram")
        self.gen_tree.heading(2, text="File Name")
        self.gen_tree.heading(3, text="Full Name")
        self.gen_tree.heading(4, text="Type")

        self.gen_tree.column(1, width=250, anchor=Tkconstants.W)
        self.gen_tree.column(2, width=250, anchor=Tkconstants.W)
        self.gen_tree.column(3, width=350, anchor=Tkconstants.W)
        self.gen_tree.column(4, width=150, anchor=Tkconstants.W)

        self.gen_tree.tag_configure('used', background=('pale green'))
        self.gen_tree.tag_configure('unused', background=('light coral'))
        self.gen_tree.tag_configure('unknown', background=('light blue'))

        self.gen_tree.grid(row=4, columnspan=6, sticky='nsew')

        logPack.log_info(self.logger, "Exit init_gen_treeview")

    def init_app_treeview(self, master):
        logPack.log_info(self.logger, "Enter init_app_treeview")
        self.app_tree = Ttk.Treeview(self.app_frame, columns=(1, 2, 3, 4, 5, 6), height=40, selectmode="extended",
                                     show="headings")
        self.app_tree.pack()

        self.app_tree.heading(1, text="Trigram")
        self.app_tree.heading(2, text="Number")
        self.app_tree.heading(3, text="Version")
        self.app_tree.heading(4, text="File Name")
        self.app_tree.heading(5, text="Full Name")
        self.app_tree.heading(6, text="Type")

        self.app_tree.column(1, width=150, anchor=Tkconstants.W)
        self.app_tree.column(2, width=150, anchor=Tkconstants.W)
        self.app_tree.column(3, width=100, anchor=Tkconstants.E)
        self.app_tree.column(4, width=200, anchor=Tkconstants.W)
        self.app_tree.column(5, width=250, anchor=Tkconstants.W)
        self.app_tree.column(6, width=150, anchor=Tkconstants.W)

        self.app_tree.tag_configure('used', background=('pale green'))  # dict_tag_to_fgcolor.get('used')
        self.app_tree.tag_configure('unused', background=('light coral'))
        self.app_tree.tag_configure('unknown', background=('light blue'))
        self.app_tree.tag_configure('+', background=('pale green'))
        self.app_tree.tag_configure('-', background=('light coral'))
        self.app_tree.tag_configure(' ', background=('white'))

        # Toggle vertical scrolbar
        self.main_scroll = Ttk.Scrollbar(master, orient="vertical", command=self.app_tree.yview)
        self.main_scroll.pack(side='right', fill='y')
        self.app_tree.configure(yscrollcommand=self.main_scroll.set)
        logPack.log_info(self.logger, "Exit init_app_treeview")

    def init_sys_treeview(self, master):
        logPack.log_info(self.logger, "Enter init_sys_treeview")
        self.sys_tree = Ttk.Treeview(self.sys_frame, columns=(1, 2, 3, 4, 5), height=40, selectmode="extended",
                                     show="headings")
        self.sys_tree.pack()

        self.sys_tree.heading(1, text="Number")
        self.sys_tree.heading(2, text="Version")
        self.sys_tree.heading(3, text="File Name")
        self.sys_tree.heading(4, text="Full Name")
        self.sys_tree.heading(5, text="Type")

        self.sys_tree.column(1, width=150, anchor=Tkconstants.CENTER)
        self.sys_tree.column(2, width=100, anchor=Tkconstants.W)
        self.sys_tree.column(3, width=300, anchor=Tkconstants.W)
        self.sys_tree.column(4, width=300, anchor=Tkconstants.W)
        self.sys_tree.column(5, width=150, anchor=Tkconstants.W)

        self.sys_tree.tag_configure('used', background=('pale green'))
        self.sys_tree.tag_configure('unused', background=('light coral'))
        self.sys_tree.tag_configure('unknown', background=('light blue'))
        self.sys_tree.tag_configure('+', background=('pale green'))
        self.sys_tree.tag_configure('-', background=('light coral'))
        self.sys_tree.tag_configure(' ', background=('white'))

        logPack.log_info(self.logger, "Exit init_sys_treeview")

    def init_man_treeview(self, master):
        logPack.log_info(self.logger, "Enter init_man_treeview")
        self.man_tree = Ttk.Treeview(self.man_frame, columns=(1, 2, 3, 4, 5), height=40,
                                     selectmode="extended", show="headings")
        self.man_tree.pack()

        self.man_tree.heading(1, text="Number")
        self.man_tree.heading(2, text="Version")
        self.man_tree.heading(3, text="File Name")
        self.man_tree.heading(4, text="Full Name")
        self.man_tree.heading(5, text="Type")

        self.man_tree.column(1, width=150, anchor=Tkconstants.CENTER)
        self.man_tree.column(2, width=100, anchor=Tkconstants.W)
        self.man_tree.column(3, width=300, anchor=Tkconstants.W)
        self.man_tree.column(4, width=300, anchor=Tkconstants.W)
        self.man_tree.column(5, width=150, anchor=Tkconstants.W)

        self.man_tree.tag_configure('used', background=('pale green'))
        self.man_tree.tag_configure('unused', background=('light coral'))
        self.man_tree.tag_configure('unknown', background=('light blue'))
        self.man_tree.tag_configure('+', background=('pale green'))
        self.man_tree.tag_configure('-', background=('light coral'))
        self.man_tree.tag_configure(' ', background=('white'))

        logPack.log_info(self.logger, "Exit init_man_treeview")

    def init_par_treeview(self, master):
        logPack.log_info(self.logger, "Enter init_par_treeview")
        self.par_tree = Ttk.Treeview(self.par_frame, columns=(1, 2, 3), height=40, selectmode="extended",
                                     show="headings")
        self.par_tree.pack()

        self.par_tree.heading(1, text="Parameter Name")
        self.par_tree.heading(2, text="Pararmeter Value")
        self.par_tree.heading(3, text="Comments")

        self.par_tree.column(1, width=250, anchor=Tkconstants.W)
        self.par_tree.column(2, width=250, anchor=Tkconstants.W)
        self.par_tree.column(3, width=500, anchor=Tkconstants.W)

        self.par_tree.tag_configure('used', background=('pale green'))
        self.par_tree.tag_configure('unused', background=('light coral'))
        self.par_tree.tag_configure('unknown', background=('light blue'))
        self.par_tree.tag_configure('+', background=('pale green'))
        self.par_tree.tag_configure('-', background=('light coral'))
        self.par_tree.tag_configure(' ', background=('white'))

        logPack.log_info(self.logger, "Exit init_par_treeview")

    def init_ads_treeview(self, master):
        logPack.log_info(self.logger, "Enter init_ads_treeview")
        self.ads_tree = Ttk.Treeview(self.ads_frame, columns=(1, 2, 3), height=40, selectmode="extended",
                                     show="headings")
        self.ads_tree.pack()

        self.ads_tree.heading(1, text="Parameter Name")
        self.ads_tree.heading(2, text="Pararmeter Value")
        self.ads_tree.heading(3, text="Comments")

        self.ads_tree.column(1, width=250, anchor=Tkconstants.W)
        self.ads_tree.column(2, width=250, anchor=Tkconstants.W)
        self.ads_tree.column(3, width=500, anchor=Tkconstants.W)

        self.ads_tree.tag_configure('used', background=('pale green'))
        self.ads_tree.tag_configure('unused', background=('light coral'))
        self.ads_tree.tag_configure('unknown', background=('light blue'))
        self.ads_tree.tag_configure('+', background=('pale green'))
        self.ads_tree.tag_configure('-', background=('light coral'))
        self.ads_tree.tag_configure(' ', background=('white'))

        logPack.log_info(self.logger, "Exit init_ads_treeview")

    def init_unk_treeview(self, master):
        logPack.log_info(self.logger, "Enter init_unk_treeview")
        self.unk_tree = Ttk.Treeview(self.unk_frame, columns=(1, 2), height=40, selectmode="extended",
                                     show="headings")
        self.unk_tree.pack()

        self.unk_tree.heading(1, text="File Name")
        self.unk_tree.heading(2, text="Type")

        self.unk_tree.column(1, width=600, anchor=Tkconstants.CENTER)
        self.unk_tree.column(2, width=400, anchor=Tkconstants.W)

        self.unk_tree.tag_configure('used', background=('pale green'))
        self.unk_tree.tag_configure('unused', background=('light coral'))
        self.unk_tree.tag_configure('unknown', background=('light blue'))
        self.unk_tree.tag_configure('+', background=('pale green'))
        self.unk_tree.tag_configure('-', background=('light coral'))
        self.unk_tree.tag_configure(' ', background=('white'))

        logPack.log_info(self.logger, "Exit init_unk_treeview")

    def _compare_lst(self, root=None):
        logPack.log_info(self.logger, "Enter _compare_lst")

        if root is None:
            root = self.master

        # Uploading first RUNNING.LST file
        lst_file_1 = tkFileDialog.askopenfilename(initialdir="/", title="Select first RUNNING.LST file",
                                                  filetypes=(("lst files", "*.lst"), ("all files", "*.lst")))
        logPack.log_debug(self.logger, "First file uploaded => %s" % lst_file_1)

        if lst_file_1 in (None, ""):
            logPack.log_debug(self.logger, "User cancellation => No LST File Loaded")
            logPack.log_info(self.logger, "Exit _compare_lst")
            return

        # Uploading second packages.csv file
        lst_file_2 = tkFileDialog.askopenfilename(initialdir="/", title="Select second RUNNING.LST file",
                                                  filetypes=(("lst files", "*.lst"), ("all files", "*.lst")))
        logPack.log_debug(self.logger, "Second file uploaded => %s" % lst_file_2)

        if lst_file_2 in (None, ""):
            logPack.log_debug(self.logger, "User cancellation => No LST File Loaded")
            logPack.log_info(self.logger, "Exit _compare_lst")
            return

        self._do_compare_lst(lst_file_1, lst_file_2, root)

        logPack.log_info(self.logger, "Exit _compare_lst")

    def _do_compare_lst(self, lst_file_1, lst_file_2, root):
        logPack.log_info(self.logger, "Enter _do_compare_lst")

        # Init loaded_package
        self.loaded_package = AppUI.default_package
        self.init_loaded_package(root)

        lst_content_1 = self._get_lst_content(lst_file_1)
        lst_content_2 = self._get_lst_content(lst_file_2)
        lst_content = self._merge_content(lst_content_1, lst_content_2)

        file_path, file_name_1 = os.path.split(lst_file_1)
        file_path, file_name_2 = os.path.split(lst_file_2)
        self.loaded_package['general']['pack_name'] = "%s vs %s" % (file_name_1[:-4], file_name_2[:-4])
        self.loaded_package['general']['catalog_name'] = cpnmgt.ndiff_catalog_name

        self._populate_package_comparison(lst_content, root)

        logPack.log_info(self.logger, "Exit _do_compare_lst")

    def _get_lst_content(self, lst_file):
        logPack.log_info(self.logger, "Enter _get_csv_content")

        the_file = open(lst_file)
        lst_content = the_file.readlines()
        lst_content = [a_line[a_line.find(";") + 1:] for a_line in lst_content]
        lst_content = [a_line[:a_line.find(";")] for a_line in lst_content]
        the_file.close()

        logPack.log_info(self.logger, "Exit _get_csv_content")
        return lst_content

    def _get_cat_content(self, cat_file):
        logPack.log_info(self.logger, "Enter _get_cat_content")
        cat_content = None
        file_path, the_name = os.path.split(cat_file)
        file_name, file_ext = os.path.splitext(the_name)

        if file_ext.upper() == ".PRP":
            cat_content = self._get_cal_content(cat_file)
        elif re.match('.M[0-9][0-9]', file_ext.upper()):
            cat_content = self._get_llt_content(cat_file)

        logPack.log_info(self.logger, "Exit _get_cat_content")
        return cat_content

    def _get_cal_content(self, cat_file):
        logPack.log_info(self.logger, "Enter _get_cal_content")
        catal_file = open(cat_file)
        temp_content = catal_file.readlines()
        cat_content = []
        for line in temp_content:
            if line.startswith("FILE."):
                cat_content.append(line[line.find('=') + 1:].rstrip())
        catal_file.close()

        logPack.log_info(self.logger, "Exit _get_cal_content")
        return cat_content

    def _get_llt_content(self, llt_file):
        logPack.log_info(self.logger, "Enter _get_llt_content")
        lltool_file = open(llt_file)
        temp_content = lltool_file.readlines()
        llt_content = []

        for line in temp_content:
            if not (line.startswith(";") or line.startswith("#")):
                llt_content.append(line.rstrip())
        lltool_file.close()

        logPack.log_info(self.logger, "Exit _get_llt_content")
        return llt_content

    def _compare_csv(self, root=None):
        logPack.log_info(self.logger, "Enter _compare_csv")

        if root is None:
            root = self.master

        # Uploading first packages.csv file
        csv_file_1 = tkFileDialog.askopenfilename(initialdir="/", title="Select first PACKAGE.CSV file",
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.csv")))
        logPack.log_debug(self.logger, "First file uploaded => %s" % csv_file_1)

        if csv_file_1 in (None, ""):
            logPack.log_debug(self.logger, "User cancellation => No LST File Loaded")
            logPack.log_info(self.logger, "Exit _compare_csv")
            return

        # Uploading second packages.csv file
        csv_file_2 = tkFileDialog.askopenfilename(initialdir="/", title="Select second PACKAGE.CSV file",
                                                  filetypes=(("csv files", "*.csv"), ("all files", "*.csv")))
        logPack.log_debug(self.logger, "Second file uploaded => %s" % csv_file_2)

        if csv_file_2 in (None, ""):
            logPack.log_debug(self.logger, "User cancellation => No LST File Loaded")
            logPack.log_info(self.logger, "Exit _compare_csv")
            return

        self._do_compare_csv(csv_file_1, csv_file_2, root)

        logPack.log_info(self.logger, "Exit _compare_csv")

    def _do_compare_csv(self, csv_file_1, csv_file_2, root):
        logPack.log_info(self.logger, "Enter _do_compare_csv")

        # Init loaded_package
        self.loaded_package = AppUI.default_package
        self.init_loaded_package(root)

        csv_content_1 = self._get_csv_content(csv_file_1)
        csv_content_2 = self._get_csv_content(csv_file_2)
        csv_content = self._merge_content(csv_content_1, csv_content_2)

        file_path, file_name_1 = os.path.split(csv_file_1)
        file_path, file_name_2 = os.path.split(csv_file_2)
        self.loaded_package['general']['pack_name'] = "%s vs %s" % (file_name_1[:-4], file_name_2[:-4])
        self.loaded_package['general']['catalog_name'] = cpnmgt.ndiff_catalog_name

        self._populate_package_comparison(csv_content, root)

        logPack.log_info(self.logger, "Exit _do_compare_csv")

    def _merge_content(self, csv_content_1, csv_content_2):
        logPack.log_info(self.logger, "Enter _merge_content")

        csv_content_temp = list(ndiff(csv_content_1, csv_content_2))
        for a_line in csv_content_temp:
            if a_line.find("?") >= 0:
                csv_content_temp.remove(a_line)

        logPack.log_info(self.logger, "Exit _merge_content")
        return csv_content_temp

    def _populate_package_comparison(self, csv_content, root):
        logPack.log_info(self.logger, "Enter _populate_package_comparison")

        file_number = 0

        for file_name in csv_content:
            file_number += 1
            diff_status = file_name[:2]
            f = file_name[2:]

            if len(self.loaded_package['parameter']) == 0:
                self.check_parameter(root, f)

            if len(self.loaded_package['ads_param']) == 0:
                self.check_ads_parameter(root, f)

            sdk_version = self.loaded_package['general']['sdk_version'].upper()
            if sdk_version.startswith("XX.YY.") or len(sdk_version) == 8:
                self.check_t3_sdk_version(f)

            cpn_app = cpnmgt.app_component_present(f)
            if cpn_app != cpnmgt.unknown_component:
                tmp_list = list(cpn_app)
                tmp_list = tmp_list + [f]

                tmp_comp = tmp_list[4]
                tmp_list[3] = cpnmgt.dict_file_types.get(tmp_comp[-3:].upper())
                index = tmp_comp.find(tmp_list[0]) + len(tmp_list[0])
                comp_version = tmp_comp[index:index + 4]

                if comp_version.isdigit():
                    tmp_list = tmp_list + [comp_version[:2] + "." + comp_version[2:]]
                else:
                    tmp_list = tmp_list + [" "]

                tmp_tuple = tuple(tmp_list + [diff_status[0]])
                self.loaded_package['application'].append(tmp_tuple)

            cpn_sys = cpnmgt.sys_component_present(f)
            if cpn_sys != cpnmgt.unknown_component:
                tmp_list = list(cpn_sys)
                tmp_list = tmp_list + [f]

                tmp_comp = tmp_list[3]
                tmp_list[2] = cpnmgt.dict_file_types.get(tmp_comp[-3:].upper())
                index = tmp_comp.find(tmp_list[0]) + len(tmp_list[0])
                comp_version = tmp_comp[index:index + 4]

                if comp_version.isdigit():
                    sversion = comp_version[:2] + "." + comp_version[2:]
                    tmp_list = tmp_list + [sversion]
                    if cpnmgt.check_system_pack(cpn_sys[0]):
                        loaded_sys_version = self.loaded_package['general'].get('system_version')
                        if not loaded_sys_version[:2].isdigit():
                            self.loaded_package['general']['system_version'] = sversion
                        else:
                            self.loaded_package['general']['system_version'] = loaded_sys_version + "-" + sversion
                else:
                    tmp_list = tmp_list + [" "]
                tmp_tuple = tuple(tmp_list + [diff_status[0]])

                self.loaded_package['system'].append(tmp_tuple)

            cpn_man = cpnmgt.man_component_present(f)
            if cpn_man != cpnmgt.unknown_component:
                tmp_list = list(cpn_man)
                tmp_list = tmp_list + [f]

                tmp_comp = tmp_list[3]
                tmp_list[2] = cpnmgt.dict_file_types.get(tmp_comp[-3:].upper())
                index = tmp_comp.find(tmp_list[0]) + len(tmp_list[0])
                comp_version = tmp_comp[index:index + 4]

                if comp_version.isdigit():
                    mversion = "%s.%s" % (comp_version[:2], comp_version[2:])
                    tmp_list = tmp_list + [mversion]
                    if cpnmgt.check_manager_pack(cpn_man[0]):
                        loaded_man_version = self.loaded_package['general'].get('manager_version')
                        if not loaded_man_version[:2].isdigit():
                            self.loaded_package['general']['manager_version'] = mversion
                        else:
                            self.loaded_package['general']['manager_version'] = loaded_man_version + "-" + mversion
                else:
                    tmp_list = tmp_list + [" "]
                tmp_tuple = tuple(tmp_list + [diff_status[0]])

                self.loaded_package['manager'].append(tmp_tuple)

            if cpn_app == cpn_sys and cpn_app == cpn_man:
                tmp_list = list(cpn_man)
                tmp_list = tmp_list + [f]

                tmp_tuple = tuple(tmp_list + [diff_status[0]])
                self.loaded_package['unknown'].append(tmp_tuple)

        if self.loaded_package['general']['sdk_version'].upper().startswith("XX.YY."):
            self.loaded_package['general']['sdk_version'] = cpnmgt.get_sdk_version(
                self.loaded_package['general'].get('system_version'),
                self.loaded_package['general'].get('manager_version')
            )
        self.loaded_package['general']['file_number'] = file_number
        self._populate_gui()

        logPack.log_info(self.logger, "Exit _populate_package_comparison")

    def _get_csv_content(self, csv_file):
        logPack.log_info(self.logger, "Enter _get_csv_content")

        the_file = open(csv_file)
        csv_content = the_file.readlines()
        csv_content = [a_line.replace(';', '', 7) for a_line in csv_content]
        csv_content = [a_line[a_line.find(";") + 1:] for a_line in csv_content]
        csv_content = [a_line[:a_line.find(";")] for a_line in csv_content]
        the_file.close()

        logPack.log_info(self.logger, "Exit _get_csv_content")
        return csv_content

    def _compare_catalog(self, root=None):
        logPack.log_info(self.logger, "Enter _compare_catalog")

        if root is None:
            root = self.master

        # Uploading first Catalog file
        cat_file_1 = tkFileDialog.askopenfilename(initialdir="/", title="Select first Catalog file", filetypes=(
            ("prp files", "*.prp"), ("m** files", "*.m**")))
        logPack.log_debug(self.logger, "First Catalog file uploaded => %s" % cat_file_1)

        if cat_file_1 in (None, ""):
            logPack.log_debug(self.logger, "User cancellation => No Catalog File Loaded")
            logPack.log_info(self.logger, "Exit _compare_catalog")
            return

        # Uploading second Catalog file
        cat_file_2 = tkFileDialog.askopenfilename(initialdir="/", title="Select second Catalog file", filetypes=(
            ("prp files", "*.prp"), ("m** files", "*.m**")))
        logPack.log_debug(self.logger, "Second Catalog file uploaded => %s" % cat_file_2)

        if cat_file_2 in (None, ""):
            logPack.log_debug(self.logger, "User cancellation => No Catalog File Loaded")
            logPack.log_info(self.logger, "Exit _compare_catalog")
            return

        self._do_compare_catalog(cat_file_1, cat_file_2, root)

        logPack.log_info(self.logger, "Exit _compare_catalog")

    def _do_compare_catalog(self, cat_file_1, cat_file_2, root):
        logPack.log_info(self.logger, "Enter _do_compare_lst")

        # Init loaded_package
        self.loaded_package = AppUI.default_package
        self.init_loaded_package(root)

        file_path, file_name_1 = os.path.split(cat_file_1)
        file_path, file_name_2 = os.path.split(cat_file_2)

        cat_content_1 = self._get_cat_content(cat_file_1)
        cat_content_2 = self._get_cat_content(cat_file_2)

        cat_content = self._merge_content(cat_content_1, cat_content_2)

        self.loaded_package['general']['pack_name'] = "%s - %s" % (file_name_1[:-4], file_name_2[:-4])
        self.loaded_package['general']['catalog_name'] = cpnmgt.ndiff_catalog_name

        self._populate_package_comparison(cat_content, root)

        logPack.log_info(self.logger, "Exit _do_compare_lst")

    def _compare_mixed_pack(self, root=None):
        logPack.log_info(self.logger, "Enter _compare_mixed_pack")

        if root is None:
            root = self.master

        # Uploading first Package file
        pack_file_1 = tkFileDialog.askopenfilename(initialdir="/", title="Select First Package file", filetypes=(
            ("prp files", "*.prp"), ("m** files", "*.m**"), ("lst files", "*.lst"), ("csv files", "*.csv")))
        logPack.log_debug(self.logger, "First Package file uploaded => %s" % pack_file_1)

        if pack_file_1 in (None, ""):
            logPack.log_debug(self.logger, "User cancellation => No Package File Loaded")
            logPack.log_info(self.logger, "Exit _compare_mixed_pack")
            return

        # Uploading second Package file
        pack_file_2 = tkFileDialog.askopenfilename(initialdir="/", title="Select Second Package file", filetypes=(
            ("prp files", "*.prp"), ("m** files", "*.m**"), ("lst files", "*.lst"), ("csv files", "*.csv")))
        logPack.log_debug(self.logger, "Second Package file uploaded => %s" % pack_file_2)

        if pack_file_2 in (None, ""):
            logPack.log_debug(self.logger, "User cancellation => No Package File Loaded")
            logPack.log_info(self.logger, "Exit _compare_mixed_pack")
            return

        self._do_compare_mixed_pack(pack_file_1, pack_file_2, root)

        logPack.log_info(self.logger, "Exit _compare_mixed_pack")

    def _do_compare_mixed_pack(self, pack_file_1, pack_file_2, root):
        logPack.log_info(self.logger, "Enter _do_compare_mixed_pack")

        # Init loaded_package
        self.loaded_package = AppUI.default_package
        self.init_loaded_package(root)

        file_path, file_name_1 = os.path.split(pack_file_1)
        file_path, file_name_2 = os.path.split(pack_file_2)

        pack_content_1 = self._get_pack_content(pack_file_1)
        pack_content_2 = self._get_pack_content(pack_file_2)

        cat_content = self._merge_content(pack_content_1, pack_content_2)

        self.loaded_package['general']['pack_name'] = "%s vs %s" % (file_name_1[:-4], file_name_2[:-4])
        self.loaded_package['general']['catalog_name'] = cpnmgt.ndiff_catalog_name

        self._populate_package_comparison(cat_content, root)

        logPack.log_info(self.logger, "Exit _do_compare_mixed_pack")

    def _get_pack_content(self, pack_file):
        logPack.log_info(self.logger, "Enter _get_pack_content")
        pack_content = None
        file_path, the_name = os.path.split(pack_file)
        file_name, file_ext = os.path.splitext(the_name)

        if file_ext.upper() == ".PRP":
            pack_content = self._get_cal_content(pack_file)
        elif re.match('.M[0-9][0-9]', file_ext.upper()):
            pack_content = self._get_llt_content(pack_file)
        elif file_ext.upper() == ".LST":
            pack_content = self._get_lst_content(pack_file)
        elif file_ext.upper() == ".CSV":
            pack_content = self._get_csv_content(pack_file)

        logPack.log_info(self.logger, "Exit _get_pack_content")
        return pack_content


def runAppUI(self):
    root = Tk.Tk()
    app = AppUI(root)
    app.pack()
    root.mainloop()


if __name__ == "__main__":
    runAppUI(self=None)
