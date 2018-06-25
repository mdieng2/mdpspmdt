import Tkinter as Tk
import Tkconstants, tkFileDialog
import mdzipmgt.mdzipmgt as Zip


class AppUI(Tk.Frame):
    _ui_frame = None

    def __init__(self, master=None):
        AppUI_ui_frame = Tk.Frame.__init__(self, master, relief=Tk.SUNKEN, bd=2)
        master.uiFrame = AppUI_ui_frame
        master.title("MD-PSPMGT")
        menubar = Tk.Menu(master)

        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="Load package", accelerator='Ctrl+O', command=self._load_package)
        menu.add_command(label="Save as", accelerator='Ctrl+S', command=self._save_as)
        menu.add_command(label="Quit", accelerator='Ctrl+Q', command=master.quit)

        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=menu)
        menu.add_command(label="Select All", accelerator='Ctrl+A', command=self._select_all)
        menu.add_command(label="Copy", accelerator='Ctrl+C', command=self._copy_selection)
        menu.add_command(label="Bufferize", accelerator='Ctrl+B', command=self._copy_in_clipboard)

        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=menu)
        menu.add_command(label="About", accelerator='Ctrl+H', command=self._app_credentials)

        try:
            master.config(menu=menubar)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            master.tk.call(master, "config", "-menu", menubar)

        self.canvas = Tk.Canvas(self, bg="white", width=800, height=800,
                                bd=0, highlightthickness=0)
        self.canvas.pack()

        #master.bind("<Any-KeyPress>", self._app_credentials)
        master.bind('<Control-O>', self._load_package)
        master.bind('<Control-o>', self._load_package)
        master.bind('<Control-S>', self._save_as)
        master.bind('<Control-s>', self._save_as)
        master.bind('<Control-A>', self._app_credentials)
        master.bind('<Control-a>', self._app_credentials)
        master.bind('<Control-C>', self._select_all)
        master.bind('<Control-c>', self._select_all)
        master.bind('<Control-B>', self._copy_selection)
        master.bind('<Control-b>', self._copy_selection)
        master.bind('<Control-H>', self._copy_in_clipboard)
        master.bind('<Control-h>', self._copy_in_clipboard)
        master.bind('<Control-Q>', self._exit_app)
        master.bind('<Control-q>', self._exit_app)

        """label1 = Tk.Label(master, text="label1")
        #label1.grid(row=0, column=0, sticky="E")
        label1.pack(padx=15, pady=10, side=Tk.LEFT)

        label2 = Tk.Label(master, text="label2")
        #label2.grid(row=0, column=1, sticky="W")
        label2.pack(padx=5, pady=20, side=Tk.LEFT)

        label3 = Tk.Label(master, text="label3")
        #label3.grid(row=1, column=0, sticky="E")
        label3.pack(padx=5, pady=20, side=Tk.LEFT)

        label4 = Tk.Label(master, text="label4")
        #label4.grid(row=1, column=1, sticky="W")
        label4.pack(padx=5, pady=20, side=Tk.BOTTOM)"""


    def _exit_app(self, root=None):
        print "exit_app"
        self.master.quit()

    def _load_package(self, root=None):
        print "Enter load_package"
        root.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("zip files", "*.zip"), ("all files", "*.zip")))
        print (root.filename)
        self._display_package_content(root)
        print "Exit load_package"

    def _save_as(self, root=None):
        print "Save_as"

    def _app_credentials(self, root=None):
        print "app_credentials"

    def _select_all(self, root=None):
        print "select_all"

    def _copy_selection(self, root=None):
        print "copy_selection"

    def _copy_in_clipboard(self, root=None):
        print "copy_in_clipboard"

    def _display_package_content(self, root=None):
        print "Enter _display_package_content"
        print root.filename
        #################
        #Tk.__init__(self)
        t = SimpleTable(self._ui_frame, 10, 2)
        #t.__init__(root, 10, 2) #self._initFrame(root, 10, 2)
        #root.uiFrame.hide()
        t.pack(side="top", fill="x")
        t.set(0, 0, "Hello")
        t.set(0, 1, "Moussa")
        #################
        file_list = Zip.read_zipfile(root.filename)
        for f in file_list:
            print(f)
        """ print "======================================================================================="
            print "|{:.^6}|{:.^6}|{:.^50}|{:.^20}|".format('Name', 'Number', 'File Name', 'Full Name')
            print "======================================================================================="
            for f in file_list:
                cpnent = Cpnent.component_present(f)
                print "|{:.<6}|{:.<6}|{:.<50}|{:.<20}|".format(cpnent[1], cpnent[0], f, cpnent[2])
            """
        print "Exit _display_package_content"

    def _initFrame(self, parent, rows=10, columns=4):
        # use black background so it "peeks through" to
        # form grid lines
        #Tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Tk.Label(self, text="%s/%s" % (row, column),
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


class SimpleTable(Tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to
        # form grid lines
        Tk.Frame.__init__(self, parent, background="black")
        Tk.Frame.grid_configure(self, row=0, column=0, sticky='nsew')
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Tk.Label(self, text="%s/%s" % (row, column),
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


def runAppUI(self):
    root = Tk.Tk()
    app = AppUI(root)
    app.pack()
    root.mainloop()


def testAppUI(self):
    runAppUI(self=None)